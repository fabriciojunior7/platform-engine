import pygame
import cores
import entidades

class Parede(entidades.Entidade):
	def __init__(self, x, y, largura, altura, cor):
		entidades.Entidade.__init__(self, x, y, largura, altura, cor)