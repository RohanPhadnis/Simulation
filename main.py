from abstraction import *

width = 720
height = 720
pygame.init()
screen = pygame.display.set_mode((width, height))
trails = pygame.Surface((width, height))
trails.fill((0, 0, 0))

particles = [Particle(x=width/2-120, y=height/2, mass=10**15, vel=[1, 2], rad=5, color=(0, 255, 255)),
             Particle(x=width/2+120, y=height/2, mass=10**15, vel=[-1, -2], rad=5, color=(255, 0, 255)),
             Particle(x=width/2, y=height/2, mass=10**16, rad=10, color=(255, 255, 0), vel=[0, -1])]

# particles = [Particle(x=random.random() * width, y=random.random()*height, vel=[random.choice([-1, 1]) * random.random()/10, random.choice([-1, 1]) * random.random()/10]) for _ in range(200)]
# #particles.append(Particle(x=width/2, y=height/2, color=(255, 255, 255), mass=10**22, rad=20))
run = True
start = 0
t = time.time()

def processing():
    global start
    while run:
        physics_handler(particles, start)
        start += 10**-4

thread1 = threading.Thread(target=processing)
thread1.start()

while run:
    pygame.display.update()
    screen.blit(trails, (0, 0))
    energy = 0
    for particle in particles:
        particle.draw(screen)
        pygame.draw.circle(trails, particle.color, particle.pos, 1)
        energy += energy_calc(particle.mass, particle.vel)
        if particle.pos[0] < 0:
            particle.vel[0] = abs(particle.vel[0])
        elif particle.pos[0] > width:
            particle.vel[0] = -1 * abs(particle.vel[0])
        if particle.pos[1] < 0:
            particle.vel[1] = abs(particle.vel[1])
        elif particle.pos[1] > height:
            particle.vel[1] = -1 * abs(particle.vel[1])
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                trails.fill((0, 0, 0))

print(start / (time.time() - t))
