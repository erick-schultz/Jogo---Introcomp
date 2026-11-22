import pygame #importando biblioteca
import random #importando biblioteca

from jogador import Jogador
from inimigo import Inimigo

# Implementa uma batalha entre jogadores e inimigos, controlando a ordem das ações, executando ataques e defesas, verificando se a batalha terminou e exibindo o resultado.
class Batalha(): #criando classe batalha
  def __init__(self, jogadores, inimigos, janela): #construtor da classe
      self.jogadores = jogadores
      self.inimigos = inimigos
      self.janela = janela
      self.personagem_atual = self.ordem_acoes()[0] #personagem jogando no momento
      self.alvo = inimigos.sprites()[0] #inimigo alvo
      self.alvo_inimigo = jogadores.sprites()[0]
      self.rodada = 1
      self.defendeu = []

  # Cria uma lista de personagens de ambos os lados e classifique-os por velocidade em ordem decrescente
  def ordem_acoes(self) -> list: # cria lista com a ordem dos jogadores no jogo
    todos_os_personagens = [] #criando lista
    for jogador in self.jogadores:
      if jogador.pontos_vida > 0:
        todos_os_personagens.append(jogador) #adicionando todos jogadores 
    for inimigo in self.inimigos:
      if inimigo.pontos_vida > 0:
        todos_os_personagens.append(inimigo) #adicionando todos os inimigos
          
    todos_os_personagens.sort(key=lambda char: char.velocidade, reverse=True) # ordena a lista por velocidade
      
    return todos_os_personagens #retorna a lista


  def escolher_alvo_do_inimigo(self, inimigo): # inimigo escolhe alvo aleatoriamente
    alvos_disponiveis = []
    for i, jogador in enumerate(self.jogadores.sprites()):
      if jogador.pontos_vida > 0:
        alvos_disponiveis.append(jogador)
        
    #while True:
    escolha = int(random.choice(range(1, len(alvos_disponiveis) + 1)))
    alvo_index = escolha - 1
    self.alvo_inimigo = alvos_disponiveis[alvo_index]
    return 0


  def acabou(self) -> bool: #mostra se os personagens morrerram
      cont_jog = 0
      cont_ini = 0

      for jogador in self.jogadores:
          if (jogador.pontos_vida <= 0): # se os pontos de vida do jogador forem menor ou iguais a 0
              cont_jog += 1 #incrementa o contador
      if (cont_jog == len(self.jogadores.sprites())):
          return True

      for inimigo in self.inimigos:
          if (inimigo.pontos_vida <= 0): #se os pontos de vida do inimigo forem menor ou iguais a 0
              cont_ini += 1 #incrementa o contador
      if (cont_ini == len(self.inimigos.sprites())):
          return True
      return False

  def finalizar_batalha(self): #exibe se vc ganhou ou perdeu o jogo
      if all(jogador.pontos_vida <= 0 for jogador in self.jogadores):
          frase = "Você perdeu! Todos os seus personagens foram derrotados."
          return (frase, "perdeu") #retorna tuplas para exibir na tela cores diferentes
      elif all(inimigo.pontos_vida <= 0 for inimigo in self.inimigos):
          frase = "Você venceu! Todos os inimigos foram derrotados."
          return (frase, "venceu") #retorna tuplas para exibir na tela cores diferentes

  def realizar_acao_do_jogador(self, jogador) -> None: #ação do jogador atacar X defender
    if (jogador.acao == 0): #atacar
      if jogador.pontos_vida > 0:
        alvo = self.alvo
        dano = jogador.atacar(alvo.defesa)
        alvo.receber_dano(dano)
       
        
    elif (jogador.acao == 1): #defender
      if jogador.pontos_vida > 0:
        jogador.defender()
        self.defendeu.append(jogador)
              

  def realizar_acao_do_inimigo(self, inimigo): # turno do inimigo
    if (inimigo.pontos_vida > 0): #se inimigo estiver vivo
      if (inimigo.acao == 0): # se ele escolheu atacar
        self.escolher_alvo_do_inimigo(inimigo)
        alvo = self.alvo_inimigo
        dano = inimigo.atacar(alvo.defesa)
        alvo.receber_dano(dano)

        
      elif (inimigo.acao == 1): #se ele escolher defender
        inimigo.defender()
        self.defendeu.append(inimigo)

  def passar_turno(self): # Atualize o jogador atual e o alvo para a próxima rodada
    personagens_disponiveis = self.ordem_acoes()
    personagen_atual_index = personagens_disponiveis.index(self.personagem_atual)
    proximo_index = (personagen_atual_index + 1) % len(personagens_disponiveis)
    self.personagem_atual = personagens_disponiveis[proximo_index]
    
    self.rodada += 1
    
    return True

