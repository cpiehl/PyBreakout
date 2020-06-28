from models.actor import ActorInterface

class Block(ActorInterface):

	width = 15
	height = 50
	color = (255, 255, 0)

	def __init__(self, x, y, alive=True):
		self.x = x
		self.y = y
		self.alive = alive

	def draw(self, screen):
		if self.alive:
			super().draw(screen)