def coletar_resposta(categoria, categorias):
  while True:
    indice = 1
    opcoes = categorias[categoria]
    numeroDeOpcoes = len(opcoes)

    for opcao in opcoes:
      print(indice, opcao)
      indice += 1
    
    resposta = int(input("Escolha uma opção: "))

    if (resposta >= numeroDeOpcoes | resposta <= numeroDeOpcoes):
      return resposta
    
    print("Escolha uma das opções disponíveis")