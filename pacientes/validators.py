# patients/validators.py
import re
from django.core.exceptions import ValidationError

def validate_cpf(value):
    # Remove caracteres não numéricos
    cpf = re.sub(r'[^0-9]', '', value)

    # CPF deve ter 11 dígitos
    if len(cpf) != 11:
        raise ValidationError("CPF deve conter 11 dígitos.")

    # Não pode ser sequência repetida (000..., 111..., etc.)
    if cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    # Validação dos dígitos verificadores
    def calc_digit(digs):
        s = sum(int(d) * w for d, w in zip(digs, range(len(digs) + 1, 1, -1)))
        d = (s * 10) % 11
        return d if d < 10 else 0

    if int(cpf[9]) != calc_digit(cpf[:9]) or int(cpf[10]) != calc_digit(cpf[:10]):
        raise ValidationError("CPF inválido.")
