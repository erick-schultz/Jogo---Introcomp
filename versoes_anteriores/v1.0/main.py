# Importando bibliotecas publicas
import pygame
import random
import sys

from personagem import Personagem
from window import Window
from jogador import Jogador
from inimigo import Inimigo
from batalha import Batalha

# Inicializa pygame
pygame.init()


# Cria função principal
def main():
  # Configura tela
  win = Window(768, 1024)  # definindo altura e largura
  janela = pygame.display.set_mode(win.returnWinSize())  # abre janela
  pygame.display.set_caption("Jogo Batalha")  # nome do jogo
  janela.fill(win.returnColor())  # cor da janela

  # Variável constante
  FPS = 60

  # Cores
  branco = (255, 255, 255)
  preto = (0, 0, 0)

  # Fonte
  fonte = pygame.font.Font('freesansbold.ttf', 32) 

  #----------- imagens e menu (integração) --------------
  #imagem de fundo
  img_fundo = pygame.image.load(
      "fundoCerto.png")  #carregando imagem de fundo para a variavel
  img_fundo = pygame.transform.scale(
      img_fundo,
      (win.returnWinSize()))  #para redimensionar o tamanho da imagem q ficou mto grande

  #imagem quadrado1
  img_quad = pygame.image.load("combat_menu_1.png")  #carregando imagem quadrado

  rect_quad = img_quad.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  
  #definindo posição do retangulo
  rect_quad.x = 15  # Posição X inicial
  rect_quad.y = 530  # Posição Y para ocupar a parte inferior da tela

  #imagem quadrado2
  img_quad2 = pygame.image.load("combat_menu_2.png")  #carregando imagem quadrado
  rect_quad2 = img_quad2.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  
  # #definindo posição do retangulo
  rect_quad2.x = 605  # Posição X inicial
  rect_quad2.y = 530  # Posição Y para ocupar a parte inferior da tela

  #pos seta menu
  seta_x = 50
  personagem_y = 535

  #pos seta inimigos
  seta2_x = 880
  inimigo_y = 190

  personagem_selecionado = None
  acao_selecionada = None

  opcao_atual = ""

  acoes_disponiveis = ["Atacar", "Defender"]
  acao_atual = 0  # Índice da ação atualmente selecionada (0 para Atacar, 1 para Defender)
  
  # Cria jogadores (genéricos)
  jogador1 = Jogador("Alpha", 180, 200, 30, 70, 8, 1, "P1hunter.png")
  jogador2 = Jogador("Beta", 100, 280, 70, 30, 7, 2, "P2Paladino.png")
  jogador3 = Jogador("Gamma", 170, 380, 50, 50, 6, 3, "P3Shadow.png")

  jogadores = pygame.sprite.Group()
  jogadores.add(jogador1, jogador2, jogador3)

  # Cria inimigos (genéricos), no futuro, add como grupo do sprite
  inimigo1 = Inimigo("Duda", 780, 190, 30, 70, 8, "I1.png")
  inimigo2 = Inimigo("Dudo", 700, 320, 70, 30, 7, "I2.png")

  inimigos = pygame.sprite.Group()
  inimigos.add(inimigo1, inimigo2)

  batalha = Batalha(jogadores, inimigos, janela)

  ordem_jogada = batalha.ordem_acoes()

  personagem_atual = ordem_jogada[0] #pega o primeiro personagem da lista

  personagem_atual_index = ordem_jogada.index(personagem_atual) #pega o index do personagem atual

  #limita a seta para não sair da tela (menu)
  limite_esquerdo = 50
  limite_direito = 270 - 20 

  #limita a seta para não sair da tela (inimigos)
  limite_up = 190
  limite_down = 310 

  # Crie uma variável para rastrear o inimigo selecionado
  inimigo_atual = None
  inimigo_index = 0  # Índice do inimigo atualmente selecionado (0 para inimigo_1, 1 para inimigo_2)

  ataque_selecionado = False #para condição de escolher alvo

  trocar_personagem = False

  # Cria variavel de tickrate
  clock = pygame.time.Clock()

  # Estado do jogo
  running = True

  # Cria laço principal
  while running:
      janela.blit(img_fundo, (0, 0))  #mostrar a imagem de fundo na tela

      janela.blit(img_quad, rect_quad)  # mostrar o quadrado na tela
      janela.blit(img_quad2, rect_quad2)  # mostrar o quadrado na tela

      #personagens na tela
      janela.blit(jogador1.imagem, (jogador1.x, jogador1.y))
      janela.blit(jogador2.imagem, (jogador2.x, jogador2.y))
      janela.blit(jogador3.imagem, (jogador3.x, jogador3.y))

      #inimigos na tela
      janela.blit(inimigo1.imagem, (inimigo1.x, inimigo1.y))
      janela.blit(inimigo2.imagem, (inimigo2.x, inimigo2.y))
      # Fecha jogo

    # Atualiza o tickrate#seta ataque X defesa
      pygame.draw.polygon(janela, (255, 0, 0), [(seta_x, personagem_y + 70), (seta_x + 20, personagem_y + 60), (seta_x, personagem_y + 50)]) 

      if ataque_selecionado:
    # Desenhe a seta de seleção de alvo
        pygame.draw.polygon(janela, (255, 0, 0), [(seta2_x + 20, inimigo_y + 70), (seta2_x, inimigo_y + 60), (seta2_x + 20, inimigo_y + 50)])
      
      for event in pygame.event.get():
          if (event.type == pygame.QUIT):
              running = False

          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
              if acao_atual == 1:
                print(f"{personagem_atual.nome} defendeu.")
                personagem_atual_index = (personagem_atual_index + 1) % len(ordem_jogada)
                personagem_atual = ordem_jogada[personagem_atual_index]
              elif acao_atual == 0:
                print(f"{personagem_atual.nome} atacou.")
                ataque_selecionado = True 
                print("Escolha um alvo para o ataque.")
        
            elif event.key == pygame.K_x:
              if ataque_selecionado:
                  ataque_selecionado = False  # Cancela a seleção de alvo
                  print("Seleção de alvo cancelada. Escolha entre Ataque e Defesa novamente.")
        
            elif event.key == pygame.K_LEFT:
              if not ataque_selecionado: 
                seta_x -= 200  # Move a seta para a esquerda
                acao_atual = 0  # Seleciona "Ataque"
                if seta_x < limite_esquerdo: #limita a seta
                  seta_x = limite_esquerdo
            elif event.key == pygame.K_RIGHT:
              if not ataque_selecionado: 
                seta_x += 200 # Move a seta para a direita
                acao_atual = 1  # Seleciona "Defesa"
                if seta_x > limite_direito: #limita a seta
                  seta_x = limite_direito
        
        
            # Use as teclas de seta para alternar entre os inimigos
            elif ataque_selecionado:
              if event.key == pygame.K_UP:
                seta2_x = 880
                inimigo_y -= 120
                inimigo_index = 0 
                if inimigo_y < limite_up: #limita a seta
                  inimigo_y = limite_up
              elif event.key == pygame.K_DOWN:
                seta2_x = 790
                inimigo_y += 120
                inimigo_index = 1
                if inimigo_y > limite_down: #limita a seta
                  inimigo_y = limite_down
        
              # Use a tecla de espaço para confirmar o inimigo selecionado
              elif event.key == pygame.K_SPACE:
                if inimigo_index == 0:
                  inimigo_atual = inimigos.sprites()[inimigo_index]
                  print(f"Você selecionou o {inimigo_atual.nome}")
                elif inimigo_index == 1:
                  inimigo_atual = inimigos.sprites()[inimigo_index]
                  print(f"Você selecionou o {inimigo_atual.nome}")
                ataque_selecionado = False
                trocar_personagem = True
        
        
        
        
                if trocar_personagem:  
                  # Avance para o próximo personagem na ordem de jogada
                  personagem_atual_index = (personagem_atual_index + 1) % len(ordem_jogada)
                  personagem_atual = ordem_jogada[personagem_atual_index]

      


    
    

      # No canto inferior direito, nomes e pontos de vida dos personagens
      n = 1
      for jogador in jogadores.sprites():
          janela.blit(fonte.render(f"{n}. {jogador.nome} ({jogador.pontos_vida}/valor fixo)", True, (0, 0, 0)),(620, 540 + n * 30))
          n += 1

      # No canto inferior esquerdo, nome do personagem atual
      janela.blit(fonte.render(f"Sua vez {personagem_atual.nome}", True, (0, 0, 0)), (50, 540))

      # tela.blit(fonte.render(f"Ação: {acoes_disponiveis[acao_atual]}", True, (0, 0, 0)), (50, 570))
      janela.blit(fonte.render(f"Atacar            Defender", True, (0, 0, 0)), (80, 580))

      if trocar_personagem:
        #inimigo escolhido como alvo na tela
        janela.blit(fonte.render(f"Você atacou {inimigo_atual.nome}", True, (0, 0, 0)), (40, 620))
        trocar_personagem = False
              
      
      

      

      

      # Atualiza tela
      pygame.display.update()

      # Define tickrate
      clock.tick(FPS)

      # Passar para o próximo turno
      batalha.passar_turno()

      # Fim da batalha
  batalha.finalizar_batalha()

  pygame.quit()

if __name__ == "__main__":
  main()