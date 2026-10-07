from django.urls import path
from . import views


urlpatterns = [
    path('',views.lista_automoveis,name='lista_automoveis'),
    path('automoveis/novo/',views.criar_automovel,name='criar_automovel'),
    path('automoveis/editar/<int:pk>/',views.editar_automovel,name='editar_automovel'),
    path('automoveis/excluir/<int:pk>/',views.excluir_automovel,name='excluir_automovel'),

    path('clientes/',views.lista_clientes,name='lista_clientes'),
    path('clientes/novo/',views.criar_cliente,name='criar_cliente'),
    path('clientes/editar/<int:pk>/',views.editar_cliente,name='editar_cliente'),
    path('clientes/excluir/<int:pk>/',views.excluir_cliente,name='excluir_cliente'),

    path('locacoes/',views.lista_locacoes,name='lista_locacoes'),
    path('locacoes/nova/',views.criar_locacao,name='criar_locacao'),
    path('locacoes/editar/<int:pk>/',views.editar_locacao,name='editar_locacao'),
    path('locacoes/excluir/<int:pk>/',views.excluir_locacao,name='excluir_locacao'),
]