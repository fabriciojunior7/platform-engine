import pygame, random
import cores
import entidades

class Player(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor)
		self.velocidadeX = 0.0
		self.velocidadeXMax = 5.0
		self.velocidadeY = 0.0
		self.velocidadeYMax = 10.0
		self.gravidade = 0.1
		self.colidindo = False
		self.ad = [False, False]

	def atualizarPosicao(self, largura, altura):
		#Eixo X
		if(self.ad[0] == True and self.x > 0):
			self.x -= self.velocidadeXMax
		if(self.ad[1] == True and self.x < (largura - self.largura)):
			self.x += self.velocidadeXMax
		#Eixo Y
		if(self.colidindo == False):
			if(self.velocidadeY < self.velocidadeYMax):
				self.velocidadeY += self.gravidade
			self.y += self.velocidadeY
			self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

	def botaoPressionado(self, key):
		if(key == pygame.K_a):
			self.ad[0] = True
		if(key == pygame.K_d):
			self.ad[1] = True

	def botaoSolto(self, key):
		if(key == pygame.K_a):
			self.ad[0] = False
		if(key == pygame.K_d):
			self.ad[1] = False		
		
	def vibrar(self):
		self.x += random.randint(-1, 1)
		self.y += random.randint(-1, 1)
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)





