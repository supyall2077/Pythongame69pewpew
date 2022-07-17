###--- import ---###
import pygame
import random
import os
pygame.font.init()

###--- Variables ---###
WIDTH, HEIGHT = 900, 600
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 80, 70
ENEMY_WIDTH, ENEMY_HEIGHT = 80, 80
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

FPS = 60
VEL = 8
BULLET_VEL = 12
MAX_BULLETS = 5
MAX_ENEMY = 10
score = 0

SCORE_FONT = pygame.font.SysFont("Pokemon GB.ttf", 100)

BACKGROUND_IMG = pygame.transform.scale(pygame.image.load(os.path.join('gDljmw.jpeg')), (WIDTH, HEIGHT))
SPACESHIP_IMG = pygame.image.load(os.path.join('spaceship_red.png'))
SPACESHIP = pygame.transform.scale(SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
ENEMY = pygame.transform.scale(pygame.image.load(os.path.join('UFO.png')), (ENEMY_WIDTH, ENEMY_HEIGHT))




###--- DEFs ---###
def handle_collision(all_enemies, player_bullets, score):
    for enemy in all_enemies:
        for bullet in player_bullets:
            if enemy.colliderect(bullet):
                all_enemies.remove(enemy)
                player_bullets.remove(bullet)
                score = score + 100
                return score
    return score

def handle_enemy(all_enemies, enemy, MAX_ENEMY):
    # define Enemy #
    while len(all_enemies) < MAX_ENEMY:
        new_enemy = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        new_enemy.x = random.randint(0, WIDTH - ENEMY_WIDTH)
        new_enemy.y = random.randint(0, 400)
        all_enemies.append(new_enemy)




def handle_player_bullet(player_bullets):
    for bullet in player_bullets:
        bullet.y -= BULLET_VEL
        if bullet.y < 0:
            player_bullets.remove(bullet)

def handle_player_movement(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT] and player.x - VEL >= 0: # LEFT
        player.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and player.x + VEL <= WIDTH - SPACESHIP_WIDTH: #RIGHT
        player.x += VEL

def draw(player, player_bullets, all_enemies, score):
    WIN.blit(BACKGROUND_IMG, (0, 0))
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    score_text = SCORE_FONT.render(str(score), 1, (r, g, b))
    WIN.blit(score_text, (WIDTH/2 - 50, HEIGHT - 60))
    WIN.blit(SPACESHIP, (player.x, player.y))

    for enemy in all_enemies:

        WIN.blit(ENEMY, (enemy.x, enemy.y))

    for bullet in player_bullets:
        pygame.draw.rect(WIN, (r, g, b), bullet)


    pygame.display.update()

def main():
    # lists #
    player_bullets = []
    all_enemies = []
    score = 0

    # Objet Controls #
    player = pygame.Rect(WIDTH/2, 530, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    enemy_pos_x = random.randint(0, WIDTH)
    enemy_pos_y = random.randint(0, 400)
    enemy = pygame.Rect(enemy_pos_x, enemy_pos_y, ENEMY_WIDTH, ENEMY_HEIGHT)


    #main wile loop #
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Bullet input #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(player_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(player.x + SPACESHIP_WIDTH // 2, player.y, 10, 30)
                    player_bullets.append(bullet)

        # input #
        keys_pressed = pygame.key.get_pressed()
        handle_player_movement(keys_pressed, player)

        # bullet #

        handle_player_bullet(player_bullets)

        handle_enemy(all_enemies,enemy, MAX_ENEMY)

        score = handle_collision(all_enemies, player_bullets, score)

        draw(player, player_bullets, all_enemies, score)





###--- Main ---###
if __name__ == "__main__":
    main()


a = 3.5