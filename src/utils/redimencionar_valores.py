def redimencionar_valores(valores, valor_maximo):
  return list(map(lambda x: x / valor_maximo, [*valores.values()]))

def redimencionar_valor_escala_1(valor_original, valor_maximo):
  return valor_original / valor_maximo