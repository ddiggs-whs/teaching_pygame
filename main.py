import pygame

pygame.init()

WINDOWWIDTH = 800
WINDOWHEIGHT = 600

DISPLAY = pygame.display.set_mode([WINDOWWIDTH, WINDOWHEIGHT])
FPSCLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
left = 50
top = 50
width = 40
height = 40
x_speed = 5
y_speed = 5
x_color = RED
mos_pos = (0, 0)


class BouncingRectangle(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

        self.x_color = RED

        self.image.fill(WHITE)
        pygame.draw.line(self.image, self.x_color, self.rect.topleft, self.rect.bottomright, 10)
        pygame.draw.line(self.image, self.x_color, self.rect.bottomleft, self.rect.topright, 10)

        self.x_speed = 5
        self.y_speed = 5

    def update(self):
        self.rect.x += self.x_speed
        if self.rect.right >= WINDOWWIDTH:
            self.x_speed *= -1
            self.rect.x += self.x_speed
        if self.rect.left <= 0:
            self.x_speed *= -1
            self.rect.x += self.x_speed

        self.rect.y += self.y_speed
        if self.rect.bottom >= WINDOWHEIGHT:
            self.y_speed *= -1
            self.rect.y += self.y_speed
        if self.rect.top <= 0:
            self.y_speed *= -1
            self.rect.y += self.y_speed


my_rectangle = BouncingRectangle(80, 80)
my_group = pygame.sprite.Group()
my_group.add(my_rectangle)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    DISPLAY.fill(BLACK)

    my_group.update()
    my_group.draw(DISPLAY)


    pygame.display.update()
    FPSCLOCK.tick(30)