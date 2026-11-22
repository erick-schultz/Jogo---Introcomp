import pygame
import random

from personagem import Personagem

# Cria classe Inimigo que herda de Personagem
class Inimigo(Personagem):
  def __init__(self, nome, x, y, ataque, defesa, velocidade, caminho_imagem):
    super().__init__(nome, x, y, ataque, defesa, velocidade, caminho_imagem)

    self.imagem = pygame.image.load(f"{caminho_imagem}")
    self.imagem = pygame.transform.scale_by(self.imagem, self.tamanho)
    self.imagem = pygame.transform.flip(self.imagem, True, False)  #espelha a imagem

  def escolher_acao(self):
    self.acao = random.choice([0,1])
    if (self.acao == 0):
      return "ATACAR"
    else:
      return "DEFENDER"
    