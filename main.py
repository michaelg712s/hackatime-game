import asyncio
import pygame
import random

pygame.init()

async def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)

    # Load images
    Bomb = pygame.image.load("Bomb.png")
    money = pygame.image.load("money.png")
    Burger = pygame.image.load("Burger.png")
    lose = pygame.image.load("lose.png")
    background = pygame.image.load("Backround.gif")
    apple = pygame.image.load("apple.png")

    characters = [
        pygame.image.load("player.png"),
        pygame.image.load("player2.png"),
        pygame.image.load("player3.png")
    ]

    # Resize images
    characters = [
        pygame.transform.scale(img, (200, 200))
        for img in characters
    ]
    Bomb = pygame.transform.scale(Bomb, (50, 50))
    Burger = pygame.transform.scale(Burger, (50, 50))
    apple = pygame.transform.scale(apple, (50, 50))
    money = pygame.transform.scale(money, (50, 50))
    lose = pygame.transform.scale(lose, (800, 600))
    background = pygame.transform.scale(background, (800, 600))

    # Character selection
    selected = 0
    selecting = True
    running = True

    while selecting and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                selecting = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    selected = (selected - 1) % 3
                elif event.key == pygame.K_RIGHT:
                    selected = (selected + 1) % 3
                elif event.key == pygame.K_RETURN:
                    selecting = False

        if selecting:
            screen.fill((0, 0, 0))
            screen.blit(characters[selected], (300, 250))
            screen.blit(
                font.render("Choose character: LEFT / RIGHT", True,
                            (255, 255, 255)),
                (100, 150)
            )
            screen.blit(
                font.render("Press ENTER to start", True,
                            (255, 255, 255)),
                (220, 480)
            )
            pygame.display.flip()

        await asyncio.sleep(0)

    if running:
        player = characters[selected]

        x, y = 250, 400
        burger_x, burger_y = random.randint(0, 750), -50
        bomb_x, bomb_y = random.randint(0, 750), -50
        apple_x, apple_y = random.randint(0, 750), -50

        score = 0
        lives = 3
        game_over = False
        level = 1

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN and game_over:
                    if event.key == pygame.K_r:
                        score = 0
                        lives = 3
                        game_over = False
                        burger_y = bomb_y = apple_y = -50

            keys = pygame.key.get_pressed()

            if not game_over:
                if keys[pygame.K_LEFT]:
                    x -= 5
                if keys[pygame.K_RIGHT]:
                    x += 5

                x = max(-80, min(x, 680))

                burger_y += 2 if level == 1 else 4
                bomb_y += 2 if level == 1 else 4
                apple_y += 2 if level == 1 else 3

                player_rect = pygame.Rect(x, y, 200, 200)
                burger_rect = pygame.Rect(burger_x, burger_y, 50, 50)
                bomb_rect = pygame.Rect(bomb_x, bomb_y, 50, 50)
                apple_rect = pygame.Rect(apple_x, apple_y, 50, 50)

                if player_rect.colliderect(burger_rect):
                    score += 100
                    burger_y = -50
                    burger_x = random.randint(0, 750)

                if player_rect.colliderect(apple_rect):
                    score += 150
                    apple_y = -50
                    apple_x = random.randint(0, 750)

                if player_rect.colliderect(bomb_rect):
                    lives -= 1
                    bomb_y = -50
                    bomb_x = random.randint(0, 750)

                    if lives <= 0:
                        game_over = True

                if burger_y > 600:
                    burger_y = -50
                    burger_x = random.randint(0, 750)

                if apple_y > 600:
                    apple_y = -50
                    apple_x = random.randint(0, 750)

                if bomb_y > 600:
                    bomb_y = -50
                    bomb_x = random.randint(0, 750)

                if score >= 1000:
                    level = 2

            screen.blit(background, (0, 0))

            if game_over:
                screen.blit(lose, (0, 0))
                screen.blit(
                    font.render("Press R to restart", True,
                                (255, 255, 255)),
                    (250, 520)
                )
            else:
                screen.blit(player, (x, y))
                screen.blit(Burger, (burger_x, burger_y))
                screen.blit(Bomb, (bomb_x, bomb_y))
                screen.blit(apple, (apple_x, apple_y))
                screen.blit(
                    font.render(f"Score: {score}", True,
                                (255, 255, 255)),
                    (10, 10)
                )
                screen.blit(
                    font.render(f"Lives: {lives}", True,
                                (255, 255, 255)),
                    (10, 50)
                )

            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())