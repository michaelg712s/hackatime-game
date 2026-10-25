#REMINDERS 
# the game is like going to be snadwitches falling from sky and player has to get them.
# find sandwitch sprite 
# fix color and postions of the player 
# make the player move.
# Make a screen for charater selction 
# change backround 
#  make a counter for points 
# make a kitchen backround 

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
lose = pygame.image.load("lose.png")
backround = pygame.image.load("Backround.gif")
player2 = pygame.image.load("player2.png")
player3 = pygame.image.load("player3.png")
#pple = pygame.image.load("apple")

x = 250
y = 450
x2 = random.randint(0, 750)
y2 = -50
x3 = random.randint(0, 750)
y3 = -45
x4 = 400
y4 = 300
score = 0
font = pygame.font.Font(None, 40)
# vaiables 
characters = [player, player2, player3]
selected = 0
selecting = True 
speed1 = 234567
speed = 1
Bombspeed = 0.25
Burgerspeed = 0.12
player_rect = pygame.Rect(x, y, 200, 200)
Burger_rect = pygame.Rect(x2, y2, 50, 50)
Bomb_rect = pygame.Rect(x3, y3, 50, 50)

score_text = font.render("Score: " + str(score), True, (255, 255, 255))
player = pygame.transform.scale(player, (200,200))
Burger = pygame.transform.scale(Burger, (50,50))
Bomb = pygame.transform.scale(Bomb, (50,50))
lose = pygame.transform.scale(lose,(800,600))
backround = pygame.transform.scale(backround, (800,600))


#rember to remove backround from charter 

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
     screen.blit(score_text, (10,10))
     score_text = font.render("Score: " + str(score), True, (255, 255, 255))

    pygame.display.flip()    

    keys = pygame.key.get_pressed()
   
    player_rect = pygame.Rect(x, y, 200, 200)
    Burger_rect = pygame.Rect(x2, y2, 50, 50)
    Bomb_rect = pygame.Rect(x3, y3, 50, 50)
    
    if player_rect.colliderect(Burger_rect):
        score += 100
        y2 = -50
        x2 = random.randint(0, 750)
       
    if player_rect.colliderect(Bomb_rect):
        game_over = True
        
        
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


pygame.display.flip()  
pygame.quit()

