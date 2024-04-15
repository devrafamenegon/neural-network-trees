def coletar_resposta(opcoes):
  while True:
    indice = 1
    numeroDeOpcoes = len(opcoes)

    print("\n")
    
    for opcao in opcoes:
      print("[", indice, "]", opcao)
      indice += 1
    
    resposta = int(input("Escolha uma opção: "))

    if (0 < resposta <= numeroDeOpcoes):
      return resposta
    
    print("\nEscolha uma das opções disponíveis.\n")