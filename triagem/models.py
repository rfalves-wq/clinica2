from django.db import models
from pacientes.models import Paciente
from enfermeiros.models import Enfermeiro

class Triagem(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.CASCADE)

    criada_em = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.paciente.nome} → {self.enfermeiro.nome}'
