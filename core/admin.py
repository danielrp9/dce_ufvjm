from django.contrib import admin
from .models import (
    BlogPost, Edital, Evento, Post, Configuracao, Atualizacao, 
    MembroChapa, Patrimonio, Financeiro
)

# Registrar os modelos normalmente
admin.site.register(BlogPost)
admin.site.register(Edital)
admin.site.register(Evento)
admin.site.register(Post)
admin.site.register(Configuracao)
admin.site.register(MembroChapa)
admin.site.register(Patrimonio)

# Personalização do Django Admin
admin.site.site_header = "Administração do DCE"
admin.site.site_title = "Administração DCE Blog"
admin.site.index_title = "Bem-vindo ao painel de administração"

# Configuração do Admin para Atualização
@admin.register(Atualizacao)
class AtualizacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_publicacao")
    search_fields = ("titulo", "descricao")

# Configuração do Admin para Financeiro
@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ("descricao", "tipo", "valor", "data") 
    search_fields = ("descricao",)  
    list_filter = ("tipo", "data") 
    ordering = ("-data",)  # Ordenação do mais recente para o mais antigo
    list_per_page = 20 
