from RevenueExpenseControl.models import *
from RevenueExpenseControl.serializers import *
from RevenueExpenseControl.functions import *
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response


class ReceitasViewSet(viewsets.ModelViewSet):
	serializer_class = ReceitasSerializer

	def get_queryset(self):
		descricao = self.request.query_params.get('descricao')
		return search_description(Receita, descricao)


class DespesasViewSet(viewsets.ModelViewSet):
	serializer_class = DespesasSerializer
	
	def get_queryset(self):
		descricao = self.request.query_params.get('descricao')
		return search_description(Despesa, descricao)


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
		return search_data(Receita, self.kwargs['year'], self.kwargs['month'])


class DespesaMesViewSet(generics.ListAPIView):
	serializer_class = DespesasSerializer

	def get_queryset(self):
		return search_data(Despesa, self.kwargs['year'], self.kwargs['month'])


class ResumoViewSet(APIView):

	def get(self, request, year, month):

		despesa_total, receita_total, categorias = create_resume(year, month)

		data = {
				'Valor de Todas as Receitas do Mês': despesa_total,
				'Valor de Todas as Despesas do Mês': receita_total,
				'Despesa por Categoria': categorias,
				'Saldo Final do Mês': receita_total - despesa_total
			}

		return Response(data=data)