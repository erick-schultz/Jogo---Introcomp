class Window:  # criando classe janela
  __width = 0  # criou largura
  __height = 0  # criou altura
  __color = (255,255,255)  # definiu cor

  def __init__(self, altura, largura): #criando construtor
      self.__width = largura
      self.__height = altura

  def returnWinSize(self): #retorna valor da janela
      return (self.__width, self.__height)

  def returnColor(self):  # retorna a cor da janela
      return self.__color 

