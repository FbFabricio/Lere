from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Cliente
from .forms import LoginForm

# Create your views here.
@login_required
def contatos(request):
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
                login(request, user)  # Faz o login do usuário
                return redirect('contatos')  # Redireciona para a página desejada após login
            else:
                form.add_error(None, 'Usuário ou senha inválidos')  # Erro genérico
    else:
        form = LoginForm()  # Exibe o formulário vazio para GET

    return render(request, 'oficina/login.hmtl', {'form': form})

@login_required
def cadastro(request,HttpResponsePermantRedirect='contatos/'):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        carro = request.POST.get('carro')
        placa = request.POST.get('placa')

        # Criar e salvar no banco de dados
        Cliente.objects.create(nome=nome, carro=carro, placa=placa)

        return redirect(HttpResponsePermantRedirect)  # Redireciona para a lista de veículos

    return render(request, 'oficina/cadastro.html')


