import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# load images
car_image = pygame.image.load("car_5.png").convert_alpha()

# set up variables
car_width = 56
car_height = 125
lane_width = WIDTH // 4
car_speed = 5
cars = []
for i in range(4):
    x = i * lane_width + (lane_width - car_width) // 2
    y = -car_height
    cars.append(pygame.Rect(x, y, car_width, car_height))

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move cars
    for car in cars:
        car.y += car_speed

    # spawn new car
    for i in range(4):
        if random.random() < 0.02:
            x = i * lane_width + (lane_width - car_width) // 2
            y = -car_height
            cars.append(pygame.Rect(x, y, car_width, car_height))

    # draw background
    screen.fill(WHITE)

    # draw cars
    for car in cars:
        screen.blit(car_image, car)

    # check for collision
    for car in cars:
        if car.colliderect(pygame.Rect(0, HEIGHT - car_height, WIDTH, car_height)):
            running = False

    # update screen
    pygame.display.flip()

    # set frame rate
    clock.tick(FPS)

# quit Pygame on exit
pygame.quit()