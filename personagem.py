import pygame
import sys

# Cria classe personagem que vai ser extendida por Jogador e Inimigo, classe derivada de sprite

class Personagem(pygame.sprite.Sprite):
  def __init__(self, nome, x, y, ataque, defesa, velocidade, caminho_imagem):
    # Inicializa herança de sprite
    pygame.sprite.Sprite.__init__(self)

    # Define atributos do personagem
    self.nome = nome
    self.pontos_vida = 100 #0 - 100
    self.vida_total = self.pontos_vida
    self.x = x
    self.y = y
    self.ataque = ataque #0 - 100
    self.defesa = defesa #0 - 100
    self.velocidade = velocidade #0 - 10
    self.tamanho = 3
    self.acao = None

    # Define atributos de imagem do sprite
    self.imagem = pygame.image.load(f"{caminho_imagem}")
    self.imagem = pygame.transform.scale_by(self.imagem, self.tamanho)

  #  atualiza self.morreu() e escolhe acao
  def update(self):
    if not self.morreu():
      self.escolher_acao()
    

  # Define o método de ataque do personagem (comum à Jogador e à Inimigo)
  def atacar(self, defesa_inimigo) -> float: 
    dano = (self.ataque) * (50/(50 + defesa_inimigo))
    return dano

  # Define o método de defesa do personagem (comum à Jogador e à Inimigo)
  def defender(self) -> None:
    self.defesa *= 2

  # Método para receber o dano tomado em batalha
  def receber_dano(self, dano) -> None:
    self.pontos_vida -= dano
    if (self.pontos_vida <= 0):
      self.imagem = pygame.image.load("morte.png")
      self.imagem = pygame.transform.scale(self.imagem, (200,200))

  def morreu(self) -> bool:
    if (self.pontos_vida <= 0):
      return True
