import pygame

class Drawable:
	
	x = 0
	y = 0
	width = 0
	height = 0
	color = (0, 0, 0)


	def draw(self, screen):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
