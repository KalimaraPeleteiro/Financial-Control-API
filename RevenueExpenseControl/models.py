from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=2000)
    valor = models.DecimalField(blank=False, decimal_places=2, max_digits=100)
    data = models.DateField()

class Despesa(models.Model):
    descricao = models.CharField(max_length=2000)
    valor = models.DecimalField(blank=False, decimal_places=2, max_digits=100)
    data = models.DateField()
