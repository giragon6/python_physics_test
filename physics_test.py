import pygame
from ball import Ball

# press space to go up!

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    ball = Ball(screen, 250, 250, 25, vx=-20) # vx = starting x velocity

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            ball.pos.y -= 5

        screen.fill((255, 255, 255))

        ball.update()
        ball.draw()

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()