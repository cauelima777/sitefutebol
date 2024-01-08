from django import forms 
from dados.models import Jogador, Dados
class JogadorForm(forms.ModelForm):  # Corrigindo a primeira letra para maiúscula
    class Meta: 
        model = Jogador 
        fields = '__all__'
        
class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = '__all__'
        

