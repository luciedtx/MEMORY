from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    # path('', views.profil, name='profil'),
    # path('', views.inscription, name='inscription'),
    # path('', views.connexion, name='connexion'),

]
