from button import Button


class NormalButton(Button):
	"""Hard button, subclass of Button class."""

	def __init__(self, ai_game, msg):
		"""Initialize easy button attributes"""
		super().__init__(ai_game, msg)
		self.rect.midbottom = self.screen_rect.midbottom
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		super()._prep_msg(msg)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
