import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys


def main():
    #Sets up the game screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Sets up our containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True: #Main game loop
        log_state()
        updatable.update(dt)

        for asteroid in asteroids: #Checks for collisions with player
            result = asteroid.collides_with(Player1)
            if result:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for event in pygame.event.get(): #Checks for user closing game
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") #Draws everything to the screen
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
