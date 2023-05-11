
import pygame, sys
from pygame.locals import *
import random

pygame.init()
# Set up pygame window
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Car Racing Game')

# Load images and sounds
car_img = pygame.image.load('car_5.png')
other_car_img = pygame.image.load('car_1.png')
other_car_img1 = pygame.image.load('car_2.png')
other_car_img2 = pygame.image.load('car_3.png')
other_car_img3 = pygame.image.load('car_4.png')

# Set up game objects
player_car = pygame.Rect(350, 500, 40, 70)
other_cars = []
for i in range(4):
    car = pygame.Rect(random.randint(200, 700), random.randint(-150, -5), 40, 70)
    other_cars.append(car)

clock = pygame.time.Clock()
score = 0 # initialize score to zero

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_car.left > 200:
        player_car.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player_car.right < 600:
        player_car.move_ip(5, 0)
    if keys[pygame.K_UP] and player_car.top > 0:
        player_car.move_ip(0, -5)
    if keys[pygame.K_DOWN] and player_car.bottom < 600:
        player_car.move_ip(0, 5)

    # Move other cars at random speeds
    for car in other_cars:
        car.move_ip(0, random.randint(5, 10))

    # Detect collision
    for car in other_cars:
        if player_car.colliderect(car):
            pygame.time.delay(500)
            pygame.quit()
            sys.exit()

    # Check if player has passed another car
    for car in other_cars:
        if player_car.top < car.bottom:
            score += 1
            other_cars.remove(car)
            other_cars.append(pygame.Rect(random.randint(200, 700), random.randint(-150, -5), 40, 70))

    # Draw game objects
    window.fill((255, 255, 255))
    for car in other_cars:
        window.blit(other_car_img, car)
    window.blit(car_img, player_car)

    # Display score
    font = pygame.font.Font(None, 30)
    text = font.render('Score: ' + str(score), True, (0, 0, 0))
    window.blit(text, (10, 10))

    # Update Pygame display
    pygame.display.update()

    # Set the tick speed
    clock.tick(30)
