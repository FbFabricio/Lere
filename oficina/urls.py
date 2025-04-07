from django.urls import path
from . import views

urlpatterns = [
    #path('historico',),
    path('contatos/', views.contatos, name='lista_de_clientes'),
    path('cadastro/', views.cadastro, name='cadastro')
    ]