def coletar_resposta(contexto):
  while True:
    pergunta = contexto["pergunta"]
    opcoes = contexto["opcoes"]

    indice = 1
    numeroDeOpcoes = len(opcoes)

    print("\n")
    print(pergunta)
    for opcao in opcoes:
      print("[", indice, "]", opcao)
      indice += 1
    
    resposta = int(input("Escolha uma opção: "))

    if (0 < resposta <= numeroDeOpcoes):
      return resposta
    
    print("\nEscolha uma das opções disponíveis.")