from django.urls import path
from . import views

#rotas
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('editais/', views.editais, name='editais'),
    path('eventos/', views.eventos, name='eventos'),
    path('blog/', views.blog_view, name='blog'),  
    path('chapa/', views.chapa_view, name='chapa'), 
    path('patrimonio/', views.patrimonio_view, name='patrimonio'), 
    path('financeiro/', views.financeiro_view, name='financeiro'),
]

