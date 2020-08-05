import pygame
import random
import sys
from time import sleep

pygame.font.init()
pygame.init()                  
pygame.display.set_caption('Rong')                
screen = pygame.display.set_mode([700,600])
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)


RED = (200,0,0)
BLACK = (0,0,0)
BLUE = (0,0,250)
YELLOW = (250,200,0)
WHITE = (255,255,255)

P1pos = [20,300]
P2pos = [650,300]
PSize = [30,150]

Up1 = pygame.K_UP
Down1 = pygame.K_DOWN
Up2 = pygame.K_w
Down2 = pygame.K_s

def DrawPlayer(Ppos):
    pygame.draw.rect(screen,WHITE,(Ppos,PSize))

def MovePlayer(Ppos,Up,Down):
    if key[Down]: 
        Ppos[1] += 3
    if key[Up]: 
        Ppos[1] -= 3
    if Ppos[1] <0:
        Ppos[1] = 1
    if Ppos[1] > 450:
        Ppos[1] = 449

class Ball:
    def __init__(self):
        self.speedX = -4
        self.speedY = 0
        self.HasLost = False
        self.Bpos = [350,300]
        self.RandomCollision = [1,2,3]
        self.Positive = False
        self.Negative = False

    def Checkhit(self,P1pos,P2pos):
        self.Hitbox1 = pygame.draw.rect(screen,WHITE,(P1pos,PSize))
        self.Hitbox2 = pygame.draw.rect(screen,WHITE,(P2pos,PSize))
        self.HitboxB = pygame.draw.circle(screen,RED,self.Bpos,15)
        self.Hitbox1part1 = pygame.draw.rect(screen,WHITE,(P1pos,[30,75]))
        self.Hitbox1part2 = pygame.draw.rect(screen,WHITE,([P1pos[0],P1pos[1]+75],(30,75)))
        self.Hitbox2part1 = pygame.draw.rect(screen,WHITE,(P2pos,[30,75]))
        self.Hitbox2part2 = pygame.draw.rect(screen,WHITE,([P2pos[0],P2pos[1]+75],(30,75)))

        if self.Hitbox1part1.colliderect(self.HitboxB) or self.Hitbox2part1.colliderect(self.HitboxB):
            self.speedY = random.choice(self.RandomCollision)
            self.Positive = True
            self.Negative = False
        if self.Hitbox1part2.colliderect(self.HitboxB) or self.Hitbox2part2.colliderect(self.HitboxB):
            self.Negative = True
            self.Positive = False

        if self.HitboxB.colliderect(self.Hitbox1) or self.HitboxB.colliderect(self.Hitbox2):
            self.speedX = self.speedX/-1
            self.speedX = int(self.speedX)

        if self.Bpos[1] < 5:
            self.Positive = True
            self.Negative = False
        if self.Bpos[1] > 595:
            self.Negative = True
            self.Positive = False

    def DrawBall(self):
        if self.speedX == 4:
            self.Bpos[0] += 4
        if self.speedX == -4:
            self.Bpos[0] -= 4
        if self.Positive:
            self.Negative = False
            self.Bpos[1] += random.choice(self.RandomCollision)
        if self.Negative:
            self.Positive = False
            self.Bpos[1] -= random.choice(self.RandomCollision)
        pygame.draw.circle(screen,RED,self.Bpos,15)

    def Lost(self):
        if self.Bpos[0] < 0:
            self.HasLost = True
            self.LostHit = "The Left Player"
        if self.Bpos[0] > 700:
            self.HasLost = True
            self.LostHit = "The Right Player"

        if self.HasLost == True:
            text_surface = font.render((self.LostHit+" lost"), False, (255, 255, 255))
            screen.blit(text_surface, dest=(175,250))
            

B = Ball()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    screen.fill((BLACK))
    
    MovePlayer(P1pos,Up2,Down2)
    MovePlayer(P2pos,Up1,Down1)
    B.DrawBall()
    B.Checkhit(P1pos,P2pos)
    B.Lost()
    DrawPlayer(P1pos)
    DrawPlayer(P2pos)

    pygame.display.update()
    clock.tick(60)
