from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    victoire = models.IntegerField(default=0)
    score_jeu = models.IntegerField(default=0)
    date_partie = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.score_jeu} - {self.date_partie} - {self.victoire}"