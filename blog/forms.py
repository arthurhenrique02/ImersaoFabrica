from django.forms import ModelForm
from .models import Contatos

# criar a classe de formulario para o create
class formulario(ModelForm):
    # criar um meta
    class Meta:
        model = Contatos
        fields = ['nome', 'numero', 'rua', 'bairro', 'casa', 'ponto_ref']