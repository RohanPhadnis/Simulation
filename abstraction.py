import time
import random
import math
import threading
import pygame
from pygame.locals import *


def show_text(window, text: str, x: int, y: int, size: int = 30, color: tuple = (255, 255, 255)) -> None:
    font = pygame.font.SysFont('times', size)
    window.blit(font.render(text, False, color), [x, y])


# Button: a class to handle rectangular buttons
# superclass: Obstacle
# subclass: none
class Button:

    # constructor
    def __init__(self, text: str, x: int, y: int, color: tuple):
        self.pos = [x, y]
        self.text = text
        self.dim = [len(text) * 25, 50]
        self.color = color
        self.text = text
        self.rect = None

    # draw: a function to render the Button on the screen
    # params:
    #   - self (Button)
    # returns -> None
    def draw(self, window) -> None:
        self.rect = pygame.draw.rect(window, self.color, self.pos + self.dim)
        show_text(window, self.text, self.pos[0] + 10, self.pos[1] + 10)


# Slider: a class to handle sliders
# superclass: object
# subclass: none
class Slider:

    # constructor
    def __init__(self, label: str, position: list, domain: range, width: int = 100):
        self.label = label
        self.position = position
        self.width = width
        self.current_position = self.position[0]
        self.domain = domain
        self.clicked = False
        self.radius = 10
        self.rect = None

    # get_val: a function to extract the numerical value of the Slider
    # params:
    #   - self (Slider)
    # returns -> int: an integer value of the Slider's position relative to its domain
    def get_val(self) -> int:
        return round((self.domain.stop - self.domain.start) * (
                self.current_position - self.position[0]) / self.width) + self.domain.start

    # draw: a function to render a Slider on the screen
    # params:
    #   - self (Slider)
    # returns -> None
    def draw(self, window) -> None:
        pygame.draw.line(window, (0, 0, 0), self.position, [self.position[0] + self.width, self.position[1]], 2)
        self.rect = pygame.draw.circle(window, (0, 0, 0), [self.current_position, self.position[1]], self.radius)
        show_text(window, str(self.domain.start), self.position[0], self.position[1] - 10, color=(0, 0, 0))
        show_text(window, str(self.domain.stop), self.position[0] + self.width, self.position[1] - 10, color=(0, 0, 0))
        # show_text(self.label + ': ' + str(self.get_val()), self.position[0], self.position[1] + 30, color=(0, 0, 0))

    # detect_click: a function to detect mouse clicks on the Slider
    # params:
    #   - self (Slider)
    #   - click_position (tuple): the coordinates of the mouse click
    # returns -> bool: a boolean value indicating if the Slider is clicked
    # def detect_click(self, click_position: tuple) -> bool:
    #     return ((self.current_position - self.radius <= click_position[0] <= self.current_position + self.radius) and (
    #             self.position[1] - self.radius <= click_position[1] <= self.position[1] + self.radius))


class Particle:

    def __init__(self, x, y, mass=1, vel=None, color=(255, 0, 0), rad=5):
        if vel is None:
            vel = [0, 0]
        self.pos = [x, y]
        self.mass = mass
        self.rect = None
        self.color = color
        self.vel = vel
        self.old_pos = self.pos.copy()
        self.old_vel = self.vel.copy()
        self.last_time = 0  # change to time.time() for using real-time systems
        self.rad = rad
        self.force = [0, 0]
        self.momenta = []

    def draw(self, window):
        self.rect = pygame.draw.circle(window, self.color, self.pos, self.rad)

    def move(self, current_time):
        if len(self.momenta) != 0:
            self.vel = [0, 0]
            for vel in self.momenta:
                self.vel[0] += vel[0]
                self.vel[1] += vel[1]
            self.momenta = []

        self.old_pos = self.pos.copy()
        self.old_vel = self.vel.copy()

        self.vel[0] += (self.force[0] * (current_time - self.last_time)) / self.mass
        self.vel[1] += (self.force[1] * (current_time - self.last_time)) / self.mass

        self.pos[0] += self.vel[0] * (current_time - self.last_time)
        self.pos[1] += self.vel[1] * (current_time - self.last_time)

        self.last_time = current_time
        self.force = [0, 0]

    def impulse(self, new_vel):
        self.momenta.append(new_vel)

    def update_force(self, force):
        self.force[0] += force[0]
        self.force[1] += force[1]


G = 6.67 * 10 ** -11
hyp_calc = lambda vector1, vector2: math.sqrt((vector1[0] - vector2[0]) ** 2 + (vector1[1] - vector2[1]) ** 2)
energy_calc = lambda mass, vel: 0.5 * mass * (vel[0] ** 2 + vel[1] ** 2)
momentum_calc = lambda mass, vel: [mass * vel[0], mass * vel[1]]
collisions = []


def angle_calc(point1, point2):
    x = point2[0] - point1[0]
    y = point2[1] - point1[1]
    if x != 0:
        return math.atan(y / x)
    else:
        return math.pi / 2


def gravity_handler(particles, current_time):
    for index1, particle1 in enumerate(particles):
        if index1 + 1 < len(particles):
            for index2, particle2 in enumerate(particles[index1 + 1:]):
                pos = particle2.pos
                if hyp_calc(particle1.pos, pos) != 0:
                    force_mag = G * particle1.mass * particle2.mass / ((hyp_calc(particle1.pos, pos)) ** 2)
                else:
                    force_mag = 0
                angle = angle_calc(particle1.pos, pos)
                if pos[0] < particle1.pos[0]:
                    x_coeff = -1
                else:
                    x_coeff = 1
                if pos[1] < particle1.pos[1]:
                    y_coeff = -1
                else:
                    y_coeff = 1
                particle1.update_force([x_coeff * math.fabs(force_mag * math.cos(angle)),
                                        y_coeff * math.fabs(force_mag * math.sin(angle))])
                particle2.update_force([-x_coeff * math.fabs(force_mag * math.cos(angle)),
                                        -y_coeff * math.fabs(force_mag * math.sin(angle))])
        particle1.move(current_time)


def physics_handler(particles, current_time):
    global collisions
    for index1, particle1 in enumerate(particles):
        if index1 + 1 < len(particles):
            for index2, particle2 in enumerate(particles[index1 + 1:]):
                pos = particle2.pos
                if hyp_calc(particle1.pos, pos) != 0:
                    force_mag = G * particle1.mass * particle2.mass / ((hyp_calc(particle1.pos, pos)) ** 2)
                else:
                    force_mag = 0
                angle = angle_calc(particle1.pos, pos)
                if pos[0] < particle1.pos[0]:
                    x_coeff = -1
                else:
                    x_coeff = 1
                if pos[1] < particle1.pos[1]:
                    y_coeff = -1
                else:
                    y_coeff = 1
                particle1.update_force([x_coeff * math.fabs(force_mag * math.cos(angle)),
                                        y_coeff * math.fabs(force_mag * math.sin(angle))])
                particle2.update_force([-x_coeff * math.fabs(force_mag * math.cos(angle)),
                                        -y_coeff * math.fabs(force_mag * math.sin(angle))])
                if particle1.rect is not None and particle2.rect is not None and particle2.rect.colliderect(particle1.rect):
                    if [index1, index1 + index2 + 1] not in collisions:
                        vel1 = [
                            ((particle1.mass - particle2.mass) * particle1.vel[0] + 2 * particle2.mass * particle2.vel[0]) / (particle1.mass + particle2.mass),
                            ((particle1.mass - particle2.mass) * particle1.vel[1] + 2 * particle2.mass * particle2.vel[
                                1]) / (particle1.mass + particle2.mass)
                        ]
                        vel2 = [
                            ((particle2.mass - particle1.mass) * particle2.vel[0] + 2 * particle1.mass * particle1.vel[0]) / (particle1.mass + particle2.mass),
                            ((particle2.mass - particle1.mass) * particle2.vel[1] + 2 * particle1.mass * particle1.vel[
                                1]) / (particle1.mass + particle2.mass)
                        ]
                        particle1.impulse(vel1.copy())
                        particle2.impulse(vel2.copy())
                        collisions.append([index1, index1 + index2 + 1])
                else:
                    if [index1, index1 + index2 + 1] in collisions:
                        collisions.remove([index1, index1 + index2 + 1])
        particle1.move(current_time)