from django.forms import ModelForm
from carros.models import Carro

class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ["carro","marca","ano"]