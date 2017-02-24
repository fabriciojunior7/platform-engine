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
		self.colisaoDireita = False
		self.colisaoEsquerda = False

	def atualizarPosicao(self, largura, altura):
		#Eixo X
		if(self.ad[0] == True and self.x > 0):
			self.x -= self.velocidadeXMax
		if(self.ad[1] == True and self.x < (largura - self.largura) and self.colisaoDireita == False):
			self.x += self.velocidadeXMax
		#Eixo Y
		if(self.colidindo == False):
			if(self.velocidadeY < self.velocidadeYMax):
				self.velocidadeY += self.gravidade
			self.y += self.velocidadeY
		else:
			self.velocidadeY = 0

		#AtualizarPosisoes
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		self.topo = pygame.Rect(self.x + 2, (self.y - self.alturaTB), self.larguraTB, self.alturaTB)
		self.base = pygame.Rect(self.x + 2, (self.y + self.altura), self.larguraTB, self.alturaTB)
		self.direita = pygame.Rect((self.x - self.larguraDE), self.y + 2, self.larguraDE, self.alturaDE)
		self.esquerda = pygame.Rect((self.x + self.largura), self.y + 2, self.larguraDE, self.alturaDE)

	def botaoPressionado(self, key):
		if(key == pygame.K_a):
			self.ad[0] = True
		if(key == pygame.K_d):
			self.ad[1] = True
		if(key == pygame.K_w):
			self.colidindo = False
			self.velocidadeY = -5

	def botaoSolto(self, key):
		if(key == pygame.K_a):
			self.ad[0] = False
		if(key == pygame.K_d):
			self.ad[1] = False	

	def colidiuTopo(self, y):
		if(self.velocidadeY < 0):
			self.velocidadeY = 0

	def colidiuBase(self, y):
		if(self.velocidadeY < 0):
			self.colidindo = False
		else:
			self.colidindo = True
			self.y = y - self.altura - 1

	def colidiuDireita(self, x):
		self.x = x - self.largura
		self.colidiuDireita = True
		

		
	def vibrar(self):
		self.x += random.randint(-1, 1)
		self.y += random.randint(-1, 1)
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)






