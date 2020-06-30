from enum import IntFlag

class Side(IntFlag):
	NONE   = 0
	TOP    = 1 << 0
	BOTTOM = 1 << 1
	LEFT   = 1 << 2
	RIGHT  = 1 << 3
