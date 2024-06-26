import json
from utils.coletar_resposta import coletar_resposta
from utils.redimencionar_valores import redimencionar_valor_escala_1
from utils.mostrar_imagem import mostrar_imagem
from sklearn.neural_network import MLPClassifier

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES DE ENTRADA
with open('./scripts/clima/opcoes_entrada.json', 'r', encoding='utf-8') as clima_opcoes_entrada: 
  opcoes_entrada = json.load(clima_opcoes_entrada)

# IMPORTAÇÃO DO SCRIPT COM AS ENTRADAS/SAIDAS DE TREINAMENTO
with open('./scripts/clima/treinamentos.json', 'r', encoding='utf-8') as clima_treinamentos: 
  treinamentos = json.load(clima_treinamentos)

def treinar_rede():
  # CRIAÇÃO DA REDE
  rede = MLPClassifier(
    solver='lbfgs',
    activation='logistic', 
    alpha=1e-8,
    hidden_layer_sizes=(20, 20), 
    random_state=1
  )

  # ENTRADAS TREINAMENTO
  x = []

  # SAÍDAS TREINAMENTO
  y = []

  # PARA CADA CLIMA
  for clima in treinamentos["treinamentos"]:
    # DEFINA A SAIDA DA REDE COMO O NOME DO CLIMA
    y.append(clima["saida"])

    # VARIAVEL QUE ARMAZENARA AS ENTRADAS REDIMENCIONADAS
    entradas_teste_redimencionadas = []

    for entrada in clima["entradas"]:
      valor = clima["entradas"][entrada]
      numeroDeOpcoes = len(opcoes_entrada[entrada])

      # REDIMENCIONANDO AS ENTRADAS EM ESCALA ATÉ 1
      entradas_teste_redimencionadas.append(
        redimencionar_valor_escala_1(valor, numeroDeOpcoes)
      )
    
    x.append(entradas_teste_redimencionadas)

  # TREINANDO A REDE
  rede.fit(x, y)

  return rede

def utilizar_rede_clima():
  # INSTANCIANDO UMA REDE TREINADA
  rede = treinar_rede()

  # COLETANDO ENTRADAS DO USUÁRIO
  entradas_usuario = {
    "temperatura": coletar_resposta(opcoes_entrada["temperatura"]),
    "pluviosidade": coletar_resposta(opcoes_entrada["pluviosidade"]),
    "umidade": coletar_resposta(opcoes_entrada["umidade"]),
    "vento": coletar_resposta(opcoes_entrada["vento"]),
    "neve": coletar_resposta(opcoes_entrada["neve"]),
    "neblina": coletar_resposta(opcoes_entrada["neblina"]),
    "tempestade": coletar_resposta(opcoes_entrada["tempestade"])
  }

  entradas_usuario_redimencionadas = []

  for entrada in entradas_usuario:
    valor = entradas_usuario[entrada]
    numeroDeOpcoes = len(opcoes_entrada[entrada])

    entradas_usuario_redimencionadas.append(
      redimencionar_valor_escala_1(valor, numeroDeOpcoes)
    )

  resultado = rede.predict([entradas_usuario_redimencionadas])
  print("\n- ", resultado[0])

  path = './assets/clima/' + resultado[0]
  mostrar_imagem(path)

  return resultado
