import pygame
from pygame.sprite import Sprite
class Heart(Sprite):
	def __init__(self,ai_settings,screen):
		super(Heart,self).__init__()
		self.screen = screen
		self.ai_settings=ai_settings
		self.image = pygame.image.load('F://python_work//alien_invasion//images//heart.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect=screen.get_rect()
		
