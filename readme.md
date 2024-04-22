## **Escolha Ideal de Árvores para Plantio 🌳🌿**

**Descrição do Problema:**

A escolha da árvore ideal para plantar pode ser um desafio complexo, pois depende de diversos fatores como **clima, condições locais e capacidade de manutenção**. Este modelo de rede neural, visa auxiliar na tomada de decisão sobre qual árvore é mais adequada para cada situação, levando em consideração esses três aspectos.

**Estrutura da Rede:**

A rede neural é composta por quatro sub-redes interligadas: [Desenho das Redes](https://whimsical.com/redes-neurais-arvores-UEz9q62GnM1Rrs1PjFmFNA@6HYTAunKLgTV49MPDN8N5HaGmfqjrBQNp8mUEnN1yba8hfi) ✍

## **Sub-rede Neural "Clima" ☀️🌧️❄️💨**

**Objetivo:** Identificar o clima com base nas características climáticas informadas.

**Entradas:**

- **Temperatura:** Temperatura média anual.
- **Pluviosidade:** Precipitação anual média.
- **Umidade:** Umidade relativa do ar média.
- **Vento:** Velocidade média do vento.
- **Neve:** Frequência média de neve.
- **Neblina:** Frequência média de neblina.
- **Tempestades:** Incidência média de tempestades.

**Saída:**

- **Clima:** O clima que se adequar com as entradas especificadas. Exemplo: Clima Temperado Úmido.

## **Sub-rede Neural "Condição Local" 🏞️**

**Objetivo:** Definir a qualidade do local de plantio.

**Entradas:**

- **Altitude:** Qual a altitude disponível para o crescimento da árvore (Baixa, Média, Alta).
- **Espaço:** Qual o espaço ao redor disponível para o crescimento da árvore (Pequeno, Médio, Grande).
- **Solo:** Tipo de solo (argiloso, arenoso, limoso).
- **Relevo:** Características do relevo (plano, encosta, vale).
- **Drenagem:** Qual o nível de drenagem do solo (Boa, Moderada, Ruim).
- **Clima:** Qual o clima retornado na Sub-rede neural Clima (Clima Seco, Clima Subtropical Úmido, Clima Temperado...).

**Saída:**

- **Nível de condição local,** entre 1 a 7. (_Nível 1 - Ótimas Condições para Plantio, Nível 7 - Condições Impróprias para Plantio_).

## **Sub-rede Neural "Capacidade de Manutenção" 🛠️**

**Objetivo:** Definir a capacidade de manutenção do usuário.

**Entradas:**

- **Experiência:** Você já teve alguma experiência com o cuidado de árvores? (Sim ou Não).
- **Dedicação:** Você tem tempo disponível para dedicar aos cuidados básicos com a árvore, como regar, adubar e podar? (Sim ou Não).
- **Aptidão:** Você se sente confortável realizando tarefas físicas como regar, adubar e podar a árvore? (Sim ou Não).
- **Disposição:** Você está disposto a aprender sobre os cuidados específicos com a espécie de árvore que deseja plantar? (Sim ou Não).
- **Acesso a Ferramentas:** Você tem acesso a ferramentas e equipamentos básicos para o cuidado da árvore, como mangueira, regador, pá, podador, etc.? (Sim ou Não).
- **Contratar profissional:** Você está disposto a contratar um profissional para cuidar da árvore, caso não tenha tempo ou condições de fazê-lo sozinho? (Sim ou Não).
- **Clima:** Qual o clima retornado na Sub-rede neural Clima (Clima Seco, Clima Subtropical Úmido, Clima Temperado...).
- **Condição Local:** Nível de Condição Local retornado na Sub-rede neural Condição Local (Nível 1 - Ótimas Condições para Plantio, Nível 7 - Condições Impróprias para Plantio...).

**Saída:**

- **Nível de condição de manutenção do indivíduo,** entre 1 a 7. (_Nível 1 - Excelente Manutenção, Nível 7 - Manutenção Deficiente_).

## **Sub-rede Neural "Características" 🌱**

**Objetivo:** Receber características específicas e retornar a árvore que mais se adeque a todas as demais entradas (**Clima, nível de condição local e nível de condição de manutenção**).

**Entradas:**

- **Tempo de Maturidade:** Quanto tempo você está disposto a esperar para que a árvore atinja a maturidade? (Rápido, Moderado, Lento).
- **Tipo de Copa:** Qual o tipo de copa desejado? (Compacta, Arredondada, Cônica, Colunar ou Irregular).
- **Flores:** Você deseja que a árvore tenha flores? (Sim ou Não).
- **Frutos:** Você deseja que a árvore tenha frutos? (Sim ou Não).
- **Clima:** Qual o clima retornado na Sub-rede neural Clima (Clima Seco, Clima Subtropical Úmido, Clima Temperado...).
- **Condição Local:** Nível de Condição Local retornado na Sub-rede neural Condição Local (Nível 1 - Ótimas Condições para Plantio, Nível 7 - Condições Impróprias para Plantio...).
- **Capacidade de Manutenção:** Nível de Capacidade de Manutenção retornado na Sub-rede neural Capacidade de Manutenção (Nível 1 - Excelente Manutenção, Nível 7 - Manutenção Deficiente...).

**Saídas:**

- **Características da Árvore:** Características da árvore, incluindo:
  - **Altura:** Altura madura média.
  - **Taxa de crescimento:** Lento, moderado, rápido.
  - **Copa:** Colunar, arredondada, oval, etc.
  - **Flores:** Descrição da floração (cor, época, duração).
  - **Frutos:** Descrição dos frutos (comestíveis, ornamentais, atrativos para a fauna).
  - **Cuidados específicos:** Necessidades especiais de rega, poda, adubação ou controle de pragas.
  - **Restrições de plantio:** Distância mínima recomendada de construções, redes subterrâneas, etc.
  - **Usos:** Principais usos como: Ornamental, forrageira, medicinal.
  - **Observações:** Observações adicionais relevantes sobre a árvore.

**Justificativa da Estrutura:**

A divisão da rede neural em sub-redes menores oferece diversas vantagens:

- **Modularidade:** Permite um desenvolvimento e manutenção mais fáceis do modelo, pois cada sub-rede pode ser trabalhada de forma independente.
- **Especialização:** Cada sub-rede se concentra em um aspecto específico do problema, o que pode levar a um melhor desempenho geral.
