from django import forms
from .models import Automovel, Cliente, Locacao


class AutomovelForm(forms.ModelForm):
    class Meta:
        model = Automovel
        fields = [
            'marca',
            'modelo',
            'ano',
            'placa',
            'valor_diaria',
            'disponivel'
        ]


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'cpf',
            'telefone',
            'email'
        ]


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = [
            'cliente',
            'automovel',
            'data_inicio',
            'data_fim',
            'valor_total'
        ]