import json
from utils.coletar_resposta import coletar_resposta
from utils.redimencionar_valores import redimencionar_valor_escala_1
from sklearn.neural_network import MLPClassifier

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES DE ENTRADA
with open('src/scripts/condicoes_locais_opcoes_entrada.json', 'r', encoding='utf-8') as condicoes_locais_opcoes_entrada: 
  opcoes_entrada = json.load(condicoes_locais_opcoes_entrada)

# IMPORTAÇÃO DO SCRIPT COM AS ENTRADAS/SAIDAS TESTE
with open('src/scripts/condicoes_locais_treinamentos.json', 'r', encoding='utf-8') as condicoes_locais_treinamentos: 
  entradas_saidas = json.load(condicoes_locais_treinamentos)

def treinar_rede():
  # CRIAÇÃO DA REDE
  rede_condicoes_locais = MLPClassifier(
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

  # PARA CADA condicoes_locais
  for condicoes_locais in entradas_saidas["treinamentos"]:
    # DEFINA A SAIDA DA REDE COMO O NOME DO condicoes_locais
    y.append(condicoes_locais["saida"])

    # VARIAVEL QUE ARMAZENARA AS ENTRADAS REDIMENCIONADAS
    entradas_teste_redimencionadas = []

    for entrada in condicoes_locais["entradas"]:
      valor = condicoes_locais["entradas"][entrada]
      numeroDeOpcoes = len(opcoes_entrada[entrada])

      # REDIMENCIONANDO AS ENTRADAS EM ESCALA ATÉ 1
      entradas_teste_redimencionadas.append(
        redimencionar_valor_escala_1(valor, numeroDeOpcoes)
      )
    
    x.append(entradas_teste_redimencionadas)

  # TREINANDO A REDE
  rede_condicoes_locais.fit(x, y)

  return rede_condicoes_locais

def utilizar_rede_condicoes_locais(clima):
  # INSTANCIANDO UMA REDE TREINADA
  rede_condicoes_locais = treinar_rede()

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

  resultado = rede_condicoes_locais.predict([entradas_usuario_redimencionadas])
  print("\n- ", resultado[0])
  return resultado
