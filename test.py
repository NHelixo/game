import pygame

pygame.init()
clock = pygame.time.Clock()

# Параметри екрана
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Колір
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

wall_1 = pygame.Surface((60, 60))
wall_1.fill(RED)

wall_2 = pygame.Surface((60, 60))
wall_2.fill(BLUE)

map_1 = [
    pygame.Rect(300, 300, 60, 60),
    pygame.Rect(360, 300, 60, 60),
    pygame.Rect(500, 500, 60, 60)
]

player = pygame.Rect(100, 100, 50, 50)
player_speed = 5

running = True
while running:
    screen.fill(WHITE)

    # Обробка подій
    keys = pygame.key.get_pressed()
    new_x, new_y = player.x, player.y

    if keys[pygame.K_w]:  # Вгору
        new_y -= player_speed
    if keys[pygame.K_s]:  # Вниз
        new_y += player_speed
    if keys[pygame.K_a]:  # Вліво
        new_x -= player_speed
    if keys[pygame.K_d]:  # Вправо
        new_x += player_speed

    # Тимчасовий новий прямокутник
    new_rect = pygame.Rect(new_x, new_y, player.width, player.height)

    # Перевірка колізій
    if not any(new_rect.colliderect(block) for block in map_1):
        player.x, player.y = new_x, new_y  # Дозволяємо рух

    # Малюємо блоки
    for block in map_1:
        pygame.draw.rect(screen, RED, block)

    # Малюємо гравця
    pygame.draw.rect(screen, BLUE, player)

    pygame.display.flip()

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()