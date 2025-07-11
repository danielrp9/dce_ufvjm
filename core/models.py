from django.db import models
from django.contrib.auth.models import User  #vincular postagens a usuários

class BlogPost(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    links = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']  # Mais recentes primeiro
    
    
class Edital(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    arquivo = models.FileField(upload_to='editais/')

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_publicacao']  # Mais recentes primeiro

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-data_criacao']  # Mais recentes primeiro


class Configuracao(models.Model):
    logo = models.ImageField(upload_to='logos/')


class Atualizacao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    link = models.URLField(blank=True, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class MembroChapa(models.Model):
    CAMPUS_CHOICES = [
        ('Diamantina', 'Diamantina'),
        ('Janaúba', 'Janaúba'),
        ('Mucuri', 'Mucuri'),
        ('Unaí', 'Unaí'),
    ]

    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='membros_chapa/', blank=True, null=True)
    campus = models.CharField(max_length=20, choices=CAMPUS_CHOICES)

    def __str__(self):
        return f"{self.nome} - {self.campus}"

class Patrimonio(models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    valor_aproximado = models.DecimalField(max_digits=10, decimal_places=2)
    campi = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

from django.db import models

class Financeiro(models.Model):
    TIPO_CHOICES = [
        ('Receita', 'Receita'),
        ('Despesa', 'Despesa'),
    ]

    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.descricao} - {self.tipo} - R$ {self.valor}"


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    horario = models.CharField(max_length=50) 
    parceiros = models.CharField(max_length=255, blank=True, null=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    link_compra = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo
# Adicione ao seu models.py

class Atividade(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    imagem = models.ImageField(upload_to='atividades/')
    data = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo if self.titulo else f"Atividade {self.id}"
    
class BannerChapa(models.Model):
    imagem = models.ImageField(upload_to='banners_chapa/', help_text="Imagem principal do banner da chapa.")
    titulo = models.CharField(max_length=255, default="Chapa", help_text="Título exibido no banner.")
    subtitulo = models.CharField(max_length=255, default="Conheça os membros da chapa", help_text="Subtítulo exibido no banner.")
    ativo = models.BooleanField(default=True, help_text="Apenas o banner ativo será exibido.")
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Banner da Chapa"
        verbose_name_plural = "Banners da Chapa"

    def __str__(self):
        return f"Banner da Chapa - {self.titulo} ({'Ativo' if self.ativo else 'Inativo'})"