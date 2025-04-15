from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import Cliente
from .forms import LoginForm, ClienteForm

# Create your views here.


# @login_required
def contatos(request):

    ''' Mostra todos os clientes registratos em uma lista '''
    
    clientes = Cliente.objects.all()
    return render(request,'oficina/lista_contatos.html', {'clientes': clientes})


def login_view(request): 
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # faz o login do usuário
                return redirect('')  # eedireciona para a página desejada após login
            else:
                form.add_error(None, 'Usuário ou senha inválidos')  # Erro genérico
    else:
        form = LoginForm()  # Exibe o formulário vazio para GET

    return render(request, 'oficina/login.html', {'form': form})

# # @login_required
# def cadastro(request):

#     '''Tela de cadastro de cliente'''

#     if request.method == 'POST':
#         nome = request.POST.get('nome')
#         carro = request.POST.get('carro')
#         placa = request.POST.get('placa')

#         # Criar e salvar no banco de dados
#         Cliente.objects.create(nome=nome, carro=carro, placa=placa)

#         return redirect()  # Redireciona para a lista de veículos

#     return render(request, 'oficina/cadastro.html')


# @login_required
def historico(request):

    '''Historico de clientes(mostra serviços passados)'''

    historico = Cliente.objects.all()
    return render(request, 'oficina/historico.html', {'historico': historico})


def cadastro_cliente(request):
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()  # <- Aqui ele salva no banco
            return redirect('lista_de_clientes')  
    else:
        form = ClienteForm()
    
    return render(request, 'oficina/cadastro.html', {'form': form})



def detalhes_clientes(request,cliente_id):

    '''Tela com dados dos clientes detalhas'''

    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'oficina/clientes.html', {'cliente': cliente})


def editar_cliente(request, cliente_id):

    '''Edita os dados do cliente'''


    cliente = get_object_or_404(Cliente, id=cliente_id)  # pega o cliente do banco

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)  # passa a instância
        if form.is_valid():
            form.save()  # isso atualiza o registro existente
            return redirect('lista_de_clientes')
    else:
        form = ClienteForm(instance=cliente)  # pré-preenche com os dados atuais

    return render(request, 'oficina/editar.html', {'form': form, 'cliente': cliente})


def remover_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return redirect('lista_de_clientes')

def buscar_clientes(request):
    q = request.GET.get('q', '')
    clientes = Cliente.objects.filter(nome__icontains=q).values('id', 'nome')[:5]
    return JsonResponse(list(clientes), safe=False)

