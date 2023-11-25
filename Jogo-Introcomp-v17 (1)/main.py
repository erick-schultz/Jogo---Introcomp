# Importando bibliotecas publicas
import pygame
import time
import random
import sys

from personagem import Personagem
from window import Window
from jogador import Jogador
from inimigo import Inimigo
from batalha import Batalha

# Inicializa pygame
pygame.init()
#pygame.mixer.init()


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
  img_fundo = pygame.image.load("./fundoCerto.png")  #carregando imagem de fundo para a variavel
  img_fundo = pygame.transform.scale(img_fundo,(win.returnWinSize()))  #para redimensionar o tamanho da imagem q ficou mto grande

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
  jogador1 = Jogador("Caçador", 180, 200, 30, 70, 8, 1, "P1hunter.png")
  jogador2 = Jogador("Paladino", 100, 280, 70, 30, 7, 2, "P2Paladino.png")
  jogador3 = Jogador("Bispo", 170, 380, 50, 50, 6, 3, "P3Shadow.png")

  jogadores = pygame.sprite.Group()
  jogadores.add(jogador1, jogador2, jogador3)

  # Cria inimigos (genéricos), no futuro, add como grupo do sprite
  inimigo1 = Inimigo("Necromante", 780, 190, 30, 70, 8, "I2.png", (880, -120))
  inimigo2 = Inimigo("Esqueleto", 700, 320, 70, 30, 7, "I1.png", (790, 120))

  # cria grupo de inimigos
  inimigos = pygame.sprite.Group()
  inimigos.add(inimigo1, inimigo2)

  # cria batalha 
  batalha = Batalha(jogadores, inimigos, janela)

  # cria ordem da batalha (função de batalha)
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

  trocar_personagem = False #para condição de avançar para proximo personagem
  exibir_tela = False
  # Cria variavel de tickrate
  clock = pygame.time.Clock()

  # Estado do jogo
  running = True

  # conta personagens que ja jogaramn para assim passar turno
  contPersonagem = 0
  
  rodada = 0
  #variavel para checar se todos os personagens de uma esuipe morreram
  acabou = batalha.acabou()

  #configura e toca música
  #pygame.mixer.music.load("musica.mp3")
  #pygame.mixer.music.play(-1, 0.0)

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
      

    # Atualiza o tickrate#seta ataque X defesa
      pygame.draw.polygon(janela, (255, 0, 0), [(seta_x, personagem_y + 70), (seta_x + 20, personagem_y + 60), (seta_x, personagem_y + 50)]) 

      if ataque_selecionado:
    # Desenhe a seta de seleção de alvo
        pygame.draw.polygon(janela, (255, 0, 0), [(seta2_x + 20, inimigo_y + 70), (seta2_x, inimigo_y + 60), (seta2_x + 20, inimigo_y + 50)])
      
      for event in pygame.event.get():
        # Fecha jogo
        if (event.type == pygame.QUIT):
            running = False

        # loop para realizar a batalha
        if not acabou:
          if personagem_atual.pontos_vida > 0:
            if personagem_atual in jogadores: 
              if event.type == pygame.KEYDOWN:
                # confirma acao do jogador
                if event.key == pygame.K_z:
                  if acao_atual == 1: #defesa
                    personagem_atual.acao = acao_atual
                    batalha.realizar_acao_do_jogador(personagem_atual)
                    print(f"{personagem_atual.nome} defendeu.")
                    trocar_personagem = True
                    # personagem_atual_index = (personagem_atual_index + 1) % len(ordem_jogada)
                    # personagem_atual = ordem_jogada[personagem_atual_index]
                  elif acao_atual == 0: #ataque
                    personagem_atual.acao = acao_atual
                    print(f"{personagem_atual.nome} atacou.")
                    ataque_selecionado = True 
                    print("Escolha um alvo para o ataque.")

                # se ataque selecionado, X serve para voltar e escolher a ação novamente
                elif event.key == pygame.K_x:
                  if ataque_selecionado:
                      ataque_selecionado = False  # Cancela a seleção de alvo
                      print("Seleção de alvo cancelada. Escolha entre Ataque e Defesa novamente.")

                # escolhe ação do jogador
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
            
            
                # Usa as teclas de seta para alternar entre os inimigos
                elif ataque_selecionado:
                  for inimigo in inimigos:
                    if inimigo.morreu() and not batalha.acabou():
                      inimigos.remove(inimigo)
                      fix_pos_x = inimigo_atual.seta_pos[0]
                      fix_pos_y = inimigo_atual.seta_pos[1]
                      

                  if len(inimigos) == 1:
                    print(inimigos.sprites())
                    inimigo_atual = inimigos.sprites()[0]
                    inimigo_atual.acao = acao_atual
                    batalha.alvo = inimigo_atual
                    seta2_x = fix_pos_x
                    inimigo_y = fix_pos_y
                    
                    if event.key == pygame.K_SPACE:
                      batalha.realizar_acao_do_jogador(personagem_atual)
                      print(f"{personagem_atual.nome} atacou {inimigo_atual.nome}.")
                      ataque_selecionado = False
                      trocar_personagem = True
                      
                       
                    
                  elif len(inimigos) > 1:
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
            
                  # Usa a tecla de espaço para confirmar o inimigo selecionado
                    if event.key == pygame.K_SPACE:
                      if inimigo_index == 0:
                        inimigo_atual = inimigos.sprites()[inimigo_index]
                        batalha.alvo = inimigo_atual
                        print(f"Você selecionou o {inimigo_atual.nome}")
                        batalha.realizar_acao_do_jogador(personagem_atual)
                      elif inimigo_index == 1:
                        inimigo_atual = inimigos.sprites()[inimigo_index]
                        batalha.alvo = inimigo_atual
                        print(f"Você selecionou o {inimigo_atual.nome}")
                        batalha.realizar_acao_do_jogador(personagem_atual)
                      ataque_selecionado = False
                      trocar_personagem = True
  
              ordem_jogada = batalha.ordem_acoes()
              exibir_tela = trocar_personagem

            # turno do inimigo
            elif personagem_atual in inimigos:
              if personagem_atual.pontos_vida > 0:
                personagem_atual.escolher_acao()
                batalha.realizar_acao_do_inimigo(personagem_atual)
                trocar_personagem = True
            
  
            acabou = batalha.acabou()

            # tempo da mensgaem na tela
            tempo_mensagem = 2000 #2000ms = 2 segundos

            # escrev mensagem na tela por um certo periodo de tempo
            if exibir_tela:
              exibir_tela = False
              
              # Obtém o tempo inicial
              tempo_inicial = pygame.time.get_ticks()
              tempo_atual = pygame.time.get_ticks()
              
              #inimigo escolhido como alvo na tela
              if (personagem_atual in jogadores):
                if ((personagem_atual.acao == 0) and (inimigo_atual is not None)):
                  while tempo_atual - tempo_inicial < tempo_mensagem:
                    tempo_atual = pygame.time.get_ticks()
                    janela.blit(fonte.render(f"{personagem_atual.nome} atacou {inimigo_atual.nome}", True, (0, 0, 0)), (40, 620))
                    pygame.display.flip()  # Atualiza a tela
                    
                else:
                  while tempo_atual - tempo_inicial < tempo_mensagem:
                    tempo_atual = pygame.time.get_ticks()
                    janela.blit(fonte.render(f"{personagem_atual.nome} defendeu", True, (0, 0, 0)), (40, 620))
                    pygame.display.flip()  # Atualiza a tela

                janela.blit(img_quad, rect_quad)  # mostrar o quadrado na tela
                janela.blit(img_quad2, rect_quad2)  # mostrar o quadrado na tela      
              
              else:
                tempo_inicial = pygame.time.get_ticks()
                tempo_atual = pygame.time.get_ticks()
                if(personagem_atual.acao == 0):
                  while tempo_atual - tempo_inicial < tempo_mensagem:
                    tempo_atual = pygame.time.get_ticks()
                    janela.blit(fonte.render(f"{personagem_atual.nome} atacou {batalha.alvo_inimigo.nome}", True, (0, 0, 0)), (40, 620))
                    pygame.display.flip()  # Atualiza a tela
                else:
                  while tempo_atual - tempo_inicial < tempo_mensagem:
                    tempo_atual = pygame.time.get_ticks()
                    janela.blit(fonte.render(f"{personagem_atual.nome} defendeu", True, (0, 0, 0)), (40, 620))
                    pygame.display.flip()  # Atualiza a tela

            # passa turno
            if trocar_personagem:  
              # Avance para o próximo personagem na ordem de jogada
              contPersonagem += 1
              personagem_atual_index += 1

              if personagem_atual_index == len(ordem_jogada):
                personagem_atual_index = 0
                
                
              personagem_atual = ordem_jogada[personagem_atual_index]
              exibir_tela = trocar_personagem
              trocar_personagem = False

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
                  
              #print(contPersonagem, len(ordem_jogada), personagem_atual_index)
                    
            # passa rodada
            if contPersonagem == len(ordem_jogada):
              contPersonagem = 0
              personagem_atual_index = 0
              rodada += 1
              for personagem in batalha.defendeu:
                personagem.defesa /= 2
                batalha.defendeu = []

          #encerra jogo se algum dos times estiver sem integrantes
        else:
          janela.blit(fonte.render(f"{batalha.finalizar_batalha()}", True, (0, 0, 0)), (50, 540))
          running = False
          #volta para menu principal (update futuro)
         
      
      
    
      
      # No canto inferior direito, nomes e pontos de vida dos personagens
      n = 1
      for jogador in jogadores.sprites():
        if jogador.pontos_vida < 0:
          jogador.pontos_vida = 0
        janela.blit(fonte.render(f"{n}. {jogador.nome} ({jogador.pontos_vida:.2f}/{jogador.vida_total})", True, (0, 0, 0)),(620, 540 + n * 30))
        n += 1

      # No canto inferior esquerdo, nome do personagem atual
      janela.blit(fonte.render(f"Sua vez {personagem_atual.nome}", True, (0, 0, 0)), (50, 540))

      # tela.blit(fonte.render(f"Ação: {acoes_disponiveis[acao_atual]}", True, (0, 0, 0)), (50, 570))
      # escreve as opcoes de atacar ou defender no canto inferior esquerdo
      janela.blit(fonte.render(f"Atacar            Defender", True, (0, 0, 0)), (80, 580))

      
    
      # Atualiza tela
      pygame.display.flip()

      # Define tickrate
      clock.tick(FPS)

      # Fim da batalha
  batalha.finalizar_batalha()

  pygame.quit()

if __name__ == "__main__":
  main()