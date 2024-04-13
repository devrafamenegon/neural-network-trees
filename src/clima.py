import json

# IMPORTAÇÃO DO SCRIPT COM AS OPÇÔES DE PERGUNTAS/RESPOSTAS
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