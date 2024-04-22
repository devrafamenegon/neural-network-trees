from PIL import Image
import matplotlib.pyplot as plt

def mostrar_imagem(path):
  extensoes = ['.jpg', '.jpeg', '.png', '.webp']
  imagemEncontrada = False

  for extensao in extensoes:
    try:
      img = Image.open(path + extensao)
      plt.imshow(img)
      plt.show()
      imagemEncontrada = True
    except FileNotFoundError:
      pass

  if not imagemEncontrada:
    print('Nenhuma imagem encontrada.')