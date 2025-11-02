import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    print("Starting Asteroids!")

    running = True
    while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False


        dt = clock.tick(60) / 1000

        updatable.update(dt)

        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()
