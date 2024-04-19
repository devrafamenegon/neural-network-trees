from clima import utilizar_rede_clima
from condicao_local import utilizar_rede_condicao_local
from capacidade_manutencao import utilizar_rede_capacidade_manutencao
from arvore import utilizar_rede_arvore

print("\nEscolha Ideal de Árvores para Plantio 🌳🌿\n")

clima = utilizar_rede_clima()
condicao_local = utilizar_rede_condicao_local(clima)
capacidade_manutencao = utilizar_rede_capacidade_manutencao(condicao_local)
arvore = utilizar_rede_arvore(clima, condicao_local, capacidade_manutencao)
