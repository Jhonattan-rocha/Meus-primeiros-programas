from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('imovel/<str:id>', views.imovel, name="imovel"),
    path('agendar_visitas', views.agendar_visitas, name="agendar_visitas"),
    path('agendamentos', views.agendamentos, name="agendamentos"),
    path('cancelar_agendamento/<str:id>', views.cancelar_agendamento, name="cancelar_agendamento"),
    path('homepage/', views.homepage, name='homep'),
    path('apagar_imovel/<str:id>', views.apagar_imovel, name='apagarIM'),
    path('alterar/<int:id>', views.alterar, name='alterar')
]
