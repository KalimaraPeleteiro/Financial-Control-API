from RevenueExpenseControl.models import *
from RevenueExpenseControl.serializers import *
from rest_framework import viewsets, generics


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
	def get_queryset(self):
		queryset = Receita.objects.filter(id = self.kwargs['pk'])
		return queryset
	serializer_class = ReceitasSerializer


class DespesaEspecificaViewSet(generics.ListAPIView):
	def get_queryset(self):
		queryset = Despesa.objects.filter(id = self.kwargs['pk'])
		return queryset
	serializer_class = DespesasSerializer