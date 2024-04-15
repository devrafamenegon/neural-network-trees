def coletar_resposta(opcoes):
  while True:
    indice = 1
    numeroDeOpcoes = len(opcoes)

    for opcao in opcoes:
      print(indice, opcao)
      indice += 1
    
    resposta = int(input("Escolha uma opção: "))

    if (0 < resposta <= numeroDeOpcoes):
      print(resposta)
      return resposta
    
    print("Escolha uma das opções disponíveis")