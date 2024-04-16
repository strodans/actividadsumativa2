from django.db import models

# Create your models here.
class Usuario(models.Model):
    run = models.IntegerField(primary_key=True, verbose_name='RUN')
    username = models.CharField(max_length=10, verbose_name='Usuario')
    nombres = models.CharField(max_length=60, verbose_name='Nombres')
    apellidos = models.CharField(max_length=60, verbose_name='Apellidos')
    password = models.CharField(max_length=255, verbose_name='Contraseña')
    perfil = models.IntegerField(null=True, blank=True, verbose_name='Perfil')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class RecuperarContrasena(models.Model):
    email = models.EmailField(verbose_name='Correo Electrónico')

    def __str__(self):
        return self.email

class ModificarPerfil(models.Model):
    nombres = models.CharField(max_length=60, verbose_name='Nombres')
    apellidos = models.CharField(max_length=60, verbose_name='Apellidos')

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name='Id de la categoria')
    nombre_categoria = models.CharField(max_length=60, verbose_name='categoria')

    def __str__(self):
        return self.nombre_categoria


class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True, verbose_name='id_inventario')
    nombre = models.CharField(max_length=60, verbose_name='nombre')
    modelo = models.CharField(max_length=60, verbose_name='modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='inventario/', null=True, verbose_name='Imagen del producto')

    def __str__(self):
        return self.nombre