import pygame

pygame.init()

screen_width = 480
screen_height = 640
screenSize = (screen_width, screen_height)
gameScreen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("dltmdgjs rotoRl")

clock = pygame.time.Clock()

background = pygame.image.load("C:/Users/user/Desktop/20111이성민/1/새 폴더/background.png")

character = pygame.image.load("C:/Users/user/Desktop/20111이성민/1/새 폴더/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]    
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_to_x_LEFT=0
character_to_x_RIGHT=0
to_y = 0


running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character_to_x_LEFT -= 5
            elif event.key == pygame.K_d:
                character_to_x_RIGHT += 5
            elif event.key == pygame.K_w:
                to_y -= 5
            elif event.key == pygame.K_s:
                to_y += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                character_to_x_LEFT = 0
            elif event.key == pygame.K_d:
                character_to_x_RIGHT = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                to_y = 0
    character_x_pos += character_to_x_LEFT + character_to_x_RIGHT
    character_y_pos += to_y
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height  

    gameScreen.blit(background, (0,0))
    gameScreen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

            



pygame.quit()
