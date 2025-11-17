"""
Rede Logística - Análise de Grafos
Modelagem e análise de uma rede logística simplificada usando NetworkX.

Este módulo implementa uma rede de distribuição com:
- Depósito central
- Clientes (A, B, C)
- Cruzamentos (interseções)
- Análise de rotas otimizadas
- Identificação de pontos críticos
"""

import networkx as nx
import matplotlib.pyplot as plt


class RedeLogistica:
    """
    Classe que representa uma rede logística de distribuição.
    
    A rede é modelada como um grafo onde:
    - Nós representam localidades (Depósito, Clientes, Cruzamentos)
    - Arestas representam vias (ruas)
    - Pesos representam custos de deslocamento (tempo em minutos)
    """
    
    def __init__(self):
        """Inicializa o grafo da rede logística."""
        self.G = nx.Graph()
        self._construir_rede()
    
    def _construir_rede(self):
        """
        Constrói a rede logística com nós e arestas ponderadas.
        
        Estrutura da rede:
        - Depósito: ponto central de distribuição
        - Clientes: A, B, C (destinos de entrega)
        - Cruzamentos: C1, C2, C3 (interseções de vias)
        """
        # Adicionar nós com tipos
        self.G.add_node('Depósito', tipo='depósito')
        self.G.add_node('Cliente_A', tipo='cliente')
        self.G.add_node('Cliente_B', tipo='cliente')
        self.G.add_node('Cliente_C', tipo='cliente')
        self.G.add_node('Cruzamento_1', tipo='cruzamento')
        self.G.add_node('Cruzamento_2', tipo='cruzamento')
        self.G.add_node('Cruzamento_3', tipo='cruzamento')
        
        # Adicionar arestas com pesos (tempo em minutos)
        arestas = [
            ('Depósito', 'Cruzamento_1', 5),
            ('Depósito', 'Cruzamento_2', 7),
            ('Cruzamento_1', 'Cruzamento_3', 3),
            ('Cruzamento_1', 'Cliente_A', 4),
            ('Cruzamento_2', 'Cruzamento_3', 4),
            ('Cruzamento_2', 'Cliente_B', 6),
            ('Cruzamento_3', 'Cliente_A', 2),
            ('Cruzamento_3', 'Cliente_B', 3),
            ('Cruzamento_3', 'Cliente_C', 5),
            ('Cliente_A', 'Cliente_B', 8),
        ]
        
        for origem, destino, peso in arestas:
            self.G.add_edge(origem, destino, weight=peso)
    
    def calcular_caminho_minimo(self, origem, destino):
        """
        Calcula o caminho mais curto entre dois nós usando algoritmo de Dijkstra.
        
        Args:
            origem (str): Nó de origem
            destino (str): Nó de destino
            
        Returns:
            tuple: (caminho, custo_total)
                - caminho: lista de nós no caminho
                - custo_total: tempo total em minutos
        """
        try:
            caminho = nx.shortest_path(self.G, origem, destino, weight='weight')
            custo = nx.shortest_path_length(self.G, origem, destino, weight='weight')
            return caminho, custo
        except nx.NetworkXNoPath:
            return None, float('inf')
    
    def otimizar_rotas_entrega(self):
        """
        Calcula as rotas otimizadas do Depósito para todos os clientes.
        
        Returns:
            dict: Dicionário com rotas otimizadas para cada cliente
                  {cliente: {'caminho': [...], 'custo': valor}}
        """
        rotas = {}
        clientes = ['Cliente_A', 'Cliente_B', 'Cliente_C']
        
        for cliente in clientes:
            caminho, custo = self.calcular_caminho_minimo('Depósito', cliente)
            rotas[cliente] = {
                'caminho': caminho,
                'custo': custo
            }
        
        return rotas
    
    def identificar_pontos_criticos(self):
        """
        Identifica pontos críticos na rede:
        - Pontos de articulação: nós cuja remoção desconecta o grafo
        - Pontes: arestas cuja remoção desconecta o grafo
        
        Returns:
            dict: {'pontos_articulacao': [...], 'pontes': [...]}
        """
        pontos_articulacao = list(nx.articulation_points(self.G))
        pontes = list(nx.bridges(self.G))
        
        return {
            'pontos_articulacao': pontos_articulacao,
            'pontes': pontes
        }
    
    def calcular_centralidade(self):
        """
        Calcula a centralidade de intermediação (betweenness centrality) dos nós.
        
        A centralidade indica quais nós são mais importantes para o fluxo da rede.
        
        Returns:
            dict: Dicionário com centralidade de cada nó
        """
        return nx.betweenness_centrality(self.G, weight='weight')
    
    def visualizar_rede(self, destacar_caminho=None, salvar_arquivo=None):
        """
        Visualiza a rede logística usando matplotlib.
        
        Args:
            destacar_caminho (list, optional): Caminho a ser destacado
            salvar_arquivo (str, optional): Nome do arquivo para salvar a figura
        """
        plt.figure(figsize=(12, 8))
        
        # Layout do grafo
        pos = nx.spring_layout(self.G, seed=42, k=2)
        
        # Separar nós por tipo
        deposito = [n for n, d in self.G.nodes(data=True) if d['tipo'] == 'depósito']
        clientes = [n for n, d in self.G.nodes(data=True) if d['tipo'] == 'cliente']
        cruzamentos = [n for n, d in self.G.nodes(data=True) if d['tipo'] == 'cruzamento']
        
        # Desenhar nós
        nx.draw_networkx_nodes(self.G, pos, nodelist=deposito, 
                               node_color='red', node_size=1000, 
                               label='Depósito', alpha=0.9)
        nx.draw_networkx_nodes(self.G, pos, nodelist=clientes, 
                               node_color='green', node_size=800, 
                               label='Clientes', alpha=0.9)
        nx.draw_networkx_nodes(self.G, pos, nodelist=cruzamentos, 
                               node_color='lightblue', node_size=600, 
                               label='Cruzamentos', alpha=0.9)
        
        # Desenhar arestas
        nx.draw_networkx_edges(self.G, pos, width=2, alpha=0.5)
        
        # Destacar caminho se fornecido
        if destacar_caminho:
            path_edges = list(zip(destacar_caminho, destacar_caminho[1:]))
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, 
                                   edge_color='red', width=4, alpha=0.8)
        
        # Adicionar rótulos
        nx.draw_networkx_labels(self.G, pos, font_size=10, font_weight='bold')
        
        # Adicionar pesos das arestas
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        edge_labels = {k: f'{v} min' for k, v in edge_labels.items()}
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels, font_size=8)
        
        plt.title('Rede Logística de Distribuição', fontsize=16, fontweight='bold')
        plt.legend(loc='upper left')
        plt.axis('off')
        plt.tight_layout()
        
        if salvar_arquivo:
            plt.savefig(salvar_arquivo, dpi=300, bbox_inches='tight')
            print(f"Figura salva em: {salvar_arquivo}")
        
        plt.show()
    
    def gerar_relatorio(self):
        """
        Gera um relatório completo da análise da rede logística.
        
        Returns:
            str: Relatório formatado
        """
        relatorio = []
        relatorio.append("=" * 70)
        relatorio.append("RELATÓRIO DE ANÁLISE DA REDE LOGÍSTICA")
        relatorio.append("=" * 70)
        relatorio.append("")
        
        # Informações básicas
        relatorio.append(f"Número de nós: {self.G.number_of_nodes()}")
        relatorio.append(f"Número de arestas: {self.G.number_of_edges()}")
        relatorio.append("")
        
        # Rotas otimizadas
        relatorio.append("-" * 70)
        relatorio.append("ROTAS OTIMIZADAS DE ENTREGA")
        relatorio.append("-" * 70)
        rotas = self.otimizar_rotas_entrega()
        for cliente, info in rotas.items():
            relatorio.append(f"\n{cliente}:")
            relatorio.append(f"  Caminho: {' → '.join(info['caminho'])}")
            relatorio.append(f"  Tempo total: {info['custo']} minutos")
        relatorio.append("")
        
        # Pontos críticos
        relatorio.append("-" * 70)
        relatorio.append("PONTOS CRÍTICOS DA REDE")
        relatorio.append("-" * 70)
        criticos = self.identificar_pontos_criticos()
        relatorio.append(f"\nPontos de Articulação (nós críticos):")
        if criticos['pontos_articulacao']:
            for ponto in criticos['pontos_articulacao']:
                relatorio.append(f"  - {ponto}")
        else:
            relatorio.append("  Nenhum ponto de articulação encontrado")
        
        relatorio.append(f"\nPontes (arestas críticas):")
        if criticos['pontes']:
            for ponte in criticos['pontes']:
                relatorio.append(f"  - {ponte[0]} ↔ {ponte[1]}")
        else:
            relatorio.append("  Nenhuma ponte encontrada")
        relatorio.append("")
        
        # Centralidade
        relatorio.append("-" * 70)
        relatorio.append("CENTRALIDADE DOS NÓS (Importância no Fluxo)")
        relatorio.append("-" * 70)
        centralidade = self.calcular_centralidade()
        centralidade_ordenada = sorted(centralidade.items(), 
                                       key=lambda x: x[1], reverse=True)
        for no, valor in centralidade_ordenada:
            relatorio.append(f"  {no}: {valor:.4f}")
        relatorio.append("")
        
        relatorio.append("=" * 70)
        
        return "\n".join(relatorio)


def main():
    """Função principal para demonstração do sistema."""
    print("Inicializando Rede Logística...\n")
    
    # Criar rede
    rede = RedeLogistica()
    
    # Gerar e exibir relatório
    print(rede.gerar_relatorio())
    
    # Exemplo: visualizar caminho otimizado para Cliente_A
    print("\nVisualizando caminho otimizado para Cliente_A...")
    caminho_a, custo_a = rede.calcular_caminho_minimo('Depósito', 'Cliente_A')
    print(f"Caminho: {' → '.join(caminho_a)}")
    print(f"Custo: {custo_a} minutos")
    
    # Visualizar a rede
    print("\nGerando visualização da rede...")
    rede.visualizar_rede(destacar_caminho=caminho_a, 
                         salvar_arquivo='rede_logistica.png')


if __name__ == '__main__':
    main()
