import pygame

class ActorInterface:

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
		return (self.x + self.width) >= other.x and self.x <= (other.x + other.width) and (self.y + self.height) >= other.y and self.y <= (other.y + other.height)