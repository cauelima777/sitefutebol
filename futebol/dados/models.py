from django.db import models

# Create your models here.

class Clube(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Jogador(models.Model): 
    foto = models.ImageField(upload_to='static/', blank=True, null=True)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.nome 

class Dados(models.Model): 
    clube_detail = models.CharField(max_length = 50)
    Competicao = models.CharField(max_length = 50)
    jogador = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    temporada = models.IntegerField(default=0)
    partidas = models.IntegerField(default=0)
    gols = models.IntegerField(default=0)
    assistências = models.IntegerField(default=0)
