import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game clock
clock = pygame.time.Clock()

# Set the font for the score
font = pygame.font.SysFont("Arial", 50)

# Set the ball properties
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5 * random.choice([1, -1])
ball_speed_y = 5 * random.choice([1, -1])

# Set the paddle properties
paddle_width = 15
paddle_height = 100
paddle_speed = 5
left_paddle_x = 50
left_paddle_y = screen_height // 2 - paddle_height // 2
right_paddle_x = screen_width - 50 - paddle_width
right_paddle_y = screen_height // 2 - paddle_height // 2

# Set the initial score
left_score = 0
right_score = 0

# Set the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s]:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP]:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collision with the top and bottom walls
    if ball_y - ball_radius < 0 or ball_y + ball_radius > screen_height:
        ball_speed_y *= -1

    # Check for collision with the left paddle
    if ball_x - ball_radius < left_paddle_x + paddle_width and left_paddle_y < ball_y < left_paddle_y + paddle_height:
        ball_speed_x *= -1

    # Check for collision with the right paddle
    if ball_x + ball_radius > right_paddle_x and right_paddle_y < ball_y < right_paddle_y + paddle_height:
        ball_speed_x *= -1

    # Check for scoring
    if ball_x - ball_radius < 0:
        right_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])
    if ball_x + ball_radius > screen_width:
        left_score += 1
        ball_x, ball_y = screen_width // 2, screen_height // 2
        ball_speed_x *= random.choice([1, -1])
        ball_speed_y *= random.choice([1, -1])

    # Draw the game elements
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen