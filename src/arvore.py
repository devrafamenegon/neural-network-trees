import json
from utils.coletar_resposta import coletar_resposta
from utils.redimencionar_valores import redimencionar_valor_escala_1
from sklearn.neural_network import MLPClassifier
from PIL import Image
import matplotlib.pyplot as plt

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES DE ENTRADA
with open('./scripts/arvore/opcoes_entrada.json', 'r', encoding='utf-8') as arvore_opcoes_entrada: 
  opcoes_entrada = json.load(arvore_opcoes_entrada)

# IMPORTAÇÃO DO SCRIPT COM AS ENTRADAS/SAIDAS DE TREINAMENTO
with open('./scripts/arvore/treinamentos.json', 'r', encoding='utf-8') as arvore_treinamentos: 
  treinamentos = json.load(arvore_treinamentos)

def treinar_rede():
  # CRIAÇÃO DA REDE
  rede = MLPClassifier(
    solver='lbfgs',
    activation='logistic', 
    alpha=1e-8,
    hidden_layer_sizes=(100, 100), 
    random_state=1
  )

  # ENTRADAS TREINAMENTO
  x = []

  # SAÍDAS TREINAMENTO
  y = []

  # PARA CADA ÁRVORE
  for arvore in treinamentos["treinamentos"]:
    # DEFINA A SAIDA DA REDE COMO O NOME DA ÁRVORE
    y.append(arvore["saida"])

    # VARIAVEL QUE ARMAZENARA AS ENTRADAS REDIMENCIONADAS
    entradas_teste_redimencionadas = []

    for entrada in arvore["entradas"]:
      valor = arvore["entradas"][entrada]
      numeroDeOpcoes = len(opcoes_entrada[entrada])

      # REDIMENCIONANDO AS ENTRADAS EM ESCALA ATÉ 1
      entradas_teste_redimencionadas.append(
        redimencionar_valor_escala_1(valor, numeroDeOpcoes)
      )
    
    x.append(entradas_teste_redimencionadas)

  # TREINANDO A REDE
  rede.fit(x, y)

  return rede

def utilizar_rede_arvore(clima, condicao_local, capacidade_manutencao):
  # INSTANCIANDO UMA REDE TREINADA
  rede = treinar_rede()

  # COLETANDO ENTRADAS DO USUÁRIO
  entradas_usuario = {
    "clima": opcoes_entrada["clima"].index(clima),
    "condicao_local": opcoes_entrada["condicao_local"].index(condicao_local),
    "capacidade_manutencao": opcoes_entrada["capacidade_manutencao"].index(capacidade_manutencao),
    "maturidade": coletar_resposta(opcoes_entrada["maturidade"]),
    "tipo_de_copa": coletar_resposta(opcoes_entrada["tipo_de_copa"]),
    "flores": coletar_resposta(opcoes_entrada["flores"]),
    "frutos": coletar_resposta(opcoes_entrada["frutos"]),
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

  for arvore in treinamentos["treinamentos"]:
    if (resultado == arvore["saida"]):
      for informacao_adicional in arvore["informacoes_adicionais"]:
        print("  • ", informacao_adicional.capitalize(), ":", arvore["informacoes_adicionais"][informacao_adicional])
      
      img = Image.open('./assets/Moringa (Moringa oleifera).jpg')
      plt.imshow(img)
      plt.show()
      break
      

  return resultado
