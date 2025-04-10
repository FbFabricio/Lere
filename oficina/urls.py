from django.urls import path
from . import views

urlpatterns = [
    #path('historico',),
    path('contatos/', views.contatos, name='lista_de_clientes'),
    path('cadastro/', views.cadastro_cliente, name='cadastro_clientes'),
    path('historico/', views.historico, name='historico_clientes'),
    ]