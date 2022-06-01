import pygame
import time

def main():
	pygame.init()
	tela = pygame.display.set_mode([1280,720])
	pygame.display.set_caption('Teste de Jogo Python')
	relogio = pygame.time.Clock()

	cor_branca = (255, 255 ,255)
	cor_preta = (0, 0, 0)
	cor_vermelha = (255, 0, 0)
	cor_verde = (0, 255, 0)
	cor_azul = (0, 0, 255)

	sup1 = pygame.Surface((100,100))
	sup1.fill(cor_vermelha)

	sup2 = pygame.Surface((100,100))
	sup2.fill(cor_azul)

	sair = False

	while sair != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sair = True

		relogio.tick(12)
		tela.fill(cor_preta)
		tela.blit(sup1, [150,150])
		tela.blit(sup2, [50,50])

		pygame.display.update()


	pygame.quit()	
main()
