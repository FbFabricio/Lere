from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    
    path('contatos/', views.contatos , name='lista_de_clientes'),

    path('cadastro/', views.cadastro_cliente , name='cadastro_clientes'),

    path('login/contatos/', views.contatos , name='clientes'),

    path('cliente/<int:cliente_id>/' , views.detalhes_clientes , name='detalhes'),
    
    path('cliente/<int:cliente_id>/editar/', views.editar_cliente , name='editar'),

    path('clientes/<int:cliente_id>/remover/', views.remover_cliente, name='remover_cliente'),

  

    ]

