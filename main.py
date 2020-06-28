
import pygame
from models.ball import Ball
from models.block import Block
from models.paddle import Paddle
from models.wall import Wall

pygame.init()

WIDTH = 800
HEIGHT = 600
WALL_WIDTH = 20
PADDING = 10

walls = {
	'top': Wall(0, 0, WIDTH, WALL_WIDTH),
	'left': Wall(0, 0, WALL_WIDTH, HEIGHT),
	'bottom': Wall(0, HEIGHT - WALL_WIDTH, WIDTH, WALL_WIDTH),
	'right': Wall(WIDTH, 0, WALL_WIDTH, HEIGHT), # behind the paddle, hit this wall to lose
}

paddle = Paddle(WIDTH - WALL_WIDTH, HEIGHT / 2)

ball = Ball(WIDTH / 2, HEIGHT / 2, -0.1, -0.1)
blocks = []
for n in range(4): # 0, 1, 2, 3
	blocks.append(Block(WALL_WIDTH + PADDING, WALL_WIDTH + PADDING + (n * (PADDING + Block.height))))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False

while not done:
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# keyboard handling
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP] and not paddle.detectCollision(walls['top']):
		paddle.y -= 0.1
	if pressed[pygame.K_DOWN] and not paddle.detectCollision(walls['bottom']):
		paddle.y += 0.1

	# physics stuff
	ball.update()
	paddle.update()

	# top and bottom wall collision
	if ball.detectCollision(walls['top']) or ball.detectCollision(walls['bottom']):
		ball.vy *= -1
	# left wall collision
	if ball.detectCollision(walls['left']):
		ball.vx *= -1

	# paddle collision
	if ball.detectCollision(paddle):
		ball.vx *= -1

	# block collisions
	# for block in blocks:
	# 	if block.alive:
	# 		collideX = (block.x + block.WIDTH) >= ball.x and block.x <= (ball.x + ball.SIZE)
	# 		collideY = (block.y + block.HEIGHT) >= ball.y and block.y <= (ball.y + ball.SIZE)

	# 			block.alive = False

	# lose condition
	if ball.detectCollision(walls['right']):
		# reset ball position
		ball.x = WIDTH / 2
		ball.y = HEIGHT / 2
		ball.vx = -0.1
		ball.vy = -0.1

	# clear screen
	screen.fill((0, 0, 0))
    
	# draw walls
	for side in walls:
		walls[side].draw(screen)

	# draw paddle
	paddle.draw(screen)

	# draw ball
	ball.draw(screen)

	# draw blocks
	for block in blocks:
		block.draw(screen)
	
	pygame.display.flip()
