import pygame
import random

from jogador import Jogador
from inimigo import Inimigo

# Implementa uma batalha entre jogadores e inimigos, controlando a ordem das ações, executando ataques e defesas, verificando se a batalha terminou e exibindo o resultado.
class Batalha():
  def __init__(self, jogadores, inimigos, janela):
      self.jogadores = jogadores
      self.inimigos = inimigos
      self.janela = janela
      self.personagem_atual = self.ordem_acoes()[0]
      self.alvo = inimigos.sprites()[0]
      self.alvo_inimigo = jogadores.sprites()[0]
      self.rodada = 1
      self.defendeu = []

  # Cria uma lista de personagens de ambos os lados e classifique-os por velocidade em ordem decrescente
  def ordem_acoes(self) -> list:
    todos_os_personagens = []
    for jogador in self.jogadores:
      if jogador.pontos_vida > 0:
        todos_os_personagens.append(jogador)
    for inimigo in self.inimigos:
      if inimigo.pontos_vida > 0:
        todos_os_personagens.append(inimigo)
          
    todos_os_personagens.sort(key=lambda char: char.velocidade, reverse=True)
      
    return todos_os_personagens

  def iniciar_batalha(self) -> None:
    while (not self.acabou()):
      self.realizar_turno()
      for personagem in self.defendeu:
        personagem.defesa /= 2
      for personagem in self.ordem_acoes():
        print(personagem.nome, personagem.defesa)
      self.passar_turno()
      self.defendeu = []
     
    self.finalizar_batalha()

  def escolher_alvo_do_jogador(self, jogador):
    print(f"{jogador.nome}, escolha seu alvo:")
    alvos_disponiveis = []
    for i, inimigo in enumerate(self.inimigos.sprites()):
        if inimigo.pontos_vida > 0:
            print(f"{i + 1}: {inimigo.nome} ({inimigo.pontos_vida} pontos de vida)")
            alvos_disponiveis.append(inimigo)

    while True:
        escolha = input("Digite o número do inimigo que deseja atacar (1 ou 2): ")
        if escolha in ["1", "2"]:
            alvo_index = int(escolha) - 1
            self.alvo = alvos_disponiveis[alvo_index]
            return 0
        else:
            print("Escolha inválida. Por favor, digite 1 ou 2.")

  def escolher_alvo_do_inimigo(self, inimigo):
    print(f"{inimigo.nome}, escolha seu alvo:")
    alvos_disponiveis = []
    for i, jogador in enumerate(self.jogadores.sprites()):
      if jogador.pontos_vida > 0:
        print(f"{i + 1}: {jogador.nome} ({jogador.pontos_vida} pontos de vida)")
        alvos_disponiveis.append(jogador)
        
    #while True:
    escolha = int(random.choice(range(1, len(alvos_disponiveis) + 1)))
    alvo_index = escolha - 1
    self.alvo_inimigo = alvos_disponiveis[alvo_index]
    return 0
  
  def realizar_turno(self) -> None:
      ordem = self.ordem_acoes()
      for personagem in ordem:
        print(personagem.pontos_vida)
        if personagem.pontos_vida > 0:
          if personagem in self.jogadores:
            # Vez do jogador
            personagem.update()
            self.realizar_acao_do_jogador(personagem)
          elif personagem in self.inimigos:
            # Vez do inimigo
            print(personagem.nome)
            personagem.update()
            self.realizar_acao_do_inimigo(personagem)
        

  #def imprimir_na_tela():

  def acabou(self) -> bool:
      cont_jog = 0
      cont_ini = 0

      for jogador in self.jogadores:
          if (jogador.pontos_vida <= 0):
              cont_jog += 1
      if (cont_jog == len(self.jogadores.sprites())):
          return True

      for inimigo in self.inimigos:
          if (inimigo.pontos_vida <= 0):
              cont_ini += 1
      if (cont_ini == len(self.inimigos.sprites())):
          return True

  def finalizar_batalha(self) -> None: #exibe se vc ganhou ou perdeu o jogo
      if all(jogador.pontos_vida <= 0 for jogador in self.jogadores):
          print("Você perdeu! Todos os seus personagens foram derrotados.")
      elif all(inimigo.pontos_vida <= 0 for inimigo in self.inimigos):
          print("Você venceu! Todos os inimigos foram derrotados.")

  def realizar_acao_do_jogador(self, jogador) -> None:
    if (jogador.acao == "ATACAR"):
      if jogador.pontos_vida > 0:
        self.escolher_alvo_do_jogador(jogador)
        alvo = self.alvo
        dano = jogador.atacar(alvo.defesa)
        alvo.receber_dano(dano)
        print(f"{jogador.nome} atacou {alvo.nome} causando {dano} de dano. {alvo.pontos_vida}")
        
    elif (jogador.acao == "DEFENDER"):
      if jogador.pontos_vida > 0:
        jogador.defender()
        print(f"{jogador.nome} está em posição defensiva no próximo turno. {jogador.defesa}")
        self.defendeu.append(jogador)
              

  def realizar_acao_do_inimigo(self, inimigo):
    if (inimigo.pontos_vida > 0):
      if (inimigo.acao == 0):
        self.escolher_alvo_do_inimigo(inimigo)
        alvo = self.alvo_inimigo
        dano = inimigo.atacar(alvo.defesa)
        alvo.receber_dano(dano)
        print(f"{inimigo.nome} atacou {alvo.nome} causando {dano} de dano. {alvo.pontos_vida}")
        
      elif (inimigo.acao == 1):
        inimigo.defender()
        print(f"{inimigo.nome} está em posição defensiva no próximo turno.")
        self.defendeu.append(inimigo)

  def passar_turno(self):
    # Atualize o jogador atual e o alvo para a próxima rodada
    personagens_disponiveis = self.ordem_acoes()
    personagen_atual_index = personagens_disponiveis.index(self.personagem_atual)
    proximo_index = (personagen_atual_index + 1) % len(personagens_disponiveis)
    self.persognagem_atual = personagens_disponiveis[proximo_index]
    
    self.rodada += 1
    
    return True

