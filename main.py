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

# inicializa musica
audio_disponivel = True
try:
  pygame.mixer.init()
except pygame.error:
  audio_disponivel = False

#variaveis globais (cores) - imutáveis 
#feito para nao ficar repetindo codigo
BRANCO = (255,255,255)
PRETO = (0,0,0)
VERMELHO = (255,0,0)
VERDE = (0,255,0)

# Posição inicial do personagem
turbox = -100 #posição x
turboy = 50  # posição vertical y do personagem 


#--------------easter egg-------------------------
def desenhar_turbo(janela,x, y): #desenha na tela
  # Carrega a imagem do personagem
  turbo = pygame.image.load("Turbo.webp")
  turbo = pygame.transform.scale(turbo, (100, 100))  # Ajusta o tamanho da imagem
  janela.blit(turbo, (x, y))

def mover_turbo(): #move o personagem
  velocidade_personagem = 35
  global turbox  # Permitir a modificação da variável global
  turbox += velocidade_personagem

#------------------------------------------------------

def escrever(janela, text, pos, cor) -> None: # escreve na janela
  fonte = pygame.font.Font('freesansbold.ttf', 32)
  texto = fonte.render(text, True, cor)
  texto_rect_center = texto.get_rect(center=(janela.get_width() / 2, janela.get_height() / 2)) #centro da tela
  
  #posicionar texto no centro
  if pos == "centro":
    janela.blit(texto, texto_rect_center)

  else:
    #posicionar texto em qualquer outro lugar da tela
    janela.blit(texto, pos)

def desenhar_personagens(personagens, janela) -> None: #desenha os personagens na ordem em que foram adicionados
  pos_personagens = [(180, 200), (100, 280), (170, 380)]
  for i, personagem in enumerate(personagens):
    janela.blit(personagem.imagem, pos_personagens[i])

def menu_inicial(janela, img_fundo, personagens_selecionados) -> None:
  #cria jogadores com a classe jogador
  jogador1 = Jogador("Paladino", 100, 280, 35, 70, 3, "P2Paladino.png")
  jogador2 = Jogador("Ladino", 0, 0, 80, 20, 9, "P5Ladino.png")
  jogador3 = Jogador("Mago", 0, 0, 60, 50, 6, "P4Mago.png")
  jogador4 = Jogador("Caçador", 180, 200, 70, 30, 5, "P1Hunter.png")
  jogador5 = Jogador("Clérigo", 170, 380, 55, 40, 6, "P3Clerigo.png")

  #cria lista com todos os jogadores na ordem do menu
  jogs = [jogador1, jogador2, jogador3, jogador4, jogador5]

  #variavel que recebe o número maximo de jogadores por batalha
  max_jogadores_selecionados = 3

  #criando seta do menu
  seta_menu_x = 210 #posição inicial
  seta_menu_y = 190 #posição inicial
  
  #limita seta menu
  menu_lim_esquerda = 210
  menu_lim_direita = 780
  menu_lim_up = 190
  menu_lim_down = 460
  
  # -------------------criando menu inicial------------------------------ 
  menu_q1 = pygame.image.load("menuPaladino.jpeg") #primeiro quadrado-personagem
  rect_menu1 = menu_q1.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  rect_menu1.x = 150  # Posição X inicial
  rect_menu1.y = 230  # Posição Y para ocupar a parte inferior da tela
  menu_q1 = pygame.transform.scale_by(menu_q1, 0.15)

  menu_q2 = pygame.image.load("menuLadino.jpeg") #segundo quadrado-personagem
  rect_menu2 = menu_q2.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  rect_menu2.x = 435  # Posição X inicial
  rect_menu2.y = 230  # Posição Y para ocupar a parte inferior da tela
  menu_q2 = pygame.transform.scale_by(menu_q2, 0.15)

  menu_q3 = pygame.image.load("menuMago.jpeg") #terceiro quadrado-personagem
  rect_menu3 = menu_q3.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  rect_menu3.x = 720  # Posição X inicial
  rect_menu3.y = 230  # Posição Y para ocupar a parte inferior da tela
  menu_q3 = pygame.transform.scale_by(menu_q3, 0.15)

  menu_q4 = pygame.image.load("menuCacador.jpeg") #quarto quadrado-personagem
  rect_menu4 = menu_q4.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  rect_menu4.x = 290  # Posição X inicial
  rect_menu4.y = 500  # Posição Y para ocupar a parte inferior da tela
  menu_q4 = pygame.transform.scale_by(menu_q4, 0.15)

  menu_q5 = pygame.image.load("menuClerigo.jpeg") #quinto quadrado-personagem
  rect_menu5 = menu_q5.get_rect()  #criando um objeto retangulo do tamanho do quadrado
  rect_menu5.x = 580  # Posição X inicial
  rect_menu5.y = 500  # Posição Y para ocupar a parte inferior da tela
  menu_q5 = pygame.transform.scale_by(menu_q5, 0.15)

  index = 0 #posição do personagem no menu no formatro da lista
  escolhendo = True #variavel de controle do loop do menu
  clock = pygame.time.Clock()

  # -------------------rodando menu inicial------------------------------ 
  
  while escolhendo:
    #desenhando fundo
    janela.blit(img_fundo, (0, 0))

    #desenhando personagens no menu
    janela.blit(menu_q1, rect_menu1)
    escrever(janela, "Paladino", (160,420), BRANCO)
    janela.blit(menu_q2, rect_menu2)
    escrever(janela, "Ladino", (460,420), BRANCO)
    janela.blit(menu_q3, rect_menu3)
    escrever(janela, "Mago" , (760,420), BRANCO)
    janela.blit(menu_q4, rect_menu4)
    escrever(janela, "Caçador", (300,690), BRANCO)
    janela.blit(menu_q5, rect_menu5)
    escrever(janela, "Clérigo", (610,690), BRANCO)
    
  
    for event in pygame.event.get():
      # Fecha jogo
      if (event.type == pygame.QUIT):
        return False
      
      elif event.type == pygame.KEYDOWN:
        #tecla 'Z' apertada para confirmar escolha do personagem
        if event.key == pygame.K_z:
          personagem_selecionado = jogs[index]

          #verifica se o personagem escolhido ja foi selecionado
          if (personagem_selecionado not in personagens_selecionados):
              personagens_selecionados.add(personagem_selecionado)
              #acaba o looping quando o numero de jogadores que se pode escolher for o máx
              if len(personagens_selecionados.sprites()) == max_jogadores_selecionados:
                escolhendo = False
                break

        #seta para cima 
        elif event.key == pygame.K_UP:
            seta_menu_y -= 270
            seta_menu_x = 210
            menu_lim_direita = 780 #ajusta o limite quando subir
            menu_lim_esquerda = 210
            index = 0
            if seta_menu_y < menu_lim_up:
              #limita a seta
              seta_menu_y = menu_lim_up
              index = 0 #limita o index
        #seta para baixo   
        elif event.key == pygame.K_DOWN:
            seta_menu_y += 270
            seta_menu_x = 350
            menu_lim_direita = 635 #ajusta o limite quando descer
            menu_lim_esquerda = 350
            index = 3
            if seta_menu_y > menu_lim_down: #limita a seta
                seta_menu_y = menu_lim_down
                index = 3 #limita o index
        #seta para esquerda
        elif event.key == pygame.K_LEFT:
            seta_menu_x -= 285
            if seta_menu_x < menu_lim_esquerda: #limita a seta
                seta_menu_x = menu_lim_esquerda
            else:
                index -= 1 #limita o index
        #seta para direita
        elif event.key == pygame.K_RIGHT:
            seta_menu_x += 285
            if seta_menu_x > menu_lim_direita: #limita a seta
              seta_menu_x = menu_lim_direita
            else:
              index += 1 #limita o index

    #desenha e atualiza a seta
    desenhar_seta(janela, "vertical", seta_menu_x, seta_menu_y, False)
    pygame.display.update()
    clock.tick(60)

  return True

def desenhar_seta(janela, direcao, x, y, inv) -> None:
  # -------------------criando setas ------------------------------
  
  # seta na horiznontal apontando para direita
  if (direcao == "horizontal" and not inv):
    pygame.draw.polygon(janela, (255, 0, 0), [(x, y + 70), (x + 20, y + 60), (x, y + 50)])

  #seta na horizontal apontando para a esquerda
  elif (direcao == "horizontal" and inv):
    pygame.draw.polygon(janela, (255, 0, 0), [(x + 20, y + 70), (x, y + 60), (x + 20, y + 50)])
  
  #seta na vertical apontando para baixo
  elif (direcao == "vertical" and not inv):
    pygame.draw.polygon(janela, (255, 0, 0), [(x, y), (x + 20, y + 30), (x + 20 * 2, y)])
      
def exibir_tela_final(janela, batalha) -> None:
  #varivael de controle do texto de vitória
  acabou_jogo = True
  clock = pygame.time.Clock()

  #define como central a posição do texto final
  pos_texto_final = "centro"

  # Defina a posição inicial da imagem
  posicao = (200, 10)
  # Defina a transparência inicial da imagem
  transparencia = 0
  
  #easter egg 
  dark_souls = pygame.image.load("you_died_ds.png")
  dark_souls = pygame.transform.scale(dark_souls, (600, 600))

  #salva texto da tela final
  resultado = batalha.finalizar_batalha()
  if resultado is None:
    return
  texto_final, condicao_vitoria_derrota = resultado
  
  # exibir na tela até usuário sair do jogo
  while acabou_jogo:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    
    #se venceu a batalha
    if condicao_vitoria_derrota == "venceu":
      #preenche a tela com a cor preta
      janela.fill(PRETO)

      #escreve na tela que o jogador ganhou na cor verde
      escrever(janela, texto_final, pos_texto_final, VERDE)

      pygame.display.flip()  # Atualiza a tela

      #espera 10 segundos para desligar o jogo
      tempo_inicial = pygame.time.get_ticks()
      while pygame.time.get_ticks() - tempo_inicial < 10000:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            return
        clock.tick(60)
      acabou_jogo = False

    #se perdeu a batalha
    elif condicao_vitoria_derrota == "perdeu":  
      janela.fill(PRETO)
      # Aumenta a transparência para fazer a imagem aparecer lentamente
      if transparencia < 255:
          transparencia += 3
        
      # Configura a transparência do easter egg2
      dark_souls.set_alpha(transparencia)
      
      # Desenhe o easter egg2 na tela
      janela.blit(dark_souls, posicao)

      #escreve na tela que o jogador perdeu na cor vermelha
      escrever(janela, texto_final, pos_texto_final, VERMELHO)

      pygame.display.flip()  # Atualiza a tela
      clock.tick(60)

      #espera 4 segundos para desligar o jogo
      if transparencia >= 255:
        tempo_inicial = pygame.time.get_ticks()
        while pygame.time.get_ticks() - tempo_inicial < 4000:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
          clock.tick(60)
        acabou_jogo = False
      

# Cria função principal
def main():
  # Configura tela
  win = Window(768, 1024)  # definindo altura e largura
  janela = pygame.display.set_mode(win.returnWinSize())  # abre janela
  pygame.display.set_caption("Jogo Batalha")  # nome do jogo
  janela.fill(win.returnColor())  # cor da janela

  # Variável constante
  FPS = 60

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

  acao_atual = 0  # Índice da ação atualmente selecionada (0 para Atacar, 1 para Defender)
  
  # variável de escolha de personagem
  jogadores_selecionados = pygame.sprite.Group()

  # Cria inimigos (genéricos), no futuro, add como grupo do sprite
  inimigo1 = Inimigo("Necromante", 780, 190, 30, 70, 7, "I2.png")
  inimigo2 = Inimigo("Esqueleto", 700, 320, 70, 30, 6, "I1.png")

  # cria grupo de inimigos
  inimigos = pygame.sprite.Group()
  inimigos.add(inimigo1, inimigo2)

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

  # Estado do menu
  escolhendo_jogadores = True

  # conta personagens que ja jogaramn para assim passar turno
  contPersonagem = 0
  
  rodada = 0
  
  if escolhendo_jogadores:
    if not menu_inicial(janela, img_fundo, jogadores_selecionados):
      pygame.quit()
      return
    escolhendo_jogadores = False
    
  # cria batalha 
  batalha = Batalha(jogadores_selecionados, inimigos, janela)
  # cria ordem da batalha (função de batalha)
  ordem_jogada = batalha.ordem_acoes()
  personagem_atual = ordem_jogada[0] #pega o primeiro personagem da lista
  
  #variavel para checar se todos os personagens de uma esuipe morreram
  acabou = batalha.acabou()
  
  #configura e toca música
  if audio_disponivel:
    try:
      pygame.mixer.music.load("musica.mp3")
      pygame.mixer.music.play(-1, 0.0)
    except pygame.error:
      pass

  # Easter egg: 10% de chance de passar uma vez na partida
  global turbox
  turbox = -100
  mostrar_turbo = random.random() < 0.10

  # Cria laço principal
  while running:

    #mostrar a imagem de fundo na tela
    janela.blit(img_fundo, (0, 0))
    
    # Desenha e movimenta easter egg na tela (passa uma unica vez)
    if mostrar_turbo:
      desenhar_turbo(janela, turbox, turboy)
      mover_turbo()
      if turbox > 1024:
        mostrar_turbo = False

    #se os tres personagens ja tiverem sido escolhidos, desnha na tela

    janela.blit(img_quad, rect_quad)  # mostrar o quadrado na tela
    janela.blit(img_quad2, rect_quad2)  # mostrar o quadrado na tela

    #personagens na tela
    desenhar_personagens(jogadores_selecionados, janela)

    #inimigos na tela
    janela.blit(inimigo1.imagem, (inimigo1.x, inimigo1.y))
    janela.blit(inimigo2.imagem, (inimigo2.x, inimigo2.y))

    # No canto inferior direito, nomes e pontos de vida dos personagens
    n = 1
    for jogador in jogadores_selecionados.sprites():
      if jogador.pontos_vida < 0:
        jogador.pontos_vida = 0
      escrever(janela, f"{n}. {jogador.nome} ({jogador.pontos_vida:.2f}/{jogador.vida_total})", (620, 540 + n * 30), PRETO)
      n += 1

    # No canto inferior esquerdo, nome do personagem atual
    escrever(janela, f"Vez de {personagem_atual.nome}!", (50, 540), PRETO)

    if personagem_atual in jogadores_selecionados:
      # escreve as opcoes de atacar ou defender no canto inferior esquerdo
      escrever(janela, f"Atacar            Defender", (80, 580), PRETO)
      # seta ataque X defesa
      desenhar_seta(janela, "horizontal", seta_x, personagem_y, False)
    
    if ataque_selecionado:
      for inimigo in list(inimigos):
        if inimigo.morreu() and not batalha.acabou():
          inimigos.remove(inimigo)
      if len(inimigos) == 1:
        inimigo_vivo = inimigos.sprites()[0]
        seta2_x = inimigo_vivo.x + 90
        inimigo_y = inimigo_vivo.y
      # Desenhe a seta de seleção de alvo
      desenhar_seta(janela, "horizontal", seta2_x, inimigo_y, True)

    # Atualiza tela
    pygame.display.flip()
      
    for event in pygame.event.get():
      # Fecha jogo
      if (event.type == pygame.QUIT):
        running = False
        break

      # loop para realizar a batalha (entrada do jogador)
      if not acabou and personagem_atual.pontos_vida > 0 and personagem_atual in jogadores_selecionados:
        if event.type == pygame.KEYDOWN:
          # confirma acao do jogador
          if event.key == pygame.K_z:
            if acao_atual == 1: #defesa
              personagem_atual.acao = acao_atual
              batalha.realizar_acao_do_jogador(personagem_atual)
              trocar_personagem = True
              exibir_tela = True
              break
              
            elif acao_atual == 0: #ataque
              personagem_atual.acao = acao_atual
              ataque_selecionado = True 

            # se ataque selecionado, X serve para voltar e escolher a ação novamente
          elif event.key == pygame.K_x:
            if ataque_selecionado:
              ataque_selecionado = False  # Cancela a seleção de alvo

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
            for inimigo in list(inimigos):
              if inimigo.morreu() and not batalha.acabou():
                inimigos.remove(inimigo)
            
            # verifica se algum inimigo morreu
            if len(inimigos) == 1:
              #limita seta só ao inimigo que está vivo
              inimigo_atual = inimigos.sprites()[0]
              batalha.alvo = inimigo_atual
              seta2_x = inimigo_atual.x + 90
              inimigo_y = inimigo_atual.y
          
              if event.key == pygame.K_SPACE:
                batalha.realizar_acao_do_jogador(personagem_atual)
                ataque_selecionado = False
                trocar_personagem = True
                exibir_tela = True
                break
                  
                   
            # se nenhum inimigo morreu a seta de seleção funciona   
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
                  batalha.realizar_acao_do_jogador(personagem_atual)
                elif inimigo_index == 1:
                  inimigo_atual = inimigos.sprites()[inimigo_index]
                  batalha.alvo = inimigo_atual
                  batalha.realizar_acao_do_jogador(personagem_atual)
                ataque_selecionado = False
                trocar_personagem = True
                exibir_tela = True
                break

    if not running:
      break

    # turno do inimigo (executa automaticamente sem depender de eventos)
    if not acabou and personagem_atual in inimigos and not trocar_personagem:
      tempo_espera = pygame.time.get_ticks()
      while pygame.time.get_ticks() - tempo_espera < 1000:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
            break
        if not running:
          break
        clock.tick(FPS)

      if running and personagem_atual.pontos_vida > 0:
        personagem_atual.escolher_acao()
        batalha.realizar_acao_do_inimigo(personagem_atual)
        trocar_personagem = True
        exibir_tela = True

    # tempo da mensgaem na tela
    tempo_mensagem = 2000 #2000ms = 2 segundos

    # escreve mensagem de ação na tela por um certo periodo de tempo
    if exibir_tela and running:
      exibir_tela = False

      # redesenha cena com sprites e vidas atualizadas
      janela.blit(img_fundo, (0, 0))
      if mostrar_turbo:
        desenhar_turbo(janela, turbox, turboy)
      janela.blit(img_quad, rect_quad)
      janela.blit(img_quad2, rect_quad2)
      desenhar_personagens(jogadores_selecionados, janela)
      janela.blit(inimigo1.imagem, (inimigo1.x, inimigo1.y))
      janela.blit(inimigo2.imagem, (inimigo2.x, inimigo2.y))

      n = 1
      for jogador in jogadores_selecionados.sprites():
        if jogador.pontos_vida < 0:
          jogador.pontos_vida = 0
        escrever(janela, f"{n}. {jogador.nome} ({jogador.pontos_vida:.2f}/{jogador.vida_total})", (620, 540 + n * 30), PRETO)
        n += 1
      escrever(janela, f"Vez de {personagem_atual.nome}!", (50, 540), PRETO)

      if (personagem_atual in jogadores_selecionados):
        if ((personagem_atual.acao == 0) and (inimigo_atual is not None)): #se for jogador e estiver atacando
          mensagem = f"{personagem_atual.nome} atacou {inimigo_atual.nome}"
        else:
          mensagem = f"{personagem_atual.nome} defendeu"
      else:
        if (personagem_atual.acao == 0):
          mensagem = f"{personagem_atual.nome} atacou {batalha.alvo_inimigo.nome}"
        else:
          mensagem = f"{personagem_atual.nome} defendeu"

      escrever(janela, mensagem, (40, 620), PRETO)
      pygame.display.flip()

      tempo_inicial = pygame.time.get_ticks()
      while pygame.time.get_ticks() - tempo_inicial < tempo_mensagem:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            running = False
            break
        if not running:
          break
        clock.tick(FPS)

    # condição de parada
    acabou = batalha.acabou()

    # encerra jogo se algum dos times estiver sem integrantes
    if acabou and running:
      exibir_tela_final(janela, batalha)
      running = False

    # passa turno
    elif trocar_personagem and running:
      # atualiza ordem dos ataques e retira personagens mortos
      ordem_jogada = batalha.ordem_acoes()
      personagem_atual_index = ordem_jogada.index(personagem_atual)

      # Avance para o próximo personagem na ordem de jogada
      contPersonagem += 1
      personagem_atual_index = (personagem_atual_index + 1) % len(ordem_jogada)

      # passa para o proximo personagem
      personagem_atual = ordem_jogada[personagem_atual_index]
      trocar_personagem = False

      # passa rodada e conserta valores de defesa
      if contPersonagem >= len(ordem_jogada):
        contPersonagem = 0
        rodada += 1
        for personagem in batalha.defendeu:
          personagem.defesa /= 2
        batalha.defendeu = []

    # Define tickrate
    clock.tick(FPS)

  pygame.quit()

if __name__ == "__main__":
  main()