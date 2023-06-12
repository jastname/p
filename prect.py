import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screenSize = (screen_width, screen_height)
gameScreen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("창")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/user/Desktop/20111이성민/1/새 폴더/uncolored_peaks.png")

character = pygame.image.load("C:/Users/user/Desktop/20111이성민/1/새 폴더/character.png")

obstacle = pygame.image.load("C:/Users/user/Desktop/20111이성민/1/새 폴더/obstacle.png")

shield = pygame.image.load("C:/Users/user/Desktop/20111이성민/1/새 폴더/2108.w032.n003.65B.p1.65.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]    
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_to_x_LEFT=0
character_to_x_RIGHT=0
to_y = 0

game_font = pygame.font.Font(None, 40)

obstacle_size = obstacle.get_rect().size
obstacle_width = obstacle_size[0]
obstacle_height = obstacle_size[1]
obstacle_x_pos = random.randint(0 ,screen_width-obstacle_width)
obstacle_y_pos = 10
ob_speed = 20

shield_size = shield.get_rect().size
shield_width = shield_size[0]
shield_height = shield_size[1]
shield_x_pos = random.randint(0 ,screen_width-obstacle_width)
shield_y_pos = 10
sh_speed = 10

shield_on = False

start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character_to_x_LEFT -= 8
            elif event.key == pygame.K_d:
                character_to_x_RIGHT += 8
            elif event.key == pygame.K_w:
                to_y -= 8
            elif event.key == pygame.K_s:
                to_y += 8
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                character_to_x_LEFT = 0
            elif event.key == pygame.K_d:
                character_to_x_RIGHT = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0
    character_x_pos += character_to_x_LEFT + character_to_x_RIGHT
    character_y_pos += to_y
    obstacle_y_pos += ob_speed
    shield_y_pos += sh_speed
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height  
    
    if obstacle_y_pos > screen_height:
        obstacle_y_pos = 0
        obstacle_x_pos = random.randint(0, screen_width - obstacle_width)
    if shield_y_pos > screen_height:
        shield_y_pos = 0
        shield_x_pos = random.randint(0, screen_width - shield_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    obstacle_rect = obstacle.get_rect()
    obstacle_rect.left = obstacle_x_pos
    obstacle_rect.top = obstacle_y_pos

    shield_rect = shield.get_rect()
    shield_rect.left = shield_x_pos
    shield_rect.top = shield_y_pos

    if character_rect.colliderect(shield_rect):
        shield_on = True

    if character_rect.colliderect(obstacle_rect):
        if shield_on:
            shield_on = False
            obstacle_x_pos = random.randint(0, screen_width - obstacle_width)
            obstacle_y_pos = 10
            pass
        else:
           running = False
           

    time = game_font.render(str(int((pygame.time.get_ticks() - start_ticks / 1000))),True,(255,0,0))

    gameScreen.blit(background, (0,0))
    gameScreen.blit(obstacle, (obstacle_x_pos, obstacle_y_pos))
    gameScreen.blit(shield, (shield_x_pos, shield_y_pos))
    gameScreen.blit(character, (character_x_pos, character_y_pos))
    gameScreen.blit(time, (0,0))
    
    pygame.display.update()

            



pygame.quit()
