from django.db import models

# Create your models here.
class miniM(models.Model):
	Orientacion1 = models.CharField(max_length=100, null=True)
	Orientacion2 = models.CharField(max_length=100, null=True)
	Orientacion3 = models.CharField(max_length=100, null=True)
	Orientacion4 = models.CharField(max_length=100, null=True)
	Orientacion5 = models.CharField(max_length=100, null=True)
	Espacial1 = models.CharField(max_length=100, null=True)
	Espacial2 = models.CharField(max_length=100, null=True)
	Espacial3 = models.CharField(max_length=100, null=True)
	Espacial4 = models.CharField(max_length=100, null=True)
	Espacial5 = models.CharField(max_length=100, null=True)
	fijacion = models.CharField(max_length=100, null=True)
	calculo = models.CharField(max_length=100, null=True)
	recuerdo = models.CharField(max_length=100, null=True)
	lenguaje1 = models.CharField(max_length=100, null=True)
	lenguaje2 = models.CharField(max_length=100, null=True)
	lenguaje3 = models.CharField(max_length=100, null=True)
	lenguaje4 = models.CharField(max_length=100, null=True)
	lenguaje5 = models.CharField(max_length=100, null=True)
