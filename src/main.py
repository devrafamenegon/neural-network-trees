from clima import utilizar_rede_clima
from condicoes_locais import utilizar_rede_condicoes_locais
from capacidade_manutencao import utilizar_rede_capacidade_manutencao
from arvore import utilizar_rede_arvore

print("\nEscolha Ideal de Árvores para Plantio 🌳🌿\n")

clima = utilizar_rede_clima()
condicoes_locais = utilizar_rede_condicoes_locais(clima)
capacidade_manutencao = utilizar_rede_capacidade_manutencao(condicoes_locais)
arvore = utilizar_rede_arvore(clima, condicoes_locais, capacidade_manutencao)
