import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 32)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField()

    text = font.render('TEST KASJHDLKJHFG', True, (255, 255, 255), (0, 0, 0))
    rect = text.get_rect()
    rect.center = (100, 100)
    while True:
        screen.fill("black")
        screen.blit(text, rect) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for a in asteroids:
            if a.colliding(player):
                print('Game over!')
                return
            for shot in shots:
                if a.colliding(shot):
                    a.split()
                    shot.kill()
            
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
