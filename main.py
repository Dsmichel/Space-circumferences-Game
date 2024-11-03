import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Circumferences Game")

background_image = pygame.image.load("image/fondo.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)

# Variables
game_mode = "menu"
score = 0
level = 1
enemies = []
player_pos = (WIDTH // 2, HEIGHT - 50)
player_radius = 20
enemy_speed = 2

def draw_text(text, pos, color=WHITE):
    label = font.render(text, True, color)
    screen.blit(label, pos)

def generate_enemies():
    global enemies, level
    enemies = [{"pos": [random.randint(0, WIDTH - 40), -50]} for _ in range(level * 2)]

def update_enemies():
    for enemy in enemies:
        enemy["pos"][1] += enemy_speed
        if enemy["pos"][1] > HEIGHT:
            enemy["pos"] = [random.randint(0, WIDTH - 40), -50]

def draw_enemies():
    for enemy in enemies:
        pygame.draw.circle(screen, (255, 0, 0), enemy["pos"], player_radius)

def check_collisions(projectiles):
    global score, enemies, game_mode
    player_rect = pygame.Rect(player_pos[0] - player_radius, player_pos[1] - player_radius, player_radius * 2, player_radius * 2)

    for projectile in projectiles[:]:
        projectile_rect = pygame.Rect(projectile["pos"][0], projectile["pos"][1], 5, 10)
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy["pos"][0] - player_radius, enemy["pos"][1] - player_radius, player_radius * 2, player_radius * 2)
            if projectile_rect.colliderect(enemy_rect):
                enemies.remove(enemy)
                projectiles.remove(projectile)
                score += 1
                break

    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy["pos"][0] - player_radius, enemy["pos"][1] - player_radius, player_radius * 2, player_radius * 2)
        if player_rect.colliderect(enemy_rect):
            game_mode = "game_over"
            break

def next_level():
    global game_mode, level, enemy_speed
    level += 1
    enemy_speed += 1
    generate_enemies()
    game_mode = "pause"

# Modes
def menu():
    screen.blit(background_image, (0, 0))
    draw_text("Space Circumferences", (250, 200))
    draw_text("Press SPACE to start", (250, 300))

def game():
    global player_pos
    screen.blit(background_image, (0, 0))
    player_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (0, 255, 0), player_pos, player_radius)
    draw_text(f"Score: {score}", (650, 10))
    draw_text(f"Level: {level}", (650, 40))

def pause():
    screen.blit(background_image, (0, 0))
    draw_text("Level Cleared!", (300, 200))
    draw_text("Press SPACE to continue", (200, 300))

def game_over():
    screen.blit(background_image, (0, 0))
    draw_text("Game Over", (300, 200))
    draw_text(f"Level reached: {level}", (300, 250))
    draw_text(f"Final score: {score}", (300, 300))
    draw_text("Press SPACE to return to the menu", (200, 400))


running = True
projectiles = []
clock = pygame.time.Clock()

while running: # Main Loop
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_mode == "game":
            if event.button == 1:
                projectiles.append({"pos": list(player_pos)})

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if game_mode == "menu":
                game_mode = "game"
                score = 0
                level = 1
                enemy_speed = 2
                generate_enemies()
            elif game_mode == "pause":
                game_mode = "game"
            elif game_mode == "game_over":
                game_mode = "menu"

    if game_mode == "menu":
        menu()
    elif game_mode == "game":
        game()
        update_enemies()
        draw_enemies()
        for projectile in projectiles[:]:
            projectile["pos"][1] -= 5
            pygame.draw.rect(screen, WHITE, (*projectile["pos"], 5, 10))
            if projectile["pos"][1] < 0:
                projectiles.remove(projectile)
        check_collisions(projectiles)
        if not enemies:
            next_level()
    elif game_mode == "pause":
        pause()
    elif game_mode == "game_over":
        game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
