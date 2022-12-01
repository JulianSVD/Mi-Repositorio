from django.db import models

# es la estructura de las bases de dato
#Los modelos son tablas de la base de datos
class Curso(models.Model):
    nombre= models.CharField(max_lenght=50)
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_lenght=50)
    apellido=models.CharField(max_lenght=50)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_lenght=50)
    apellido=models.CharField(max_lenght=50)
    email=models.EmailField()
    profesion=models.CharField(max_lenght=50)

class Entregable(models.Model):
    nombre=models.CharField(max_lenght=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()#SI o NO (estado de entrega)