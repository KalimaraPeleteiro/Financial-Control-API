from django.test import TestCase
from RevenueExpenseControl.models import Receita, Despesa
from RevenueExpenseControl.serializers import ReceitasSerializer, DespesasSerializer


class ReceitasSerializerTestCase(TestCase):

    def setUp(self):
        self.example = Receita(descricao = "Receita Teste", 
                               valor = 1000, 
                               data = "2003-02-09")
        self.serializer = ReceitasSerializer(instance=self.example)

    def test_verificar_campos_serializados(self):
        """Teste que verifica quais campos foram serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['descricao', 'valor', 'data']))
    
    def test_verificar_conteudo_dos_campos(self):
        """Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['descricao'], "Receita Teste")
        self.assertEqual(float(data['valor']), 1000)
        self.assertEqual(data['data'], "2003-02-09")


class DespesasSerializerTestCase(TestCase):

    def setUp(self):
        self.example = Despesa(descricao = "Receita Teste", 
                               valor = 1000, 
                               data = "2003-02-09",
                               categoria = 'A')
        self.serializer = DespesasSerializer(instance=self.example)

    def test_verificar_campos_serializados(self):
        """Teste que verifica quais campos foram serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['descricao', 'valor', 'data', 'categoria']))
    
    def test_verificar_conteudo_dos_campos(self):
        """Teste que verifica o conteúdo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['descricao'], "Receita Teste")
        self.assertEqual(float(data['valor']), 1000)
        self.assertEqual(data['data'], "2003-02-09")
        self.assertEqual(data['categoria'], "A")
