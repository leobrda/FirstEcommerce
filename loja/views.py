from django.shortcuts import render
from .models import *


def homepage(request):
    banners = Banner.objects.filter(ativo=True)

    context = {
        'banners': banners,
    }

    return render(request, 'homepage.html', context=context)


def loja(request, nome_categoria=None):
    produtos = Produto.objects.filter(ativo=True)

    if nome_categoria:
        produtos = produtos.filter(categoria__nome=nome_categoria)

    context = {
        'produtos': produtos,
    }

    return render(request, 'loja.html', context=context)


def ver_produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)

    itens_estoque = ItemEstoque.objects.filter(produto=produto, quantidade__gt=0)

    context = {
        'produto': produto,
        'itens_estoque': itens_estoque,
    }

    return render(request, 'ver_produto.html', context=context)


def carrinho(request):
    return render(request, 'carrinho.html')


def checkout(request):
    return render(request, 'checkout.html')


def minha_conta(request):
    return render(request, 'usuario/minha_conta.html')


def login(request):
    return render(request, 'usuario/login.html')
