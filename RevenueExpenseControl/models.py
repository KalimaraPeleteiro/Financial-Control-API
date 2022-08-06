from django.db import models


class Receita(models.Model):
    descricao = models.CharField(max_length=2000)
    valor = models.DecimalField(blank=False, decimal_places=2, max_digits=100)
    data = models.DateField()


class Despesa(models.Model):

    CATEGORIAS = (
        ('A', 'Alimentação'),
        ('S', 'Saúde'),
        ('M', 'Moradia'),
        ('T', 'Transporte'),
        ('E', 'Educação'),
        ('L', 'Lazer'),
        ('I', 'Imprevistos'),
        ('O', 'Outras') 
    )

    descricao = models.CharField(max_length=2000)
    valor = models.DecimalField(blank=False, decimal_places=2, max_digits=100)
    data = models.DateField()
    categoria = models.CharField(max_length = 1, choices = CATEGORIAS, 
                                 blank = False, null = False, default = 'O')
