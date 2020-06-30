import pygame
from constants.side import Side

class ActorBase:

	x = 0
	y = 0
	vx = 0
	vy = 0

	width = 0
	height = 0
	color = (0, 0, 0)


	def draw(self, screen):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))


	def update(self):
		self.x += self.vx
		self.y += self.vy


	def detectCollision(self, other):

		self_bottom = self.y + self.height;
		other_bottom = other.y + other.height;
		self_right = self.x + self.width;
		other_right = other.x + other.width;

		if self_right >= other.x and self.x <= other_right and self_bottom >= other.y and self.y <= other_bottom:

			# calculate relative velocities
			dv_x = self.vx - other.vx
			dv_y = self.vy - other.vy

			offset_x = float("inf")
			offset_y = float("inf")

			side = Side.NONE

			# self right and other left will collide
			if dv_x > 0:
				offset_x = self_right - other.x
				side |= Side.RIGHT
			
			# self left and other right will collide
			if dv_x < 0:
				offset_x = self.x - other_right
				side |= Side.LEFT

			# self bottom and other top will collide
			if dv_y > 0:
				offset_y = self_bottom - other.y
				side |= Side.BOTTOM
			
			# self top and other bottom will collide
			if dv_y < 0:
				offset_y = self.y - other_bottom
				side |= Side.TOP

			# move self back to moment at collision
			# self.x -= offset_x if offset_x != float("inf") else 0
			# self.y -= offset_y if offset_y != float("inf") else 0

			# time since collision
			dt_x = abs(dv_x / offset_x) if offset_x != 0 else 0
			dt_y = abs(dv_y / offset_y) if offset_y != 0 else 0

			# hit at the same time, like on a corner
			if dt_x == dt_y:
				return side # both
			
			# the longer time since collision means that side hit first
			if dt_x > dt_y:
				return side & ~(Side.TOP | Side.BOTTOM) # left or right
			
			else:
				return side & ~(Side.LEFT | Side.RIGHT) # top or bottom

		return Side.NONE # no collision

	
	def bounce(self, side):
		if side & Side.RIGHT or side & Side.LEFT:
			self.vx *= -1
		if side & Side.TOP or side & Side.BOTTOM:
			self.vy *= -1
