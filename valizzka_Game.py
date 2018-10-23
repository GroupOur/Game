import pygame
import random
import valizzka_helper
pygame.init()
pygame.font.init()

# consts
types_num = ["Ulam", "Lucky", "Prime"]
myfont = pygame.font.SysFont('Comic Sans MS', 20)
max_step = 10
size_window_x = 1000
size_window_y = 500
# images
background_img = pygame.image.load('background.png')
flask_img_lst = ['flask_blue.png', 'flask_red.png']
# colors
white = (255, 255, 255)
black = (0, 0, 0)

# class that represet flasks in game
# Flask object has coordinates, image, number, directions in which object should move


class Flask():
    def __init__(self):
        self.x = random.randint(100, size_window_x - 100)
        self.y = random.randint(100, size_window_y - 200)
        self.img = pygame.image.load(random.choice(flask_img_lst))
        self.move_x = 1.1 + random.random()
        self.move_y = 1.1 + random.random()
        self.num = valizzka_helper.GenNumbers(flask_lst)

# Function move each flask


def move(flasks):
    for flask in flasks:
        textsurface = myfont.render(str(flask.num), False, white)
        if (flask.x >= 920) or (flask.x <= 100):
            flask.move_x *= -1
        if (flask.y >= 380) or (flask.y <= 0):
            flask.move_y *= -1
        flask.x += flask.move_x
        flask.y += flask.move_y
        screen.blit(flask.img, (flask.x, flask.y))
        screen.blit(textsurface, (flask.x + 27, flask.y + 33))

# Function remove clicked flask and generate new flask


def click_flask(mouse, flasks):
    for flask in flasks:
        if (flask.x + 80 > mouse[0] > flask.x) and\
                (flask.y + 80 > mouse[1] > flask.y):
            flasks.remove(flask)
            flasks.append(Flask())
            global score, step, type_of_num
            if (type_of_num == 'Ulam'):
                if (valizzka_helper.isUlam(int(flask.num)) == True):
                    score += 1
                else:
                    score -= 2
            if (type_of_num == 'Prime'):
                if (valizzka_helper.isPrime(int(flask.num)) == True):
                    score += 1
                else:
                    score -= 2
            if (type_of_num == 'Lucky'):
                if (valizzka_helper.isLucky(int(flask.num)) == True):
                    score += 1
                else:
                    score -= 2
            step += 1
            type_of_num = random.choice(types_num)
            break

# Function start new game


def click_try_again(mouse):
    global score, step
    if (700 > mouse[0] > 500) and (260 > mouse[1] > 200):
        step = 0
        score = 0
# Function draw the game background


def draw_game():
    screen.blit(background_img, (0, 0))
    pygame.draw.rect(screen, white, pygame.Rect(5, 5, 100, 20))
    textsurface = myfont.render(type_of_num, False, black)
    screen.blit(textsurface, (30, 0))

# Function draw menu background


def draw_menu(score):
    screen.blit(background_img, (0, 0))
    pygame.draw.rect(screen, black, pygame.Rect(200, 200, 200, 60))
    pygame.draw.rect(screen, black, pygame.Rect(500, 200, 200, 60))
    textsurface = myfont.render("Score " + str(score), False, white)
    screen.blit(textsurface, (200, 200))
    textsurface = myfont.render("Try again", False, white)
    screen.blit(textsurface, (500, 200))


# main
done = False
flask_lst = []
col_flasks = 10
score = 0
step = 0
type_of_num = "Ulam"

for i in range(col_flasks):
    flask_lst.append(Flask())

screen = pygame.display.set_mode((size_window_x, size_window_y))
clock = pygame.time.Clock()

while not done:
    if (step == max_step):
        draw_menu(score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                click_try_again(mouse)
    else:
        draw_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                click_flask(mouse, flask_lst)

        move(flask_lst)

    pygame.display.flip()
    clock.tick(60)
