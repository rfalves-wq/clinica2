from django.db import models
from django.contrib.auth.models import User



class Enfermeiro(models.Model):
    nome = models.CharField(max_length=100)
    coren = models.CharField(max_length=20)
    setor = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome