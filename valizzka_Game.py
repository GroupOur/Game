import pygame
import random
#import addition
pygame.init()
pygame.font.init()
img_lst = ['flask_blue.png', 'flask_red.png']


class Flask():
    def __init__(self):
        self.x = random.randint(100, 900)
        self.y = random.randint(100, 400)
        self.img = pygame.image.load(img_lst[random.randint(0, 1)])
        self.move_x = 1 + random.random()
        self.move_y = 1 + random.random()
        self.num = '99'


def move(flasks):
    for flask in flasks:
        textsurface = myfont.render(flask.num, False, white)
        if (flask.x >= 920) or (flask.x <= 100):
            flask.move_x *= -1
        if (flask.y >= 420) or (flask.y <= 0):
            flask.move_y *= -1
        flask.x += flask.move_x
        flask.y += flask.move_y
        screen.blit(flask.img, (flask.x, flask.y))
        screen.blit(textsurface, (flask.x + 35, flask.y + 40))


def click(mouse, flasks):
    for flask in flasks:
        if (flask.x + 80 > mouse[0] > flask.x) and\
                (flask.y + 80 > mouse[1] > flask.y):
            flasks.remove(flask)
            flasks.append(Flask())
            global score, step
            score += 1
            step += 1
            print(step)
            break


screen = pygame.display.set_mode((1000, 500))
myfont = pygame.font.SysFont('Comic Sans MS', 20)
white = (255, 255, 255)
done = False
flask_lst = []
col_flasks = 10
score = 0
step = 0
for i in range(col_flasks):
    flask_lst.append(Flask())

clock = pygame.time.Clock()
while not done:
    if (step == 5):
        screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
    else:
        mouse = (-1, -1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                click(pygame.mouse.get_pos(), flask_lst)

        screen.fill(white)
        move(flask_lst)
    pygame.display.flip()
    clock.tick(60)
