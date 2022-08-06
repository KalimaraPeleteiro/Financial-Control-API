from rest_framework import serializers
from RevenueExpenseControl.models import *


class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'
    
    def validate(self, data):
        query = Receita.objects.filter(descricao = data['descricao'])
        for object in query:
            if object.data.month == data['data'].month:
                raise serializers.ValidationError({'descricao': "Uma receita com essa descrição já foi registrada esse mês."})
        return data


class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'
    
    def validate(self, data):
        query = Despesa.objects.filter(descricao = data['descricao'])
        for object in query:
            if object.data.month == data['data'].month:
                raise serializers.ValidationError({'descricao': "Uma despesa com essa descrição já foi registrada esse mês."})
        return data
