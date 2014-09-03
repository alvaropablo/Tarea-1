import math
class circulo():
	_ra=0
	def __init__(self, r):
		self._ra=r
	def darArea(self):
		return math.pi*self._ra
c=circulo(5)
print(c.darArea())