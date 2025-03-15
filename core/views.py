from django.shortcuts import render
from .models import BlogPost, Edital, Evento, Post, Configuracao, Atualizacao, MembroChapa, Patrimonio, Financeiro

def home(request):
    return render(request, 'home.html')

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def editais(request):
    editais_list = Edital.objects.all()
    return render(request, 'editais.html', {'editais': editais_list})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def blog_view(request):
    posts = Post.objects.all().order_by('-data_criacao')  # Ordena os posts por data (mais recentes primeiro)
    return render(request, 'blog.html', {'posts': posts})

def inicio(request):
    configuracao = Configuracao.objects.first()
    return render(request, 'inicio.html', {'configuracao': configuracao})

def home(request):
    atualizacoes = Atualizacao.objects.all().order_by("-data_publicacao")[:6]
    return render(request, "home.html", {"atualizacoes": atualizacoes})

def chapa_view(request):
    membros = MembroChapa.objects.all()
    membros_por_campus = {
        'Diamantina': membros.filter(campus='Diamantina'),
        'Janaúba': membros.filter(campus='Janaúba'),
        'Mucuri': membros.filter(campus='Mucuri'),
        'Unaí': membros.filter(campus='Unaí'),
    }
    return render(request, 'chapa.html', {'membros_por_campus': membros_por_campus})

def patrimonio_view(request):
    query = request.GET.get("q")
    if query:
        patrimonio_list = Patrimonio.objects.filter(descricao__icontains=query)
    else:
        patrimonio_list = Patrimonio.objects.all()

    return render(request, 'patrimonio.html', {'patrimonio_list': patrimonio_list})

def financeiro_view(request):
    query = request.GET.get('q', '')

    if query:
        financeiro_list = Financeiro.objects.filter(descricao__icontains=query)
    else:
        financeiro_list = Financeiro.objects.all()

    return render(request, 'financeiro.html', {'financeiro_list': financeiro_list})

    