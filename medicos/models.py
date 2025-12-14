from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
