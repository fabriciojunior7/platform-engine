import pygame
import cores

class Entidade(pygame.sprite.Sprite):
	def __init__(self, x, y, largura, altura, cor):	
		pygame.sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura
		self.cor = cor
		#self.imagem = pygame.image.load(imagem)
		#self.imagem = pygame.transform.scale(self.imagem, (self.x, self.y))
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		self.topo = pygame.Rect(self.x, self.y, self.largura, self.altura)???


	def desenhaEntidade(self, tela):
		pygame.draw.rect(tela, self.cor, self.corpo)
		#pygame.transform.scale(self.imagem, (int(self.x), int(self.y)))
		#tela.blit(self.imagem, (self.x, self.y))






