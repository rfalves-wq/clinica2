from django.db import models
from pacientes.models import Paciente
from enfermeiros.models import Enfermeiro

class Atendimento(models.Model):
    STATUS_CHOICES = (
        ('AGUARDANDO', 'Aguardando Triagem'),
        ('EM_TRIAGEM', 'Em Triagem'),
        ('FINALIZADO', 'Triagem Finalizada'),
    )

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    enfermeiro = models.ForeignKey(Enfermeiro, on_delete=models.SET_NULL, null=True, blank=True)
    chegada = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AGUARDANDO'
    )

    def __str__(self):
        return self.paciente.nome
