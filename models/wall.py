from models.actor import ActorBase

class Wall(ActorBase):

	color = (0, 128, 255)

	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.width = w
		self.height = h