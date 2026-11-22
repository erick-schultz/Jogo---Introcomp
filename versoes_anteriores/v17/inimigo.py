import pygame #importando biblioteca
import random #importando biblioteca

from personagem import Personagem

# Cria classe Inimigo que herda de Personagem
class Inimigo(Personagem): #construtor da classe
  def __init__(self, nome, x, y, ataque, defesa, velocidade, caminho_imagem, seta_pos):
    super().__init__(nome, x, y, ataque, defesa, velocidade, caminho_imagem)

    self.imagem = pygame.image.load(f"{caminho_imagem}")
    self.imagem = pygame.transform.scale_by(self.imagem, self.tamanho)
    self.imagem = pygame.transform.flip(self.imagem, True, False)#espelha a imagem
    self.seta_pos = seta_pos

  def escolher_acao(self): #escolhe entre atacar X defender aleatoriamente
    self.acao = random.choice([0,1])
    
    