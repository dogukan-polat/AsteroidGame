import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = updatable
    asteroid_fields = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision_with(asteroid):
                print("Game over!")
                sys.exit()

        pygame.Surface.fill(screen, (0, 0, 0))

        for obj in drawable:
            obj.draw(screen)
    
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()