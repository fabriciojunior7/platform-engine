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
		#self.larguraTB = self.largura - 4
		self.larguraTB = self.largura
		self.alturaTB = 10
		self.larguraDE = 5
		#self.alturaDE = self.altura - 4
		self.alturaDE = self.altura
		self.separacao = 15
		#self.imagem = pygame.image.load(imagem)
		#self.imagem = pygame.transform.scale(self.imagem, (self.x, self.y))
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		self.topo = pygame.Rect(self.x, (self.y - self.alturaTB), self.larguraTB, self.alturaTB)
		self.base = pygame.Rect(self.x, (self.y + self.altura), self.larguraTB, self.alturaTB)
		self.direita = pygame.Rect((self.x - self.larguraDE), self.y, self.larguraDE, self.alturaDE)
		self.esquerda = pygame.Rect((self.x + self.largura), self.y, self.larguraDE, self.alturaDE)


	def desenhaEntidade(self, tela):
		pygame.draw.rect(tela, self.cor, self.corpo)
		pygame.draw.rect(tela, cores.verde, self.topo)
		pygame.draw.rect(tela, cores.verde, self.base)
		pygame.draw.rect(tela, cores.verde, self.direita)
		pygame.draw.rect(tela, cores.verde, self.esquerda)
		#pygame.transform.scale(self.imagem, (int(self.x), int(self.y)))
		#tela.blit(self.imagem, (self.x, self.y))






