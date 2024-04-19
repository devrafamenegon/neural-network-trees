import json
from utils.coletar_resposta import coletar_resposta
from utils.redimencionar_valores import redimencionar_valor_escala_1
from sklearn.neural_network import MLPClassifier

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES DE ENTRADA
with open('./scripts/capacidade_manutencao/opcoes_entrada.json', 'r', encoding='utf-8') as capacidade_manutencao_opcoes_entrada: 
  opcoes_entrada = json.load(capacidade_manutencao_opcoes_entrada)

# IMPORTAÇÃO DO SCRIPT COM AS ENTRADAS/SAIDAS DE TREINAMENTO
with open('./scripts/capacidade_manutencao/treinamentos.json', 'r', encoding='utf-8') as capacidade_manutencao_treinamentos: 
  treinamentos = json.load(capacidade_manutencao_treinamentos)

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

  # PARA CADA CAPACIDADE DE MANUTENÇÃO
  for capacidade_manutencao in treinamentos["treinamentos"]:
    # DEFINA A SAIDA DA REDE COMO O NÍVEL DA CAPACIDADE DE MANUTENÇÃO
    y.append(capacidade_manutencao["saida"])

    # VARIAVEL QUE ARMAZENARA AS ENTRADAS REDIMENCIONADAS
    entradas_teste_redimencionadas = []

    for entrada in capacidade_manutencao["entradas"]:
      valor = capacidade_manutencao["entradas"][entrada]
      numeroDeOpcoes = len(opcoes_entrada[entrada])

      # REDIMENCIONANDO AS ENTRADAS EM ESCALA ATÉ 1
      entradas_teste_redimencionadas.append(
        redimencionar_valor_escala_1(valor, numeroDeOpcoes)
      )
    
    x.append(entradas_teste_redimencionadas)

  # TREINANDO A REDE
  rede.fit(x, y)

  return rede

def utilizar_rede_capacidade_manutencao(condicao_local):
  # INSTANCIANDO UMA REDE TREINADA
  rede = treinar_rede()

  # COLETANDO ENTRADAS DO USUÁRIO
  entradas_usuario = {
    "condicao_local": opcoes_entrada["condicao_local"].index(condicao_local),
    "experiencia": coletar_resposta(opcoes_entrada["experiencia"]),
    "dedicacao": coletar_resposta(opcoes_entrada["dedicacao"]),
    "aptidao": coletar_resposta(opcoes_entrada["aptidao"]),
    "disposicao_para_aprender": coletar_resposta(opcoes_entrada["disposicao_para_aprender"]),
    "acesso_a_ferramentas": coletar_resposta(opcoes_entrada["acesso_a_ferramentas"]),
    "contratar_um_profissional": coletar_resposta(opcoes_entrada["contratar_um_profissional"]),
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
  return resultado
