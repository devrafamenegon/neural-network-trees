## **Tema: Escolha Ideal de Árvores para Plantio 🌳🌿**

**Descrição do Problema:**

A escolha da árvore ideal para plantar pode ser um desafio complexo, pois depende de diversos fatores como **clima, condições locais e capacidade de manutenção**. Este modelo de rede neural, visa auxiliar na tomada de decisão sobre qual árvore é mais adequada para cada situação, levando em consideração esses três aspectos.

**Estrutura da Rede:**

A rede neural é composta por quatro sub-redes interligadas: [Desenho das Redes](https://whimsical.com/redes-neurais-arvores-UEz9q62GnM1Rrs1PjFmFNA@6HYTAunKLgTV49MPDN8N5HaGmfqjrBQNp8mUEnN1yba8hfi) ✍

## **Sub-rede Neural "Clima" ☀️🌧️❄️💨**

**Objetivo:** Identificar o clima com base nas características climáticas informadas.

**Entradas:**

- **Temperatura:** Valores como temperatura média anual, amplitude térmica.
- **Pluviosidade:** Precipitação anual média.
- **Umidade:** Umidade relativa do ar média.
- **Vento:** Velocidade média do vento.
- **Neve:** Frequência média de neve.
- **Neblina:** Frequência média de neblina.
- **Tempestades:** Incidência média de tempestades.

**Saída:**

- **Clima:** O clima que se adequar com as entradas especificadas. Exemplo: Clima Temperado Úmido.

## **Sub-rede Neural "Condições Locais" 🏞️**

**Objetivo:** Definir a qualidade do local de plantio.

**Entradas:**

- **Solo:** Tipo de solo (argiloso, arenoso, limoso).
- **Relevo:** Características do relevo (plano, encosta, vale).
- _(Faltam campos)_

**Saída:**

- **Nível de condição local,** entre 1 a 7. (_Nível 1: Ótimas Condições para Plantio, Nível 7: Condições Impróprias para Plantio_).

## **Sub-rede Neural "Capacidade de Manutenção" 🛠️**

**Objetivo:** Definir a capacidade de manutenção do usuário.

**Entradas:**

- **Experiência:** [1] - Já cuidei de árvores em minha casa, quintal, trabalho ou outro local. [2] - Nunca cuidei de árvores antes.
- _(Faltam campos)_

**Saída:**

- **Nível de condição de manutenção do indivíduo,** entre 1 a 7. (_Nível 1: Excelente Manutenção, Nível 7: Manutenção Deficiente_).

## **Sub-rede Neural "Características" 🌱**

**Objetivo:** Receber características específicas e retornar a árvore que mais se adeque a todas as demais entradas (**Clima, nível de condição local e nível de condição de manutenção**).

**Entradas:**

- **Capacidade de manutenção** (resultado da rede Capacidade de Manutenção).
- **Condições locais** (resultado da rede Condições locais).
- **Clima** (resultado da rede Clima).
- _(Faltam campos)_

**Saídas:**

- **Características das Árvores:** Descrição detalhada das características de cada árvore, incluindo:
  - **Tamanho:** Altura madura média.
  - **Forma da copa:** Colunar, arredondada, oval, etc.
  - **Taxa de crescimento:** Lento, moderado, rápido.
  - **Flores:** Descrição da floração (cor, época, duração).
  - **Frutos:** Descrição dos frutos (comestíveis, ornamentais, atrativos para a fauna).
  - **Cuidados específicos:** Necessidades especiais de rega, poda, adubação ou controle de pragas.
  - **Restrições de plantio:** Distância mínima recomendada de construções, redes subterrâneas, etc.

**Justificativa da Estrutura:**

A divisão da rede neural em sub-redes menores oferece diversas vantagens:

- **Modularidade:** Permite um desenvolvimento e manutenção mais fáceis do modelo, pois cada sub-rede pode ser trabalhada de forma independente.
- **Especialização:** Cada sub-rede se concentra em um aspecto específico do problema, o que pode levar a um melhor desempenho geral.
