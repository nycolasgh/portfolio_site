from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # para usar o sistema de usuários nativos...
from django.contrib.auth import authenticate, login, logout  # ...do django precisamos dessas importações
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import FeedbackForm

"""
clientes = [
    {'id': 1, 'name': 'Zézinho Biscoitero', 'feedback': 'Achei top demais'},
    {'id': 2, 'name': 'Carlinhos Açougueiro', 'feedback': 'Trabalho muito bom!'},
    {'id': 3, 'name': 'João Agiota Carlos', 'feedback': 'Profissionais muito confiáveis!'}
]
"""


# Create your views here.

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':  # Se o método da requisição for post
        username = request.POST.get('username')  # vamos atribuir a uma variável o valor da requisição com name igual a "username"
        password = request.POST.get('password')  # mesma coisa com a senha

        try:
            user = User.objects.get(username=username)  # vamos verificar se o nome deste usuário está no banco de dados
        except:  # se não estiver, vamos mostrar uma mensagem de erro, para isso vamos utilizar a função flash message do django
            messages.error(request, 'Usuário não existe.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    context = {'page': page}
    return render(request, 'core/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # commit=False para não salvar o form antes de tratarmos os dados
            user.username = user.username.lower()  # usamos o método lower() d
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ocorreu um erro durante o registro.')

    return render(request, 'core/login_register.html', {'form': form})


def home(request):
    clientes = Client.objects.all()
    trabalhos = RecentWork.objects.all()
    servicos = Service.objects.all()
    feedbacks = Feedbacks.objects.all()
    context = {'clients': clientes,
               'works': trabalhos,
               'service': servicos,
               'feedbacks': feedbacks}
    return render(request, 'core/home.html', context)


def userProfile(request, pk):
    context = {}
    return render(request, 'core/user_profile.html', context)


def clientDetails(request, pk):
    clientes = Client.objects.all()
    cliente = Client.objects.get(id=pk)
  # jobs = RecentWork.objects.filter(client_id=pk)  # outra opção seria como no ex abaixo (tem q testar)
    jobs = cliente.recentwork_set.all()  # utilizar nomedomodelchildren_set pra selecionar todos os itens do model childdren atrelados ao seu respectivo model parent
    services = Service.objects.all()
    context = {'cliente': cliente,
               'jobs': jobs,
               'services': services,
               'clientes': clientes
               }

    return render(request, 'core/clientdetails.html', context)


@login_required(login_url='login')  # colocamos o name da nossa url de login no parametro login_url...
def feedbackForm(request):  # ...caso o usuário não esteja logado, será redirecionado pra página de login
    fdbkform = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():  # is_valid() é um metodo do django para verificar se os itens do form estão corretos
            Feedbacks.objects.create(
                user=request.user,
                clientname=request.user.client.clientname,
                companyname=request.user.client.companyname,
                feedback=request.POST.get('feedback'),
            )
            return redirect('home')  # home é o name que atribuimos no path no arquivo urls.py

    context = {'form': fdbkform}
    return render(request, 'core/feedback_form.html', context)


@login_required(login_url='login')
def updateFeedback(request, pk):  # vamos precisar de uma primary key pra identificar qual feedback está sendo atualizado
    fdbk = Feedbacks.objects.get(id=pk)  # selecionamos o feedback através da pk
    fdbkform = FeedbackForm(instance=fdbk)  # para que os campos do form apareçam preenchidos com os dados antigos que serão editados.

    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=fdbk)  # esse se refere ao conteúdo editado
        if form.is_valid():  # is_valid() é um metodo do django para verificar se os itens do form estão corretos
            form.save()
            return redirect('home')  # home é o name que atribuimos no path no arquivo urls.py

    context = {'form': fdbkform}
    return render(request, 'core/feedback_form.html', context)


def deleteFeedback(request, pk):  # vamos precisar de uma primary key pra identificar qual feedback será deletado
    fdbk = Feedbacks.objects.get(id=pk)  # selecionamos o feedback através da pk

    if request.method == 'POST':
        fdbk.delete()
        return redirect('home')  # home é o name que atribuimos no path no arquivo urls.py
    #  essa view não precisa de context, pois não vai renderizar dado nenhum
    return render(request, 'core/delete_form.html')
