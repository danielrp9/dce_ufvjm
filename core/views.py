from django.shortcuts import render
from .models import BlogPost, Edital, Evento, Post, Configuracao, Atualizacao, MembroChapa, Patrimonio, Financeiro, Atividade # Certifique-se de importar Atividade

def home(request):
    """
    Renderiza a página inicial.
    Exibe configurações e atualizações recentes.
    """
    configuracao = Configuracao.objects.first()
    atualizacoes = Atualizacao.objects.all().order_by("-data_publicacao")[:6]
    context = {
        "configuracao": configuracao,
        "atualizacoes": atualizacoes,
    }
    return render(request, "home.html", context)

def blog(request):
    """
    Renderiza a página do blog, exibindo todos os posts.
    """
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def editais(request):
    """
    Renderiza a página de editais, exibindo a lista de editais.
    """
    editais_list = Edital.objects.all()
    return render(request, 'editais.html', {'editais': editais_list})

def eventos(request):
    """
    Renderiza a página de eventos, exibindo todos os eventos.
    """
    eventos = Evento.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos})

def blog_view(request):
    """
    Renderiza a página do blog, exibindo posts ordenados por data de criação.
    (Essa função parece ser duplicada com 'blog', considere unificar se possível)
    """
    posts = Post.objects.all().order_by('-data_criacao')
    return render(request, 'blog.html', {'posts': posts})

def inicio(request):
    """
    Renderiza a página de início, exibindo configurações.
    (Essa função parece ter o mesmo propósito de 'home' em algumas partes, considere unificar)
    """
    configuracao = Configuracao.objects.first()
    return render(request, 'inicio.html', {'configuracao': configuracao})

def chapa_view(request):
    """
    Renderiza a página da chapa, exibindo membros por campus
    e as atividades recentes da chapa.
    """
    membros = MembroChapa.objects.all()
    membros_por_campus = {
        'Diamantina': membros.filter(campus='Diamantina'),
        'Janaúba': membros.filter(campus='Janaúba'),
        'Mucuri': membros.filter(campus='Mucuri'),
        'Unaí': membros.filter(campus='Unaí'),
    }
    # Adicionando as atividades para a página da chapa
    atividades = Atividade.objects.filter(ativo=True).order_by('-data')[:8]
    
    context = {
        'membros_por_campus': membros_por_campus,
        'atividades': atividades, # Atividades agora na página da chapa
    }
    return render(request, 'chapa.html', context)

def patrimonio_view(request):
    """
    Renderiza a página de patrimônio, com funcionalidade de busca.
    """
    query = request.GET.get("q")
    if query:
        patrimonio_list = Patrimonio.objects.filter(descricao__icontains=query)
    else:
        patrimonio_list = Patrimonio.objects.all()

    return render(request, 'patrimonio.html', {'patrimonio_list': patrimonio_list})

def financeiro_view(request):
    """
    Renderiza a página financeira, com funcionalidade de busca.
    """
    query = request.GET.get('q', '')

    if query:
        financeiro_list = Financeiro.objects.filter(descricao__icontains=query)
    else:
        financeiro_list = Financeiro.objects.all()

    return render(request, 'financeiro.html', {'financeiro_list': financeiro_list})