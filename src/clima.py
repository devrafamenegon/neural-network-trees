import json
from utils.coletar_resposta import coletar_resposta
from utils.redimencionar_valores import redimencionar_valores
from sklearn.neural_network import MLPClassifier

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES
with open('src/scripts/clima.json', 'r', encoding='utf-8') as clima_json: 
  dados_clima = json.load(clima_json)

with open('src/scripts/clima_resultados.json', 'r', encoding='utf-8') as clima_resultados_json: 
  dados_clima_resultados = json.load(clima_resultados_json)

categorias = {
  "temperatura": dados_clima["temperatura"],
  "pluviosidade": dados_clima["pluviosidade"],
  "umidade": dados_clima["umidade"],
  "vento": dados_clima["vento"],
  "neve": dados_clima["neve"],
  "neblina": dados_clima["neblina"],
  "tempestade": dados_clima["tempestade"],
}

respostas = {
  "temperatura": coletar_resposta("temperatura", categorias),
  "pluviosidade": coletar_resposta("pluviosidade", categorias),
  "umidade": coletar_resposta("umidade", categorias),
  "vento": coletar_resposta("vento", categorias),
  "neve": coletar_resposta("neve", categorias),
  "neblina": coletar_resposta("neblina", categorias),
  "tempestade": coletar_resposta("tempestade", categorias)
}

rede_clima = MLPClassifier(
  solver='lbfgs',
  activation='logistic', 
  alpha=1e-8,
  hidden_layer_sizes=(20, 20), 
  random_state=1
)

x = []
y = []

climas = dados_clima_resultados["climas"]
for clima in climas:
  y.append(clima["nome"])
  del clima["nome"]

  x.append(redimencionar_valores(clima))

rede_clima.fit(x, y)

print(rede_clima.predict([redimencionar_valores(respostas)])[0])