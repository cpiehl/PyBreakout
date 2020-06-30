
import pygame
from models.ball import Ball
from models.block import Block
from models.paddle import Paddle
from models.wall import Wall
from constants.side import Side

pygame.init()

WIDTH = 800
HEIGHT = 600
WALL_WIDTH = 20
PADDING = 10

BALL_VELOCITY = 0.2

BLOCK_COLS = 5
BLOCK_ROWS = 10

walls = {
	'top': Wall(0, 0, WIDTH, WALL_WIDTH),
	'left': Wall(0, 0, WALL_WIDTH, HEIGHT),
	'bottom': Wall(0, HEIGHT - WALL_WIDTH, WIDTH, WALL_WIDTH),
}

lose_wall = Wall(WIDTH, 0, WALL_WIDTH, HEIGHT) # behind the paddle, hit this wall to lose

paddle = Paddle(WIDTH - WALL_WIDTH, HEIGHT / 2)

ball = Ball(WIDTH / 2, HEIGHT / 2, BALL_VELOCITY, 0)

blocks = []
block_width = 20
block_height = (HEIGHT - (2 * WALL_WIDTH) - PADDING) / BLOCK_ROWS
for nx in range(BLOCK_COLS):
	for ny in range(BLOCK_ROWS):
		x = WALL_WIDTH + PADDING + (nx * (block_width + PADDING))
		y = WALL_WIDTH + PADDING + (ny * block_height)
		blocks.append(Block(x, y, block_width, block_height - PADDING))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False

while not done:
	# event handling
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	# keyboard handling
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP] and paddle.detectCollision(walls['top']) == Side.NONE:
		paddle.y -= 0.1
	if pressed[pygame.K_DOWN] and paddle.detectCollision(walls['bottom']) == Side.NONE:
		paddle.y += 0.1

	# physics stuff
	ball.update()
	paddle.update()

	# wall collisions
	for wall in walls:
		side = ball.detectCollision(walls[wall])
		if side != Side.NONE:
			ball.bounce(side)

	# paddle collision
	side = ball.detectCollision(paddle)
	if side != Side.NONE:
		ball.bounce(side)
		offset_normalized = (ball.y - paddle.y - (paddle.height / 2)) / (paddle.height / 2) # -1 to 1, offset from center of paddle
		ball.vy = offset_normalized * BALL_VELOCITY # steer ball by hitting off-center

	# block collisions
	for i in range(len(blocks) - 1, -1, -1):
		block = blocks[i]
		side = block.detectCollision(ball)
		if side != Side.NONE:
			ball.bounce(side)
			# block.alive = False
			del blocks[i]

	# lose condition
	if ball.detectCollision(lose_wall) != Side.NONE:
		# reset ball position
		ball.x = WIDTH / 2
		ball.y = HEIGHT / 2
		ball.vx = BALL_VELOCITY
		ball.vy = 0

	# win condition
	if len(blocks) == 0:
		print("win yey")

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
