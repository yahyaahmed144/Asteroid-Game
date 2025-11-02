import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

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

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                raise SystemExit
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  # remove asteroid from all groups
                    shot.kill()      # remove shot from all groups
                    break  



        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
    pygame.quit()



if __name__ == "__main__":
    main()
