from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"jeu/index.html")

# def profil(request):
#     return render(request,"jeu/profil.html")

# def inscription(request):
#      return render(request, 'jeu/inscription.html')

# def connexion(request):
#     return render(request, 'jeu/connexion.html')