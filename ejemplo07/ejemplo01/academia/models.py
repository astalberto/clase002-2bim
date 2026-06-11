from django.db import models
from datetime import datetime
# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def obtener_anioNacimiento(self):
        return datetime.now().year - self.edad   
    
    def provincia_cedula(self):
        if self.cedula[0:2]=="11":
            return "Loja"
        else:
            return "otra ciudad"
        
     
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI:{self.provincia_cedula()} - Edad:{self.edad} - Año de Nacimiento: {self.obtener_anioNacimiento()}"