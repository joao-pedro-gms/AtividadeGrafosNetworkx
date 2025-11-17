"""
Testes para o módulo de rede logística.
"""

import unittest
import networkx as nx
from rede_logistica import RedeLogistica


class TestRedeLogistica(unittest.TestCase):
    """Testes para a classe RedeLogistica."""
    
    def setUp(self):
        """Configura uma rede para cada teste."""
        self.rede = RedeLogistica()
    
    def test_criacao_rede(self):
        """Testa se a rede é criada corretamente."""
        # Verificar número de nós
        self.assertEqual(self.rede.G.number_of_nodes(), 7)
        
        # Verificar número de arestas
        self.assertEqual(self.rede.G.number_of_edges(), 10)
    
    def test_tipos_nos(self):
        """Testa se os tipos de nós estão corretos."""
        # Verificar depósito
        self.assertEqual(self.rede.G.nodes['Depósito']['tipo'], 'depósito')
        
        # Verificar clientes
        self.assertEqual(self.rede.G.nodes['Cliente_A']['tipo'], 'cliente')
        self.assertEqual(self.rede.G.nodes['Cliente_B']['tipo'], 'cliente')
        self.assertEqual(self.rede.G.nodes['Cliente_C']['tipo'], 'cliente')
        
        # Verificar cruzamentos
        self.assertEqual(self.rede.G.nodes['Cruzamento_1']['tipo'], 'cruzamento')
    
    def test_pesos_arestas(self):
        """Testa se os pesos das arestas existem."""
        # Verificar se todas as arestas têm peso
        for u, v, data in self.rede.G.edges(data=True):
            self.assertIn('weight', data)
            self.assertIsInstance(data['weight'], (int, float))
            self.assertGreater(data['weight'], 0)
    
    def test_caminho_minimo(self):
        """Testa o cálculo de caminho mínimo."""
        # Testar caminho do Depósito para Cliente_A
        caminho, custo = self.rede.calcular_caminho_minimo('Depósito', 'Cliente_A')
        
        self.assertIsNotNone(caminho)
        self.assertIsInstance(caminho, list)
        self.assertEqual(caminho[0], 'Depósito')
        self.assertEqual(caminho[-1], 'Cliente_A')
        self.assertIsInstance(custo, (int, float))
        self.assertGreater(custo, 0)
    
    def test_rotas_otimizadas(self):
        """Testa a otimização de rotas para todos os clientes."""
        rotas = self.rede.otimizar_rotas_entrega()
        
        # Verificar se há rotas para todos os clientes
        self.assertEqual(len(rotas), 3)
        self.assertIn('Cliente_A', rotas)
        self.assertIn('Cliente_B', rotas)
        self.assertIn('Cliente_C', rotas)
        
        # Verificar estrutura das rotas
        for cliente, info in rotas.items():
            self.assertIn('caminho', info)
            self.assertIn('custo', info)
            self.assertEqual(info['caminho'][0], 'Depósito')
            self.assertEqual(info['caminho'][-1], cliente)
    
    def test_pontos_criticos(self):
        """Testa a identificação de pontos críticos."""
        criticos = self.rede.identificar_pontos_criticos()
        
        # Verificar estrutura do resultado
        self.assertIn('pontos_articulacao', criticos)
        self.assertIn('pontes', criticos)
        
        # Verificar tipos
        self.assertIsInstance(criticos['pontos_articulacao'], list)
        self.assertIsInstance(criticos['pontes'], list)
    
    def test_centralidade(self):
        """Testa o cálculo de centralidade."""
        centralidade = self.rede.calcular_centralidade()
        
        # Verificar se há centralidade para todos os nós
        self.assertEqual(len(centralidade), self.rede.G.number_of_nodes())
        
        # Verificar se os valores estão no intervalo [0, 1]
        for no, valor in centralidade.items():
            self.assertGreaterEqual(valor, 0)
            self.assertLessEqual(valor, 1)
    
    def test_conectividade(self):
        """Testa se o grafo é conexo."""
        # Verificar se todos os nós são alcançáveis
        self.assertTrue(nx.is_connected(self.rede.G))
    
    def test_relatorio(self):
        """Testa a geração de relatório."""
        relatorio = self.rede.gerar_relatorio()
        
        # Verificar se o relatório não está vazio
        self.assertIsInstance(relatorio, str)
        self.assertGreater(len(relatorio), 0)
        
        # Verificar se contém informações importantes
        self.assertIn('RELATÓRIO', relatorio)
        self.assertIn('ROTAS OTIMIZADAS', relatorio)
        self.assertIn('PONTOS CRÍTICOS', relatorio)
        self.assertIn('Cliente_A', relatorio)
        self.assertIn('Cliente_B', relatorio)
        self.assertIn('Cliente_C', relatorio)


if __name__ == '__main__':
    unittest.main()
