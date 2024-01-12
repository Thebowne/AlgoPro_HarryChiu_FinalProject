import pygame


# Update and display players, objects, etc.
def update_screen(screen, settings, background, mob, player, start_time):
    screen.blit(background.ground_surface, (0, 50))
    screen.blit(background.sky_surface, (0, -170))
    display_score(screen, start_time)
    pygame.draw.rect(screen, (173, 216, 230), background.text_rect, 20)
    pygame.draw.ellipse(screen, 'Gold', pygame.Rect(100, 80, 100, 100))
    screen.blit(background.text_surface, background.text_rect)
    screen.blit(mob.cactus_surface, mob.cactus_rect)
    screen.blit(player.player_surface, player.player_rect)


# Function to get tick and displays the score or how long has the player has not collided
def display_score(screen, start_time):
    current_time = pygame.time.get_ticks() // 1000 - start_time
    scoreboard = pygame.font.Font(None, 36)
    scoreboard_surf = scoreboard.render(f' Score: {current_time}', False, (64, 64, 64))
    scoreboard_rect = scoreboard_surf.get_rect(center=(200, 200))
    screen.blit(scoreboard_surf, scoreboard_rect)
