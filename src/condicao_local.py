import json
from utils.coletar_resposta import coletar_resposta
from utils.redimencionar_valores import redimencionar_valor_escala_1
from sklearn.neural_network import MLPClassifier

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES DE ENTRADA
with open('./scripts/condicao_local/opcoes_entrada.json', 'r', encoding='utf-8') as condicao_local_opcoes_entrada: 
  opcoes_entrada = json.load(condicao_local_opcoes_entrada)

# IMPORTAÇÃO DO SCRIPT COM AS ENTRADAS/SAIDAS DE TREINAMENTO
with open('./scripts/condicao_local/treinamentos.json', 'r', encoding='utf-8') as condicao_local_treinamentos: 
  entradas_saidas = json.load(condicao_local_treinamentos)

def treinar_rede():
  # CRIAÇÃO DA REDE
  rede_condicao_local = MLPClassifier(
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

  # PARA CADA CONDIÇÃO LOCAL
  for condicao_local in entradas_saidas["treinamentos"]:
    # DEFINA A SAIDA DA REDE COMO O NÍVEL DE CONDIÇÃO LOCAL
    y.append(condicao_local["saida"])

    # VARIAVEL QUE ARMAZENARA AS ENTRADAS REDIMENCIONADAS
    entradas_teste_redimencionadas = []

    for entrada in condicao_local["entradas"]:
      valor = condicao_local["entradas"][entrada]
      numeroDeOpcoes = len(opcoes_entrada[entrada])

      # REDIMENCIONANDO AS ENTRADAS EM ESCALA ATÉ 1
      entradas_teste_redimencionadas.append(
        redimencionar_valor_escala_1(valor, numeroDeOpcoes)
      )
    
    x.append(entradas_teste_redimencionadas)

  # TREINANDO A REDE
  rede_condicao_local.fit(x, y)

  return rede_condicao_local

def utilizar_rede_condicao_local(clima):
  # INSTANCIANDO UMA REDE TREINADA
  rede_condicao_local = treinar_rede()

  # COLETANDO ENTRADAS DO USUÁRIO
  entradas_usuario = {
    "clima": opcoes_entrada["clima"].index(clima),
    "altura": coletar_resposta(opcoes_entrada["altura"]),
    "espaco_ao_redor": coletar_resposta(opcoes_entrada["espaco_ao_redor"]),
    "solo": coletar_resposta(opcoes_entrada["solo"]),
    "relevo": coletar_resposta(opcoes_entrada["relevo"]),
    "drenagem": coletar_resposta(opcoes_entrada["drenagem"]),
  }

  entradas_usuario_redimencionadas = []

  for entrada in entradas_usuario:
    valor = entradas_usuario[entrada]
    numeroDeOpcoes = len(opcoes_entrada[entrada])

    entradas_usuario_redimencionadas.append(
      redimencionar_valor_escala_1(valor, numeroDeOpcoes)
    )

  resultado = rede_condicao_local.predict([entradas_usuario_redimencionadas])
  print("\n- ", resultado[0])
  return resultado
