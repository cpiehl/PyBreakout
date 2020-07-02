from models.base.actor import Actor

class Paddle(Actor):

	width = 20
	height = 100
	color = (0, 255, 255)


	def __init__(self, x, y):
		self.x = x
		self.y = y
