import os
import sys

def resource_path(filename):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, filename)


#WELCOME TO THE CODE OF SANDWITCH GAME CODE
# for hacktime project thing 
# took  me 10 hours  im so bad im new to codeing 
#use arrow keys to selecte charater then press enter 
# Aovid the bomb 
# try to get apples and burgers apples get you more food
# ithink the money object works but i really dont know its really rare
#First couple lines is to make game start 
import pygame
import random 
pygame.init()
start_time = pygame.time.get_ticks()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game")
Bomb = pygame.image.load(resource_path("Bomb.png"))
money = pygame.image.load(resource_path("money.png"))
player = pygame.image.load(resource_path("player.png"))
Burger = pygame.image.load(resource_path("Burger.png"))
lose = pygame.image.load(resource_path("lose.png"))
backround = pygame.image.load(resource_path("Backround.gif"))
player2 = pygame.image.load(resource_path("player2.png"))
player3 = pygame.image.load(resource_path("player3.png"))
apple = pygame.image.load(resource_path("apple.png"))
x = 250
y = 450
x2 = random.randint(0, 750)
y2 = -50
x3 = random.randint(0, 750)
y3 = -45
x4 =random.randint(0, 750)
y4 = -50
x5 = random.randint(0, 750)
y5 = -1000
score = 0
font = pygame.font.Font(None, 40)
# vaiables 
characters = [player, player2, player3]
selected = 0
selecting = True 
applespeed = 0.20
speed = 1
Bombspeed = 0.25
Burgerspeed = 0.12
moneyspeed = 0.75
player_rect = pygame.Rect(x, y, 200, 200)
Burger_rect = pygame.Rect(x2, y2, 50, 50)
Bomb_rect = pygame.Rect(x3, y3, 50, 50)
apple_rect = pygame.Rect(x4, y4, 50,50)

score_text = font.render("Score: " + str(score), True, (255, 255, 255))
player = pygame.transform.scale(player, (200,200))
Burger = pygame.transform.scale(Burger, (50,50))
Bomb = pygame.transform.scale(Bomb, (50,50))
lose = pygame.transform.scale(lose,(800,600))
backround = pygame.transform.scale(backround, (800,600))
apple = pygame.transform.scale(apple, (50,50))
money = pygame.transform.scale(money, (50,50))
level = 1
lives = 3

game_over = False

running = True
clock = pygame.time.Clock()

while selecting:
        screen.fill((0, 0, 0,))
        screen.blit(characters[selected], (300,300))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 3

                if event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 3

                if event.key == pygame.K_RETURN:
                    player = characters[selected]
                    selecting = False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    if score >= 1000 and level == 1:
        level = 2
        Burgerspeed = 0.5
        applespeed = 0.7
        Bombspeed = 1
        moenyspeed = 1

    if player_rect.colliderect(Burger_rect):
        y = 450
    
    if game_over: 
        screen.blit(lose, (0, 0))
    else:
     screen.blit(backround, (0, 0))
     #screen.fill((34, 56, 200))
     screen.blit(player, (x,y)) 
     screen.blit(Burger, (x2,y2))  
     screen.blit(Bomb,(x3,y3))
     screen.blit(apple, (x4, y4))
     screen.blit(score_text, (10,10))
     lives_text = font.render("lives:" + str(lives), True, (255, 255, 255))
     screen.blit(lives_text, (10, 50))
     score_text = font.render("Score: " + str(score), True, (255, 255, 255))

    pygame.display.flip()    
    keys = pygame.key.get_pressed()
    player_rect = pygame.Rect(x, y, 200, 200)
    Burger_rect = pygame.Rect(x2, y2, 50, 50)
    Bomb_rect = pygame.Rect(x3, y3, 50, 50)
    apple_rect = pygame.Rect(x4, y4, 50, 50)
    money_rect = pygame.Rect(x5, y5, 50, 50)
    
    if player_rect.colliderect(Burger_rect):
        score += 100
        y2 = -50
        x2 = random.randint(0, 750)
    if player_rect.colliderect(apple_rect):
        score += 150
        y4 = -50
        x4 = random.randint(0, 750)
       
    if player_rect.colliderect(Bomb_rect):
        lives -=  1
        y3 = -50
        x3 = random.randint(0, 750)

        if lives <= 0:
            game_over = True
        
    if y4 > 600:
        y4 = -50
        x4 = random.randint(0, 750)    
    
    if y3 > 600:
        y3 = -50
        x3 = random.randint(0, 750)
    if y2 > 600:
        pygame.display.set_caption("YOU LOSE")
    if y5 > 600:
        y5 = -1000
        x5 = random.randint(0, 750)
    if random.randint(1, 1000) == 1 and y5 < -500:
        y5 = -50
        x5 = random.randint(0,750)
    
    if keys [pygame.K_LEFT]:
     x -= speed
    
    if keys [pygame.K_RIGHT]:
        x += speed
    y2 += Burgerspeed
    x  = max(-80, min(x, 849 - 200))
    y3 += Bombspeed
    y4 += applespeed
    y5 += moneyspeed
    
pygame.display.flip()  
pygame.quit()