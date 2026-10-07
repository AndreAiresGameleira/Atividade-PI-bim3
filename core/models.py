from django.db import models


class Automovel(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10)
    valor_diaria = models.DecimalField(max_digits=8, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} - {self.placa}'


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Locacao(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE
    )

    automovel = models.ForeignKey(
        Automovel,
        on_delete=models.CASCADE
    )

    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.cliente} - {self.automovel}'