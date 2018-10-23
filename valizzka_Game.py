import pygame
import random
import helper
pygame.init()
pygame.font.init()

# images
background_img = pygame.transform.scale(
    pygame.image.load('background.jpg'), (1000, 500))
wall_img = pygame.image.load('wall.png')
magician_img = pygame.image.load('magician.png')
flask_img_lst = ['flask_blue.png', 'flask_red.png']
# consts
types_num = ["Ulam", "Lucky", "Prime"]
myfont = pygame.font.SysFont('Comic Sans MS', 20)
# colors
white = (255, 255, 255)
black = (0, 0, 0)

done = False
flask_lst = []
col_flasks = 10
score = 0
step = 0
type_of_num = "Ulam"


class Flask():
    def __init__(self):
        self.x = random.randint(100, 900)
        self.y = random.randint(100, 400)
        self.img = pygame.image.load(flask_img_lst[random.randint(0, 1)])
        self.move_x = 1 + random.random()
        self.move_y = 1 + random.random()
        self.num = helper.GenNumbers(flask_lst)


def move(flasks):
    for flask in flasks:
        textsurface = myfont.render(str(flask.num), False, white)
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
            global score, step, type_of_num
            if (type_of_num == 'Ulam') and (helper.isUlam(int(flask.num)) == True):
                score += 1
            if (type_of_num == 'Prime') and (helper.isPrime(int(flask.num)) == True):
                score += 1
            if (type_of_num == 'Lucky') and (helper.isLucky(int(flask.num)) == True):
                score += 1
            step += 1
            type_of_num = random.choice(types_num)
            break


def draw_game():
    screen.blit(background_img, (0, 0))
    screen.blit(wall_img, (0, 250))
    screen.blit(magician_img, (0, 100))
    pygame.draw.rect(screen, white, pygame.Rect(5, 5, 100, 60))
    textsurface = myfont.render(type_of_num, False, black)
    screen.blit(textsurface, (30, 25))


def draw_menu(score):
    pygame.draw.rect(screen, black, pygame.Rect(200, 200, 200, 60))
    pygame.draw.rect(screen, black, pygame.Rect(500, 200, 200, 60))
    textsurface = myfont.render("Score " + str(score), False, white)
    screen.blit(textsurface, (200, 200))
    textsurface = myfont.render("Try again", False, white)
    screen.blit(textsurface, (500, 200))


for i in range(col_flasks):
    flask_lst.append(Flask())

screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()

while not done:
    if (step == 10):
        screen.fill(white)
        draw_menu(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if (event.type == pygame.MOUSEBUTTONUP):
                mouse = pygame.mouse.get_pos()
                if (700 > mouse[0] > 500) and (260 > mouse[1] > 200):
                    step = 0
                    score = 0
    else:
        draw_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                click(pygame.mouse.get_pos(), flask_lst)

        move(flask_lst)
    pygame.display.flip()
    clock.tick(60)
