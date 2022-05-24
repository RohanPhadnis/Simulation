import time
import math
import numpy
import pygame
from pygame.locals import *
from scipy.optimize import curve_fit


pygame.init()
SCREEN_DIMS = [1400, 800]
SIM_DIMS = [800, 800]
screen = pygame.display.set_mode(SCREEN_DIMS)
pygame.display.set_caption('Simulation')
trail_surf = pygame.Surface(SIM_DIMS)
trail_surf.fill((20, 20, 20))


scale = 2 * 10 ** 8
# sim to screen
calc = lambda point: [((point[0] / scale * SIM_DIMS[0]) + SIM_DIMS[0]) / 2,
                      SIM_DIMS[1] - ((point[1] / scale * SIM_DIMS[1]) + SIM_DIMS[1]) / 2]
# screen to sim
inv_calc = lambda point: [(point[0] * 2 - SIM_DIMS[0]) / SIM_DIMS[0] * scale,
                          ((SIM_DIMS[1] - point[1]) * 2 - SIM_DIMS[1]) / SIM_DIMS[1] * scale]
function = lambda t, e, d, p: ((e * d) / (1 + e * numpy.sin(t - p)))


def stringify(num):
    if abs(num) >= 10000:
        text = '{:e}'.format(num)
        text = text[0: text.find('.') + 3] + text[text.find('e'): len(text)]
    else:
        text = str(round(num, 2))
    return text


def show_text(text, x, y, size=20):
    font = pygame.font.SysFont('courier', size)
    if type(text) != str:
        text = stringify(text)
    screen.blit(font.render(text, False, (255, 255, 255)), [x, y])


def draw_grid():
    for x in range(-10, 10):
        pygame.draw.line(screen, (150, 150, 150), (x * SIM_DIMS[0] / 20 + SIM_DIMS[0] / 2, 0),
                         (x * SIM_DIMS[0] / 20 + SIM_DIMS[0] / 2, SIM_DIMS[1]), 1)
        if x % 5 == 0:
            show_text(scale * x / 10, x * SIM_DIMS[0] / 20 + SIM_DIMS[0] / 2, SIM_DIMS[1] / 2, size=20)
        # print(scale * x / 10)
    for y in range(-10, 10):
        pygame.draw.line(screen, (150, 150, 150), (0, y * SIM_DIMS[1] / 20 + SIM_DIMS[1] / 2),
                         (SIM_DIMS[0], y * SIM_DIMS[1] / 20 + SIM_DIMS[1] / 2), 1)
        if y % 5 == 0:
            show_text(scale * y / 10, SIM_DIMS[0] / 2, SIM_DIMS[1] - (y * SIM_DIMS[1] / 20 + SIM_DIMS[1] / 2), size=20)
        # print(scale * y / 10)
    pygame.draw.line(screen, (255, 255, 255), (0, SIM_DIMS[1] / 2), (SIM_DIMS[0], SIM_DIMS[1] / 2), 4)
    pygame.draw.line(screen, (255, 255, 255), (SIM_DIMS[0] / 2, 0), (SIM_DIMS[0] / 2, SIM_DIMS[1]), 4)


def draw_trail():
    trail_surf.fill((20, 20, 20))
    for i in range(len(xs)):
        pygame.draw.circle(trail_surf, sat.color, calc([xs[i], ys[i]]), 1)


class Button:

    def __init__(self, text, pos, color):
        self.text = text
        self.pos = pos
        self.dims = [len(self.text) * 20, 40]
        self.color = color
        self.rect = None

    def draw(self):
        self.rect = pygame.draw.rect(screen, self.color, self.pos + self.dims)
        show_text(self.text, self.pos[0] + 5, self.pos[1] + 5)


class Slider:

    def __init__(self, text, pos, domain, length=150, rad=8, step=None):
        self.pos = pos
        self.xpos = pos[0]
        self.length = length
        self.rad = rad
        self.text = text
        self.domain = domain
        self.step = step
        self.rect = None
        self.clicked = False

    def draw(self):
        pygame.draw.line(screen, (255, 255, 255), (self.pos[0], self.pos[1]), (self.pos[0] + self.length, self.pos[1]),
                         2)
        self.rect = pygame.draw.circle(screen, (255, 255, 255), [self.xpos, self.pos[1]], self.rad)
        show_text(self.text + ': ' + self.get_str_val(), self.pos[0], self.pos[1] - 40, size=20)
        show_text(self.domain[0], self.pos[0], self.pos[1], size=20)
        show_text(self.domain[1], self.pos[0] + self.length, self.pos[1], size=20)

    def get_val(self):
        if self.step is None:
            return ((self.xpos - self.pos[0]) / self.length) * (self.domain[1] - self.domain[0]) + self.domain[0]
        else:
            return round(((self.xpos - self.pos[0]) / self.length) * (self.domain[1] - self.domain[0]) / self.step + self.domain[0])

    def get_str_val(self):
        val = self.get_val()
        return stringify(val)


class Particle:

    def __init__(self, pos, mass, color, rad, vel=[0, 0]):
        self.pos = pos
        self.mass = mass
        self.color = color
        self.vel = vel
        self.rad = rad
        self.last_time = 0
        self.clicked = False
        self.rect = None

    def draw(self):
        draw_pos = calc(self.pos)
        if 0 <= draw_pos[0] <= SIM_DIMS[0] and 0 <= draw_pos[1] <= SIM_DIMS[1]:
            self.rect = pygame.draw.circle(screen, self.color, draw_pos, self.rad)

    def move(self, force, current_time):
        acc = [force[0] / self.mass, force[1] / self.mass]
        self.vel = [acc[0] * (current_time - self.last_time) + self.vel[0],
                    acc[1] * (current_time - self.last_time) + self.vel[1]]
        self.pos = [self.vel[0] * (current_time - self.last_time) + self.pos[0],
                    self.vel[1] * (current_time - self.last_time) + self.pos[1]]
        self.last_time = current_time


zoom_in = Button('+', [SCREEN_DIMS[0] - 110, SCREEN_DIMS[1] - 140], (20, 20, 20))
zoom_out = Button('-', [SCREEN_DIMS[0] - 150, SCREEN_DIMS[1] - 140], (20, 20, 20))
run_button = Button('run', [SCREEN_DIMS[0] - 280, SCREEN_DIMS[1] - 140], (0, 150, 150))
reset_button = Button('reset', [SCREEN_DIMS[0] - 300, SCREEN_DIMS[1] - 80], (0, 150, 150))
regress_button = Button('regress', [SCREEN_DIMS[0] - 180, SCREEN_DIMS[1] - 80], (0, 150, 150))
sat_mass = Slider('satellite mass', [SCREEN_DIMS[0] - 570, SCREEN_DIMS[1] - 180], [1, 10 ** 4])
star_mass_coeff = Slider('star mass coeff', [SCREEN_DIMS[0] - 570, SCREEN_DIMS[1] - 100], [0, 1])
star_mass_exp = Slider('star mass exp', [SCREEN_DIMS[0] - 570, SCREEN_DIMS[1] - 30], [20, 32], step=1)
precision = Slider('precision', [SCREEN_DIMS[0] - 275, SCREEN_DIMS[1] - 190], [1, 100])
x_vel_coeff = Slider('X velocity coeff', [SCREEN_DIMS[0] - 570, SCREEN_DIMS[1] - 330], [-1, 1])
x_vel_exp = Slider('X velocity exp', [SCREEN_DIMS[0] - 570, SCREEN_DIMS[1] - 260], [0, 6], step=1)
y_vel_coeff = Slider('Y velocity coeff', [SCREEN_DIMS[0] - 275, SCREEN_DIMS[1] - 330], [-1, 1])
y_vel_exp = Slider('Y velocity exp', [SCREEN_DIMS[0] - 275, SCREEN_DIMS[1] - 260], [0, 6], step=1)
sliders = [sat_mass, star_mass_coeff, star_mass_exp, x_vel_coeff, x_vel_exp, y_vel_coeff, y_vel_exp, precision]
G = 6.67 * 10 ** -11
hyp_calc = lambda pos1, pos2: math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
star = Particle([0, 0], star_mass_coeff.get_val(), (255, 255, 0), 10)
sat = Particle([0, scale / 2], sat_mass.get_val(), (200, 80, 0), 5)
run = False
timer = 0
xs = []
ys = []


def force_calc():
    try:
        mag = G * star.mass * sat.mass / (hyp_calc(sat.pos, star.pos) ** 2)
    except ZeroDivisionError:
        mag = 0
    try:
        angle = math.atan((sat.pos[1] - star.pos[1]) / (sat.pos[0] - star.pos[0]))
    except ZeroDivisionError:
        if sat.pos[1] - star.pos[0] > 0:
            angle = math.atan(math.inf)
        else:
            angle = math.atan(-math.inf)
    if star.pos[0] > sat.pos[0]:
        x_coeff = 1
    else:
        x_coeff = -1
    if star.pos[1] > sat.pos[1]:
        y_coeff = 1
    else:
        y_coeff = -1
    return [x_coeff * math.fabs(mag * math.cos(angle)), y_coeff * math.fabs(mag * math.sin(angle))]
    # return [0, 0]


def ideal_vel_calc():
    hyp = hyp_calc(star.pos, sat.pos)
    try:
        mag = math.sqrt(G * star.mass / hyp)
    except ZeroDivisionError:
        mag = 0
    dx = sat.pos[0] - star.pos[0]
    dy = sat.pos[1] - star.pos[1]
    if dy == 0:
        if dx > 0:
            angle = math.atan(math.inf)
        else:
            angle = math.atan(-math.inf)
    else:
        angle = math.atan(-dx/dy)
    return [mag * math.cos(angle), mag * math.sin(angle)]


def polar_to_rect(rad, theta):
    return [rad * math.cos(theta), rad * math.sin(theta)]


def rect_to_polar(x, y):
    if x == 0:
        if y < 0:
            val = math.atan(-math.inf)
        else:
            val = math.atan(math.inf)
    else:
        val = math.atan(y / x)
        if x < 0 and y or x < 0 and y < 0:
            val += math.pi
    return [math.sqrt(x ** 2 + y ** 2), val]


def regression():
    rs = []
    ts = []
    for i in range(len(xs)):
        rad, theta = rect_to_polar(xs[i], ys[i])
        rs.append(rad)
        ts.append(theta)
    c = curve_fit(function, numpy.array(rs), numpy.array(ts), p0=[1, rs[0], math.pi / 2], maxfev=100000)
    print(c[0])
    return c[0]


def graph(coeffs):
    global graph_points
    if len(graph_points) == 0:
        i = 0
        while i < 2 * math.pi:
            try:
                j = coeffs[0] * coeffs[1] / (1 + coeffs[0] * math.sin(i - coeffs[2]))
                graph_points.append(polar_to_rect(j, i))
            except ZeroDivisionError:
                pass
            i += 2 * math.pi / 100
    for index, point in enumerate(graph_points[:len(graph_points) - 1]):
        pygame.draw.line(screen, (150, 150, 0), calc(point), calc(graph_points[index + 1]), 2)


count = 0
start = time.time()
q = False
show_data = False
coeffs = [0, 0, 0]
graph_points = []


while not q:
    count += 1
    screen.fill((20, 20, 20))
    screen.blit(trail_surf, (0, 0))
    draw_grid()
    pygame.draw.line(screen, (255, 255, 255), (SIM_DIMS[0], 0), (SIM_DIMS[0], SIM_DIMS[1]), 4)
    pygame.draw.line(screen, (255, 255, 255), (SIM_DIMS[0], SCREEN_DIMS[1] / 2), (SCREEN_DIMS[0], SCREEN_DIMS[1] / 2),
                     4)
    show_text('position: <{} m, {} m>'.format(stringify(sat.pos[0]), stringify(sat.pos[1])), SCREEN_DIMS[0] - 550, 50)
    show_text('velocity: <{} m/s, {} m/s>'.format(stringify(sat.vel[0]), stringify(sat.vel[1])), SCREEN_DIMS[0] - 550, 100)
    show_text('speed: {} m/s'.format(stringify(math.sqrt(sat.vel[0] ** 2 + sat.vel[1] ** 2))), SCREEN_DIMS[0] - 550, 150)
    show_text('sat mass: {} kg'.format(stringify(sat.mass)), SCREEN_DIMS[0] - 550, 200)
    show_text('star mass: {} kg'.format(stringify(star.mass)), SCREEN_DIMS[0] - 550, 250)
    show_text('escape speed: {} m/s'.format(stringify(math.sqrt(2 * G * star.mass / hyp_calc(sat.pos, star.pos)))), SCREEN_DIMS[0] - 550, 300)
    show_text('time: {} sec'.format(stringify(timer)), SCREEN_DIMS[0] - 250, 200)
    iv = ideal_vel_calc()
    show_text('ideal velocity: <{} m/s, {} m/s>'.format(stringify(iv[0]), stringify(iv[1])), SCREEN_DIMS[0] - 550, 350)
    show_text('zoom', SCREEN_DIMS[0] - 150, SCREEN_DIMS[1] - 160)
    zoom_in.draw()
    zoom_out.draw()
    run_button.draw()
    reset_button.draw()
    # regress_button.draw()
    sat.draw()
    star.draw()
    for slider in sliders:
        slider.draw()

    if show_data:
        graph(coeffs)
        show_text('r(θ) = ', SCREEN_DIMS[0] - 150, SCREEN_DIMS[1] / 4)
        show_text('{} * {}'.format(stringify(coeffs[0]), stringify(coeffs[1])), SCREEN_DIMS[0] - 130, SCREEN_DIMS[1] / 4 + 10)

    if run:
        xs.append(sat.pos[0])
        ys.append(sat.pos[1])
        sat.move(force_calc(), timer)
        timer += precision.get_val()
        pygame.draw.circle(trail_surf, sat.color, calc([xs[-1], ys[-1]]), 1)
    else:
        sat.mass = sat_mass.get_val()
        star.mass = star_mass_coeff.get_val() * 10 ** star_mass_exp.get_val()
        sat.vel = [x_vel_coeff.get_val() * 10 ** x_vel_exp.get_val(), y_vel_coeff.get_val() * 10 ** y_vel_exp.get_val()]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            q = True
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            if zoom_in.rect.collidepoint(event.pos):
                scale /= 1.2
                draw_trail()
            elif zoom_out.rect.collidepoint(event.pos):
                scale *= 1.2
                draw_trail()
            elif run_button.rect.collidepoint(event.pos):
                run = True
                timer = 0
                sat.last_time = 0
                trail_surf.fill((20, 20, 20))
                xs = []
                ys = []
                show_data = False
            elif reset_button.rect.collidepoint(event.pos):
                run = False
                sat.pos = [xs[0], ys[0]]
            # elif regress_button.rect.collidepoint(event.pos):
            #     show_data = True
            #     coeffs = regression()
            #     graph_points = []
            for slider in sliders:
                slider.clicked = False
            sat.clicked = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            for slider in sliders:
                if slider.rect.collidepoint(event.pos):
                    slider.clicked = True
            if sat.rect.collidepoint(event.pos):
                sat.clicked = True
        elif event.type == MOUSEMOTION:
            for slider in sliders:
                if slider.clicked and slider.pos[0] < event.pos[0] < slider.pos[0] + slider.length:
                    slider.xpos = event.pos[0]
            if sat.clicked and 0 <= event.pos[0] <= SIM_DIMS[0] and 0 <= event.pos[1] <= SIM_DIMS[1]:
                sat.pos = inv_calc(event.pos)
    if not q:
        pygame.display.update()

print(count / (time.time() - start))
