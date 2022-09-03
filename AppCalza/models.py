import email
from django.db import models

class Medicos(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    matricula=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido

class Enfermeras(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    matricula=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido

class Pacientes (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido

