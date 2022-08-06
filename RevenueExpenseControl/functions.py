from re import S
from RevenueExpenseControl.models import *

def search_description(model, descricao):
    if descricao is not None:
        queryset = []
        for object in model.objects.all():
            if descricao in object.descricao:
                queryset.append(object)
        return queryset
    else:
        return model.objects.all()


def search_data(model, year, month):
    queryset = []
    for object in model.objects.all():
        if object.data.year == year and object.data.month == month:
            queryset.append(object)
    
    return queryset


def create_resume(year, month):
    valor_total_despesas = 0
    valor_total_receitas = 0
    dicionario_categorias = {
        'A': 0,'S': 0,'M': 0,
        'T': 0,'E': 0,'L': 0,
        'I': 0,'O': 0
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

    return  valor_total_despesas, valor_total_receitas, dicionario_categorias