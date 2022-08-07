from django.test import TestCase
from RevenueExpenseControl.models import Despesa, Receita


class ReceitaTestCase(TestCase):
    
    def setUp(self):
        self.example = Receita(descricao = "Receita Teste", 
                               valor = 1000, 
                               data = "2003-02-09")
    
    def test_verifica_campos(self):
        """Teste que verifica se os campos do modelo estão recebendo corretamente os dados"""
        self.assertEqual(self.example.descricao, "Receita Teste")
        self.assertEqual(self.example.valor, 1000)
        self.assertEqual(self.example.data, "2003-02-09")


class DespesaTestCase(TestCase):
    def setUp(self):
        self.example = Despesa(descricao = "Despesa Teste", 
                               valor = 1000, 
                               data = "2003-02-09",
                               categoria = 'A')
        self.default = Despesa(descricao = "Despesa Teste02", 
                               valor = 2000, 
                               data = "2003-02-09")
    
    def test_verifica_campos(self):
        """Teste que verifica se os campos do modelo estão recebendo corretamente os dados"""
        self.assertEqual(self.example.descricao, "Despesa Teste")
        self.assertEqual(self.example.valor, 1000)
        self.assertEqual(self.example.data, "2003-02-09")
        self.assertEqual(self.example.categoria, "A")
    
    def test_verificar_valor_default(self):
        """Teste que verifica se o valor default é escolhido em caso de omissão de categoria"""
        self.assertEqual(self.default.categoria, 'O')
