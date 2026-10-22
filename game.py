#REMINDERS 
# the game is like going to be snadwitches falling from sky and player has to get them.
# find sandwitch sprite 
# fix color and postions of the player 
# make the player move.
# Make a screen for charater selction 
# change backround 

#First couple lines is to make game start 
import pygame
import random 
pygame.init()
start_time = pygame.time.get_ticks()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game")

#the x is for palyer same for y and x2 and y2 is for burger 
Bomb = pygame.image.load("Bomb.png")
player = pygame.image.load("player.png")
Burger = pygame.image.load("Burger.png")
x = 250
y = 450
x2 = random.randint(0, 750)
y2 = -50
x3 = random.randint(0, 750)
y3 = -45
speed = 1
Bombspeed = 0.25
Burgerspeed = 0.12
player_rect = pygame.Rect(x, y, 200, 200)
Burger_rect = pygame.Rect(x2, y2, 50, 50)
Bomb_rect = pygame.Rect(x3, y3, 50, 50)


#find buger png 



player = pygame.transform.scale(player, (200,200))
Burger = pygame.transform.scale(Burger, (50,50))
Bomb = pygame.transform.scale(Bomb, (50,50))
#rember to remove backround from charter 

running = True
clock = pygame.time.Clock()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              running = False
    if player_rect.colliderect(Burger_rect):
        y = 450
    

    screen.fill((34, 56, 200))
    screen.blit(player, (x,y)) 
    screen.blit(Burger, (x2,y2))  
    screen.blit(Bomb,(x3,y3))
    pygame.display.flip()    
    keys = pygame.key.get_pressed()
   
    player_rect = pygame.Rect(x, y, 200, 200)
    Burger_rect = pygame.Rect(x2, y2, 50, 50)
    Bomb_rect = pygame.Rect(x3, y3, 50, 50)
    
    if player_rect.colliderect(Burger_rect):
        y2 = -50
        x2 = random.randint(0, 750)
       
    if player_rect.colliderect(Bomb_rect):
        y3 = -45
        x3 = random.randint(0, 750)
        pygame.display.set_caption("YOU LOSE")
    if y3 > 600:
        y3 = -50
        x3 = random.randint(0, 750)
    if y2 > 600:
        pygame.display.set_caption("YOU LOSE")





    
    if keys [pygame.K_LEFT]:

     x -= speed
    
    if keys [pygame.K_RIGHT]:
        x += speed
    y2 += Burgerspeed
    x  = max(-80, min(x, 849 - 200))
    y3 += Bombspeed



pygame.quit()

