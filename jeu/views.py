from django.shortcuts import render
from django.shortcuts import render, redirect
#from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Score
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"jeu/index.html")

def index2(request):
    return render(request,"jeu/index2.html")

def profil(request):
    return render(request,"jeu/profil.html")

def inscription(request):
     return render(request, 'jeu/inscription.html')

def connexion(request):
    return render(request, 'jeu/connexion.html')

def game(request):
    return render(request, 'jeu/game.html')

def api(request):
    return render(request, 'jeu/api.html')

def inscription(request):
    # Logique pour l'inscription
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        try:
            if username and password:
                user = User.objects.create_user(username=username, password=password, email=email, last_name=last_name, first_name=first_name)
                # Ajouter votre logique ici pour créer un Score
                Score.objects.create(user=user, score=0, victoire=0)
                login(request, user)
                return redirect('home')  # Redirigez l'utilisateur vers la page d'accueil après l'inscription
        except Exception as e:
            print(f"Erreur lors de l'inscription : {e}")
        
    return render(request, 'jeu/inscription.html')


def connexion(request):
    #Logique pour la connexion
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige vers la page d'accueil après la connexion réussie
        else:
            # Gérer le cas où l'authentification échoue (afficher un message d'erreur, etc.)
            pass
    return render(request, 'jeu/connexion.html')

@login_required
def deconnexion(request):
    logout(request)
    #Logique pour la déconnexion
    return redirect ('index')