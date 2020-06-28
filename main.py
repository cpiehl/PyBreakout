
import pygame
from models.Ball import Ball

pygame.init()

WIDTH = 800
HEIGHT = 600
WALL_WIDTH = 20

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
paddle_y = HEIGHT / 2

# ball.SIZE = 15
# ball.x = WIDTH / 2
# ball.y = HEIGHT / 2
# ball.vx = -0.1
# ball.vy = -0.1

ball = Ball(WIDTH / 2, HEIGHT / 2, -0.1, -0.1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False

while not done:
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# keyboard handling
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP] and paddle_y > WALL_WIDTH:
		paddle_y -= 0.1
	if pressed[pygame.K_DOWN] and paddle_y < (HEIGHT - WALL_WIDTH - PADDLE_HEIGHT):
		paddle_y += 0.1

	# physics stuff
	ball.x += ball.vx
	ball.y += ball.vy

	if ball.y <= WALL_WIDTH or ball.y >= (HEIGHT - WALL_WIDTH - ball.BALL_SIZE):
		ball.vy *= -1
	if ball.x <= WALL_WIDTH:
		ball.vx *= -1

	if ball.x >= (WIDTH - PADDLE_WIDTH - ball.BALL_SIZE) and (ball.y + ball.BALL_SIZE) > paddle_y and ball.y < (paddle_y + PADDLE_HEIGHT):
		ball.vx *= -1

	# lose condition
	if ball.x >= (WIDTH - ball.BALL_SIZE):
		# reset ball position
		ball.x = WIDTH / 2
		ball.y = HEIGHT / 2
		ball.vx = -0.1
		ball.vy = -0.1

	# clear screen
	screen.fill((0, 0, 0))
    
	# draw walls
	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, WIDTH, WALL_WIDTH))
	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, 0, WALL_WIDTH, HEIGHT))
	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(0, HEIGHT - WALL_WIDTH, WIDTH, WALL_WIDTH))

	# draw paddle
	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(WIDTH - PADDLE_WIDTH, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

	# draw ball
	pygame.draw.rect(screen, (255, 128, 0), pygame.Rect(ball.x, ball.y, ball.BALL_SIZE, ball.BALL_SIZE))
	
	pygame.display.flip()