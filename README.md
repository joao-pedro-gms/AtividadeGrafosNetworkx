# AtividadeGrafosNetworkx

## Objetivo

O presente exercício propõe a modelagem e análise de uma rede logística simplificada. O objetivo é aplicar conceitos da Teoria dos Grafos para solucionar problemas práticos de otimização de rotas e identificação de pontos críticos na rede, utilizando a biblioteca NetworkX em Python.

## Cenário do Problema

Uma empresa de distribuição necessita otimizar suas rotas de entrega. A rede é composta por um Depósito central, Clientes (A, B, C) e Cruzamentos (interseções) que conectam as vias.

### Componentes da Rede

- **Nós (Nodes)**: Representam as localidades (Depósito, Clientes, Cruzamentos)
- **Arestas (Edges)**: Representam as vias (ruas)
- **Peso (Weight)**: Atributo da aresta que representa o custo de deslocamento (tempo médio em minutos) entre dois nós

## Estrutura do Projeto

```
AtividadeGrafosNetworkx/
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências do projeto
├── rede_logistica.py           # Implementação principal
└── test_rede_logistica.py      # Testes unitários
```

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalando Dependências

```bash
pip install -r requirements.txt
```

As dependências incluem:
- `networkx`: Biblioteca para criação e análise de grafos
- `matplotlib`: Biblioteca para visualização de grafos

## Uso

### Executar o Programa Principal

```bash
python rede_logistica.py
```

Este comando irá:
1. Criar a rede logística
2. Gerar um relatório completo com análises
3. Visualizar a rede com o caminho otimizado para o Cliente A
4. Salvar a visualização em `rede_logistica.png`

### Executar os Testes

```bash
python -m unittest test_rede_logistica.py
```

ou

```bash
python test_rede_logistica.py
```

## Funcionalidades Implementadas

### 1. Modelagem da Rede

A rede logística é representada como um grafo não-direcionado com:
- 1 Depósito (ponto central)
- 3 Clientes (A, B, C)
- 3 Cruzamentos (C1, C2, C3)
- 10 conexões ponderadas (vias com tempo de deslocamento)

### 2. Otimização de Rotas

Utiliza o algoritmo de Dijkstra para calcular:
- Caminho mais curto do Depósito para cada cliente
- Tempo total de deslocamento para cada rota

### 3. Identificação de Pontos Críticos

Analisa a rede para identificar:
- **Pontos de Articulação**: Nós cuja remoção desconecta o grafo
- **Pontes**: Arestas cuja remoção desconecta o grafo

### 4. Análise de Centralidade

Calcula a centralidade de intermediação (betweenness centrality) para:
- Identificar nós mais importantes para o fluxo da rede
- Avaliar quais locais têm maior impacto na conectividade

### 5. Visualização

Gera visualização gráfica da rede com:
- Cores diferentes para tipos de nós (Depósito, Clientes, Cruzamentos)
- Pesos das arestas (tempo em minutos)
- Destaque para rotas otimizadas
- Legenda explicativa

## Exemplo de Saída

```
======================================================================
RELATÓRIO DE ANÁLISE DA REDE LOGÍSTICA
======================================================================

Número de nós: 7
Número de arestas: 10

----------------------------------------------------------------------
ROTAS OTIMIZADAS DE ENTREGA
----------------------------------------------------------------------

Cliente_A:
  Caminho: Depósito → Cruzamento_1 → Cliente_A
  Tempo total: 9 minutos

Cliente_B:
  Caminho: Depósito → Cruzamento_1 → Cruzamento_3 → Cliente_B
  Tempo total: 11 minutos

Cliente_C:
  Caminho: Depósito → Cruzamento_1 → Cruzamento_3 → Cliente_C
  Tempo total: 13 minutos

----------------------------------------------------------------------
PONTOS CRÍTICOS DA REDE
----------------------------------------------------------------------

Pontos de Articulação (nós críticos):
  - Cruzamento_1
  - Cruzamento_3

Pontes (arestas críticas):
  - Depósito ↔ Cruzamento_1
  - Cruzamento_1 ↔ Cliente_A
  - Cruzamento_3 ↔ Cliente_C

----------------------------------------------------------------------
CENTRALIDADE DOS NÓS (Importância no Fluxo)
----------------------------------------------------------------------
  Cruzamento_3: 0.4667
  Cruzamento_1: 0.4000
  ...
======================================================================
```

## Conceitos de Teoria dos Grafos Aplicados

1. **Grafos Ponderados**: Uso de pesos nas arestas para representar custos
2. **Algoritmo de Dijkstra**: Cálculo de caminhos mínimos
3. **Pontos de Articulação**: Análise de vulnerabilidade da rede
4. **Pontes**: Identificação de conexões críticas
5. **Centralidade de Intermediação**: Análise de importância dos nós
6. **Conectividade**: Verificação de alcançabilidade na rede

## Possíveis Extensões

- Adicionar mais clientes e cruzamentos
- Implementar rotas multi-destino (Problema do Caixeiro Viajante)
- Adicionar restrições de capacidade
- Modelar tráfego dinâmico (pesos variáveis)
- Implementar algoritmos de fluxo máximo

## Licença

Este projeto foi desenvolvido para fins educacionais.

## Autor

Desenvolvido como exercício prático de Teoria dos Grafos usando NetworkX.
