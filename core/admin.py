from django.contrib import admin
from .models import Atividade
from .models import (
    BlogPost, Edital, Evento, Post, Configuracao, Atualizacao, 
    MembroChapa, Patrimonio, Financeiro,  BannerChapa,
)

admin.site.register(BlogPost)
admin.site.register(Edital)
admin.site.register(Evento)
admin.site.register(Post)
admin.site.register(Configuracao)
admin.site.register(MembroChapa)
admin.site.register(Patrimonio)


admin.site.site_header = "Administração do DCE"
admin.site.site_title = "Administração DCE Blog"
admin.site.index_title = "Bem-vindo ao painel de administração"


@admin.register(Atualizacao)
class AtualizacaoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "data_publicacao")
    search_fields = ("titulo", "descricao")


@admin.register(Financeiro)
class FinanceiroAdmin(admin.ModelAdmin):
    list_display = ("descricao", "tipo", "valor", "data") 
    search_fields = ("descricao",)  
    list_filter = ("tipo", "data") 
    ordering = ("-data",)  
    list_per_page = 20 

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'ativo')
    list_filter = ('ativo', 'data')
    search_fields = ('titulo',)

@admin.register(BannerChapa) # Esta linha estava causando o erro porque BannerChapa não estava importado
class BannerChapaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ativo', 'data_atualizacao')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'subtitulo')
    def save_model(self, request, obj, form, change):
        if obj.ativo:
            # Desativa outros banners ativos para garantir que apenas um esteja ativo por vez
            BannerChapa.objects.exclude(pk=obj.pk).update(ativo=False)
        super().save_model(request, obj, form, change)