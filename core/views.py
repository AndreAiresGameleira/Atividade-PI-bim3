from django.shortcuts import render, redirect, get_object_or_404

from .models import Automovel, Cliente, Locacao

from .forms import (
    AutomovelForm,
    ClienteForm,
    LocacaoForm
)

def lista_automoveis(request):
    automoveis = Automovel.objects.all()

    return render(
        request,
        'core/lista_automoveis.html',
        {'automoveis': automoveis}
    )

def criar_automovel(request):
    if request.method == 'POST':
        form = AutomovelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_automoveis')

    else:
        form = AutomovelForm()

    return render(
        request,
        'core/form_automovel.html',
        {'form': form}
    )

def editar_automovel(request, pk):
    automovel = get_object_or_404(
        Automovel,
        pk=pk
    )

    if request.method == 'POST':
        form = AutomovelForm(
            request.POST,
            instance=automovel
        )

        if form.is_valid():
            form.save()
            return redirect('lista_automoveis')

    else:
        form = AutomovelForm(
            instance=automovel
        )

    return render(
        request,
        'core/form_automovel.html',
        {'form': form}
    )

def excluir_automovel(request, pk):
    automovel = get_object_or_404(
        Automovel,
        pk=pk
    )

    if request.method == 'POST':
        automovel.delete()
        return redirect('lista_automoveis')

    return render(
        request,
        'core/excluir_automovel.html',
        {'automovel': automovel}
    )





def lista_clientes(request):
    clientes = Cliente.objects.all()

    return render(
        request,
        'core/lista_clientes.html',
        {'clientes': clientes}
    )

def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_clientes')

    else:
        form = ClienteForm()

    return render(
        request,
        'core/form_cliente.html',
        {'form': form}
    )

def editar_cliente(request, pk):
    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == 'POST':
        form = ClienteForm(
            request.POST,
            instance=cliente
        )

        if form.is_valid():
            form.save()
            return redirect('lista_clientes')

    else:
        form = ClienteForm(
            instance=cliente
        )

    return render(
        request,
        'core/form_cliente.html',
        {'form': form}
    )

def excluir_cliente(request, pk):
    cliente = get_object_or_404(
        Cliente,
        pk=pk
    )

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')

    return render(
        request,
        'core/excluir_cliente.html',
        {'cliente': cliente}
    )






def lista_locacoes(request):
    locacoes = Locacao.objects.all()

    return render(
        request,
        'core/lista_locacoes.html',
        {'locacoes': locacoes}
    )

def criar_locacao(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_locacoes')

    else:
        form = LocacaoForm()

    return render(
        request,
        'core/form_locacao.html',
        {'form': form}
    )

def editar_locacao(request, pk):
    locacao = get_object_or_404(
        Locacao,
        pk=pk
    )

    if request.method == 'POST':
        form = LocacaoForm(
            request.POST,
            instance=locacao
        )

        if form.is_valid():
            form.save()
            return redirect('lista_locacoes')

    else:
        form = LocacaoForm(
            instance=locacao
        )

    return render(
        request,
        'core/form_locacao.html',
        {'form': form}
    )

def excluir_locacao(request, pk):
    locacao = get_object_or_404(
        Locacao,
        pk=pk
    )

    if request.method == 'POST':
        locacao.delete()
        return redirect('lista_locacoes')

    return render(
        request,
        'core/excluir_locacao.html',
        {'locacao': locacao}
    )