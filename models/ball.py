from models.actor import ActorBase

class Ball(ActorBase):

	width = 15
	height = 15
	color = (255, 128, 0)

	def __init__(self, x, y, vx, vy):
		self.x = x
		self.y = y
		self.vx = vx
		self.vy = vy
