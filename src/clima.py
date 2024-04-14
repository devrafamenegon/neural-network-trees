import json
from utils.coletar_resposta import coletar_resposta

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES
with open('src/scripts/clima.json', 'r', encoding='utf-8') as clima_json: 
  dados_clima = json.load(clima_json)

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

