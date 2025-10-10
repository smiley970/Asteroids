from asteroidfield import AsteroidField
from player import Player
import pygame 
from constants import *
from asteroid import Asteroid
from circleshape import *
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots,updatable, drawable)

    player = Player( SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color="black")

        updatable.update(dt)

        for other in asteroids:
            if other.collision(player):
                print("Game over!")
                exit()

    
            for bullet in shots:
                if other.collision(bullet):
                    other.split()
                    bullet.kill()

        dt = clock.tick(60)/ 1000   

        for a in drawable:
            a.draw(screen) 

        pygame.display.flip()
        
        


if __name__ == "__main__":
    main()
