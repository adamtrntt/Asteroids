from constants import *
from player import *
from asteroid import *
from AsteroidField import *

def main():
    import pygame
    pygame.init()

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable_group.update(dt)
        for sprite in drawable_group:
            sprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()