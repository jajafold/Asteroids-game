import pygame
from Vector2D import *

WIDTH = 1200
HEIGHT = 700

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("noname_game")
bg = pygame.image.load('bg.png')


def main():
    global win
    pygame.init()
    clock = pygame.time.Clock()

    ship = Ship()

    run = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ship.update()
        pygame.display.update()
        win.blit(bg, (0, 0))


class Ship:

    acceleration = 1
    reverse_acceleration = -0.05
    maxVelocity = 10
    angle = 0

    ROTATION_ANGLE = 0

    x = 500
    y = 500

    def __init__(self):
        self.ship_image = pygame.image.load('ship.png')
        self.direction = Vector2D(0, -1)
        self.velocity = Vector2D(0, 0)

    def rot_center(self, angle):
        rotated_image = pygame.transform.rotate(self.ship_image, angle)
        new_rect = rotated_image.get_rect(center=self.ship_image.get_rect(center=(self.x, self.y)).center)

        return rotated_image, new_rect

    def update(self):
        global win

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_a]:
            self.direction = self.direction.rotate(angle=-0.17)
            self.angle += 10

        elif self.keys[pygame.K_d]:
            self.direction = self.direction.rotate(angle=0.17)
            self.angle -= 10

        elif self.keys[pygame.K_s] and self.y <= HEIGHT:
            self.velocity -= self.direction.multiply(self.acceleration)

        elif self.keys[pygame.K_w] and self.y >= 0:
            self.velocity += self.direction.multiply(self.acceleration)

        if self.y >= HEIGHT + 66:
            self.y = -33
        if self.y < -66:
            self.y = HEIGHT + 33
        if self.x >= WIDTH + 66:
            self.x = -33
        if self.x < -66:
            self.x = WIDTH + 33
            
        if self.velocity.length >= self.maxVelocity:
            pass

        self.y += self.velocity.y
        self.x += self.velocity.x

        self.b = self.rot_center(self.angle)
        win.blit(self.b[0], (self.b[1].x, self.b[1].y))


if __name__ == '__main__':
    main()
