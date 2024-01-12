import pygame
from settings import Settings
from mob import Mob
from background import Background
from player import Player
import gamefunctions as gf


# Initialize pygame
pygame.init()

# Setting up the information needed
settings = Settings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
pygame.display.set_caption("Chicken Adventure")
pygame.display.set_icon(settings.icon)
clock = pygame.time.Clock()

game_active = True
start_time = 0

background = Background(screen, settings)
mob = Mob(screen, settings)
player = Player(screen, settings)

# While True loop where the game runs
while True:
    # Check for events happening inside the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player.player_rect.bottom == 570:
                if player.player_rect.collidepoint(event.pos):
                    player.player_gravity = -20
                    print('click')
            # Reacts to a key being pressed
            if event.type == pygame.KEYDOWN:
                print('keydown')
                # Jumping mechanics
                if event.key == pygame.K_SPACE and player.player_rect.bottom == 570:
                    player.player_gravity = -20
                    print('jump')
        # Start the scoreboard
        elif not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_active = True
            mob.cactus_rect.x = mob.cactus_x
            start_time = pygame.time.get_ticks() // 1000

    # Drawing player, cactus and game physics
    if game_active:
        player.gravity()
        gf.update_screen(screen, settings, background, mob, player, start_time)
        mob.enemy_spawn(settings)

    # Show screen when Game is done
    elif not game_active:
        screen.fill('pink')
        screen.blit(background.go_text_surface, background.go_text_rect)
        screen.blit(background.go_text_surf_1, background.go_text_rect_1)
        screen.blit(player.player_surface_1, player.player_rect_1)

    if player.player_rect.colliderect(mob.cactus_rect):
        print('collide')
        game_active = False

    pygame.display.update()
    clock.tick(60)
