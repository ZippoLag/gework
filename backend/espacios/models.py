from itertools import chain
from django.db import models
from django.utils import timezone

# TODO: crear modelos de datos
# CLM: creado modelo de datos en base a DCML
# Notas: agregué un id unico a cada clase creada, esto no estaba en el DCML
# Duda: los niveles dentro de la clase Permiso, deberían estar tipificados?
class Cowork(models.Model):
    id_cowork = models.AutoField(primary_key=True)
    nombre_cowork = models.CharField(max_length=50)
    direccion_cowork = models.CharField(max_length=50)
    inicioTM_cowork = models.CharField(max_length=8)
    finTM_cowork = models.CharField(max_length=8)
    inicioTT_cowork = models.CharField(max_length=8)
    finTT_cowork = models.CharField(max_length=8)
    urlGoogleMaps = models.URLField()

class Prestacion(models.Model):
    id_prestacion = models.AutoField(primary_key=True)
    nombre_prestacion = models.CharField(max_length=50)
    desc_prestacion = models.CharField(max_length=200)
    icono_prestacion = models.CharField(max_length=200)

class Espacio(models.Model):
    id_espacio = models.AutoField(primary_key=True)
    nombre_espacio = models.CharField(max_length=50)
    precioMJ_espacio = models.DecimalField(max_digits=10, decimal_places=3)
    precioJC_espacio = models.DecimalField(max_digits=10, decimal_places=3)
    ubicacion_espacio = models.CharField(max_length=100)
    id_cowork = models.ForeignKey(Cowork, on_delete=models.CASCADE)
    prestaciones = models.ManyToManyField(Prestacion)

class Puesto(models.Model):
    id_puesto = models.AutoField(primary_key=True)
    ubicacion_puesto = models.CharField(max_length=100)
    disponibilidadTM_puesto = models.BooleanField()
    disponibilidadTT_puesto = models.BooleanField()
    id_espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    dni_usuario = models.IntegerField(unique=True, blank=False)
    nombre_usuario = models.CharField(max_length=50)
    apellido_usuario = models.CharField(max_length=50)
    email_usuario = models.EmailField(max_length=70)
    pass_usuario = models.CharField(max_length=30, blank=False)
    linkedin_usuario = models.URLField()
    alta_usuario = models.DateTimeField(auto_now_add=True)
    inactivo_usuario = models.DateTimeField()

class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    desc_permiso = models.CharField(max_length=50)
    nivel_permiso = models.IntegerField()
    id_cowork = models.ForeignKey(Cowork, on_delete=models.CASCADE)   
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    fecha_contrato = models.DateTimeField(auto_now_add=True)
    inicio_contrato = models.DateTimeField()
    fin_contrato = models.DateTimeField()
    importe_contrato = models.DecimalField(max_digits=10, decimal_places=3)
    estrellas_contrato = models.IntegerField()
    resenia_contrato = models.CharField(max_length=250)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)

class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    medio_pago = models.CharField(max_length=100)
    idext_pago = models.CharField(max_length=100)
    importe_pago = models.DecimalField(max_digits=10, decimal_places=3)
    id_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)