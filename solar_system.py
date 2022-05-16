from abstraction import *

width = 1200
height = 720
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simulation')
trails_surf = pygame.Surface((width, height))
graphics_counts = 0
proc_counts = 0


def show_text(text, x, y, color=(255, 255, 255)):
    font = pygame.font.SysFont('freesans', 40)
    textobj = font.render(text, False, color)
    screen.blit(textobj, (x, y))


moon = Particle(x=-3.48 * 10 ** 8, y=1.5 * 10 ** 11, vel=[3 * 10 ** 4, -1.22 * 10 ** 3], color=(255, 255, 255),
                mass=7.35 * 10 ** 22, rad=4)
earth = Particle(x=0, y=1.5 * 10 ** 11, vel=[3 * 10 ** 4, 0], color=(0, 0, 255), mass=5.97 * 10 ** 24, rad=8)
sun = Particle(x=0, y=0, vel=[0, 0], mass=1.99 * 10 ** 30, rad=20, color=(255, 255, 0))
particles = [moon, earth, sun]
com = [0, 0]
mass = 0
scale = (2 * 1.5 * 10 ** 11) / (height * 0.75)
seconds = 0

for particle in particles:
    mass += particle.mass

run = True
start = 0


def processing():
    global run, start, seconds, particles, proc_counts
    time.sleep(8)
    start = time.time()
    while run:
        if not run:
            break
        physics_handler(particles, seconds)
        proc_counts += 1
        seconds += 20
    run = False


thread = threading.Thread(target=processing)
thread.start()

while run:
    screen.fill((0, 0, 0))
    screen.blit(trails_surf, (0, 0))
    com = [0, 0]
    for particle in particles:
        com[0] += particle.mass * particle.pos[0] / mass
        com[1] += particle.mass * particle.pos[1] / mass
    pygame.draw.circle(screen, (255, 255, 255), (
        com[0] / scale + width / 2, com[1] / scale + height / 2
    ), 5)

    pygame.draw.circle(trails_surf, sun.color,
                       (sun.pos[0] / scale + width / 2, sun.pos[1] / scale + height / 2),
                       1)
    pygame.draw.circle(screen, sun.color,
                       (sun.pos[0] / scale + width / 2, sun.pos[1] / scale + height / 2),
                       sun.rad)
    pygame.draw.circle(trails_surf, earth.color,
                       (earth.pos[0] / scale + width / 2, earth.pos[1] / scale + height / 2),
                       1)
    pygame.draw.circle(screen, earth.color,
                       (earth.pos[0] / scale + width / 2, earth.pos[1] / scale + height / 2),
                       earth.rad)
    pygame.draw.circle(trails_surf, moon.color,
                       ((moon.pos[0] + 10 * (moon.pos[0] - earth.pos[0])) / scale + width / 2,
                        (moon.pos[1] + 10 * (moon.pos[1] - earth.pos[1])) / scale + height / 2),
                       1)
    pygame.draw.circle(screen, moon.color,
                       ((moon.pos[0] + 10 * (moon.pos[0] - earth.pos[0])) / scale + width / 2,
                        (moon.pos[1] + 10 * (moon.pos[1] - earth.pos[1])) / scale + height / 2),
                       moon.rad)

    show_text('days: ' + str((seconds / 3600) / 24), width - 400, 50)
    show_text('data points: ' + str(proc_counts), width - 400, 100)
    show_text('earth velocity: ' + str(math.sqrt(earth.vel[0] ** 2 + earth.vel[1] ** 2)), width - 400, 150)
    show_text('moon velocity: ' + str(math.sqrt(moon.vel[0] ** 2 + moon.vel[1] ** 2)), width - 400, 200)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                trails_surf.fill((0, 0, 0))
    pygame.display.update()
    graphics_counts += 1
    # time.sleep(10)

print('graphics_counts:', graphics_counts / (time.time() - start))
print('proc_counts:', proc_counts / (time.time() - start))
pygame.quit()
exit()
