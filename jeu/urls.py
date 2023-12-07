from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name= 'index'),
    path('profil', views.profil, name='profil'),
    path('inscription', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    path('game', views.game, name='game'),
    path('deconnect', views.deconnexion, name='deconnect'),
    path('index2', views.index2, name= 'index2'),
    path('api',views.api, name='api')
]
