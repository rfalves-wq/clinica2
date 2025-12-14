from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    cpf = models.CharField(max_length=14, unique=True)  # Adicionando CPF

    def __str__(self):
        return self.nome
