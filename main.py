import pygame
from snake import Snake

pygame.init()

# Screen setup
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Color setup
black = (0, 0, 0)
white = (255, 255, 255)

# Snake setup
snake = Snake()

# Game loop
game_over = False
game_over_start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                snake.reset_snake()
                game_over = False
                game_over_start_time = pygame.time.get_ticks()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.change_direction(pygame.math.Vector2(-10, 0))
    elif keys[pygame.K_RIGHT]:
        snake.change_direction(pygame.math.Vector2(10, 0))
    elif keys[pygame.K_UP]:
        snake.change_direction(pygame.math.Vector2(0, -10))
    elif keys[pygame.K_DOWN]:
        snake.change_direction(pygame.math.Vector2(0, 10))

    screen.fill(black)

    if not game_over:
        snake.update()
        snake.draw(screen)

        font = pygame.font.Font('freesansbold.ttf', 32)
        score_surface = font.render(f'Score: {snake.score}', True, white)
        screen.blit(score_surface, (10, 10))

        # Check game over conditions
        if (
            snake.positions[0].x < 0
            or snake.positions[0].x >= screen_width
            or snake.positions[0].y < 0
            or snake.positions[0].y >= screen_height
            or snake.positions[0] in snake.positions[1:]
        ):
            game_over = True

    if game_over:
        game_over_font = pygame.font.Font('freesansbold.ttf', 64)
        game_over_surface = game_over_font.render('Game Over', True, white)
        screen.blit(game_over_surface, (screen_width // 2 - 200, screen_height // 2 - 50))
        
        score_surface = font.render(f'Your Score: {snake.score}', True, white)
        screen.blit(score_surface, (screen_width // 2 - 100, screen_height // 2 + 50))

        new_game_surface = font.render('Press "Space" for New Game', True, white)
        screen.blit(new_game_surface, (screen_width // 2 - 180, screen_height // 2 + 100))

        # Check if 1 minute has passed
        if pygame.time.get_ticks() - game_over_start_time > 60000:
            game_over = False

    pygame.display.update()
    clock.tick(7)  # Adjust the speed of the snake

pygame.quit()
quit()
