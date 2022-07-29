from RevenueExpenseControl.models import *
from RevenueExpenseControl.serializers import *
from rest_framework import viewsets, generics


class ReceitasViewSet(viewsets.ModelViewSet):
	queryset = Receita.objects.all()
	serializer_class = ReceitasSerializer

class DespesasViewSet(viewsets.ModelViewSet):
	queryset = Despesa.objects.all()
	serializer_class = DespesasSerializer

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