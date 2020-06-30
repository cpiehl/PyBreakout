from models.actor import ActorBase

class Block(ActorBase):

	color = (255, 255, 0)

	def __init__(self, x, y, w=15, h=50, alive=True):
		self.x = x
		self.y = y
		self.width = w
		self.height = h
		self.alive = alive

	def draw(self, screen):
		if self.alive:
			super().draw(screen)

	def detectCollision(self, other):
		return self.alive and super().detectCollision(other)