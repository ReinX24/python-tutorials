import pygame

from button import Button


class EasyButton(Button):
	"""This is a subclass of the button class."""

	def __init__(self, ai_game, msg):
		"""Initialize easy button attributes"""
		super().__init__(ai_game, msg)
		self.rect.bottomleft = self.screen_rect.bottomleft
		self._prep_msg(msg)

	def _prep_msg(self, msg):
		"""Turn msg into a rendered image and center text on the button."""
		super()._prep_msg(msg)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center
