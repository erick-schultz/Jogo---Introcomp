import pygame
from personagem import Personagem

# Cria classe Jogador que herda de Personagem
class Jogador(Personagem):
  def __init__(self, nome, x, y, ataque, defesa, velocidade, caminho_imagem):
    # Inicializa herança de Personagem
    super().__init__(nome, x, y, ataque, defesa, velocidade, caminho_imagem)
    # Define atributos da habilidade do jogador (1 - 5)
    #self.habilidade = habilidade

  # Define o método de habilidade do jogador
  '''
  def usar_habilidade(self):
    lista_habilidades = ["Ataque Especial", "Defesa Especial", "Velocidade Especial"]
    switch case
    1
    2
    3
    4
    5
  '''
  