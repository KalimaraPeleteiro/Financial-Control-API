from RevenueExpenseControl.models import *
from RevenueExpenseControl.serializers import *
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response

class ReceitasViewSet(viewsets.ModelViewSet):
	serializer_class = ReceitasSerializer

	def get_queryset(self):
		queryset = Receita.objects.all()
		descricao = self.request.query_params.get('descricao')

		# Faz a Verificação da Busca
		if descricao is not None:
			new_queryset = []
			for receita in queryset:
				if descricao in receita.descricao:
					new_queryset.append(receita)
		
			return new_queryset
		else:
			return queryset


class DespesasViewSet(viewsets.ModelViewSet):
	serializer_class = DespesasSerializer
	
	def get_queryset(self):
		queryset = Despesa.objects.all()
		descricao = self.request.query_params.get('descricao')

		# Faz a Verificação da Busca
		if descricao is not None:
			new_queryset = []
			for despesa in queryset:
				if descricao in despesa.descricao:
					new_queryset.append(despesa)
		
			return new_queryset
		else:
			return queryset


class ReceitaEspecificaViewSet(generics.ListAPIView):
	serializer_class = ReceitasSerializer

	def get_queryset(self):
		queryset = Receita.objects.filter(id = self.kwargs['pk'])
		return queryset


class DespesaEspecificaViewSet(generics.ListAPIView):
	serializer_class = DespesasSerializer

	def get_queryset(self):
		queryset = Despesa.objects.filter(id = self.kwargs['pk'])
		return queryset


class ReceitaMesViewSet(generics.ListAPIView):
	serializer_class = ReceitasSerializer

	def get_queryset(self):
		queryset = []
		for object in Receita.objects.all():
			if object.data.year == self.kwargs['year'] and object.data.month == self.kwargs['month']:
				queryset.append(object)

		return queryset


class DespesaMesViewSet(generics.ListAPIView):
	serializer_class = DespesasSerializer

	def get_queryset(self):
		queryset = []
		for object in Despesa.objects.all():
			if object.data.year == self.kwargs['year'] and object.data.month == self.kwargs['month']:
				queryset.append(object)

		return queryset


class ResumoViewSet(APIView):

	def get(self, request, year, month):

		valor_total_despesas = 0
		valor_total_receitas = 0
		dicionario_categorias = {
			'A': 0,
        	'S': 0,
        	'M': 0,
        	'T': 0,
        	'E': 0,
        	'L': 0,
        	'I': 0,
        	'O': 0
		}

		for object in Despesa.objects.all():
			if object.data.year == year and object.data.month == month:
				valor_total_despesas += object.valor
				dicionario_categorias[object.categoria] += object.valor
		
		for object in Receita.objects.all():
			if object.data.year == year and object.data.month == month:
				valor_total_receitas += object.valor

		new_keys = ['Alimentação', 'Saúde', 'Moradia', 'Transporte',
					'Educação', 'Lazer', 'Imprevistos', 'Outros']
		dicionario_categorias = dict(zip(new_keys, dicionario_categorias.values()))

		data = {
				'Valor de Todas as Receitas do Mês': valor_total_receitas,
				'Valor de Todas as Despesas do Mês': valor_total_despesas,
				'Despesa por Categoria': dicionario_categorias,
				'Saldo Final do Mês': valor_total_receitas - valor_total_despesas
			}

		return Response(data=data)