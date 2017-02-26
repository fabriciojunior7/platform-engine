import pygame, sys
import cores
import players, paredes

def game():
		
	pygame.init()
	informacaoTela = pygame.display.Info()
	largura = informacaoTela.current_w
	altura = informacaoTela.current_h
	tela = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)
	relogio = pygame.time.Clock()
	frames = 60

	#Objetos
	p1 = players.Player(350, 400, 40, 40, cores.vermelho)
	walls = []
	numWalls = 1
	for w in range(numWalls):
		walls.append(paredes.Parede(10, 600, 100, 160, cores.preto))
		walls.append(paredes.Parede(200, 600, 100, 160, cores.preto))
		walls.append(paredes.Parede(500, 600, 100, 160, cores.preto))
		walls.append(paredes.Parede(700, 600, 100, 160, cores.preto))
		walls.append(paredes.Parede(850, 600, 100, 160, cores.preto))

	def desenhar():
		#Rodar
		pygame.display.update()
		relogio.tick(frames)
		if(p1.y > (altura - p1.altura)):
			if(p1.velocidadeY > 0):
				p1.velocidadeY = 0
				p1.y = (altura - p1.altura)

		for w in walls:
			if(p1.base.colliderect(w.topo)):
				p1.colidiuBase(w.y)
				break
			else:
				p1.colidindo = False

		for w in walls:
			if(p1.topo.colliderect(w.base)):
				p1.colidiuTopo(w.y + w.altura + w.alturaTB)

			if(p1.direita.colliderect(w.esquerda)):
				p1.colidiuDireita(w.x, w.largura)
			elif(p1.esquerda.colliderect(w.direita)):
				p1.colidiuEsquerda(w.x)

		#Desenhar
		tela.fill(cores.branco)
		p1.atualizarPosicao(largura, altura)
		for w in walls:
			w.desenhaEntidade(tela)
		p1.desenhaEntidade(tela)



	while(True):
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				pygame.quit()
				sys.exit()

			if(event.type == pygame.KEYDOWN):
				p1.botaoPressionado(event.key)
				if(event.key == pygame.K_5):
					game()
				if(event.key == pygame.K_ESCAPE):
					pygame.quit()
					sys.exit()
			if(event.type == pygame.KEYUP):
				p1.botaoSolto(event.key)

		#Rodar
		desenhar()














game()


