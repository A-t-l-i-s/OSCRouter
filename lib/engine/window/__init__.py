from engine.require import *





__all__ = ("Window",)





class Window(RFT_Object, QMainWindow):
	def __init__(self):
		super().__init__()
		self.lift("Window")

		# ~~~~~~~ Variables ~~~~~~
		# ~~~~~~~~~~~~~~~~~~~~~~~~



