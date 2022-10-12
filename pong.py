import pygame, sys
import random
#from pygame import * DO NOT IMPORT ALL IT BREAKS THE CODE
pygame.init()


screen = pygame.display.set_mode((800,600))
pygame.display.Surface=('black')
pygame.display.set_caption('pygame pong')


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        self.coordinate = pygame.Rect(30, 200, 60, 120)
        self.color = (255,255,255)
        self.Surface = screen

    def draw(self):
        pygame.draw.rect(self.Surface, self.color, self.coordinate)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.coordinate.top > 0:
            if pressed_keys[pygame.K_w]:
                self.coordinate.move_ip(0, -5)
        if self.coordinate.bottom < 600:
            if pressed_keys[pygame.K_s]:
                self.coordinate.move_ip(0,5)

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        self.coordinate = pygame.Rect(710, 200, 60, 120)
        self.color = (255,255,255)
        self.Surface = screen

    def draw(self):
        pygame.draw.rect(self.Surface, self.color, self.coordinate)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.coordinate.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.coordinate.move_ip(0, -5)
        if self.coordinate.bottom < 600:
            if pressed_keys[pygame.K_DOWN]:
                self.coordinate.move_ip(0,5)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.Surface = screen
        self.color = (255,255,255)
        self.coordinate = pygame.Rect(19, 200, 10, 10)
        self.radius = 5

    def draw(self):
        pygame.draw.rect(self.Surface, self.color, self.coordinate)

    def move(self):
        #make sure to set class to variable or init will be called every loop see line 93
        if pygame.key.get_pressed()[pygame.K_w]:
            self.coordinate.move_ip(0,5)
            #for paddle physcics make x movment value negative on collition
            #when coliding with top walls make y movement neg

class Score(Ball):
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.regfont = pygame.font.Font(None, 50)
        #inherit ball coordiante
        self.ballcoordinate = Ball().coordinate
    def draw(self):
        self.text_surface = self.regfont.render(f"Score: {self.score1} - {self.score2}", False, 'White')
        screen.blit(self.text_surface, (300, 50))
    def scoreincrease(self):
        if self.ballcoordinate.left < 20:
            self.score2 += 1
        if self.ballcoordinate.right > 800:
            self.score1 += 1












P1 = Player1()
P2 = Player2()
ball = Ball()
score = Score()



clockobject = pygame.time.Clock()
#gameloop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            sys.exit()

    clockobject.tick(60)
    pygame.display.flip()
    screen.fill((0, 0, 0))

    score.draw()
    P1.draw()
    P1.move()
    P2.draw()
    P2.move()
    ball.move()
    ball.draw()
    score.scoreincrease()

















