from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    VENTA = 'V'
    COMPRA = 'C'
    ESTADO_OPCIONES = [
        (VENTA, 'Venta'),
        (COMPRA, 'Compra'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=1, choices=ESTADO_OPCIONES, default=VENTA)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    calificacion_promedio = models.FloatField(default=0.0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    # Agregar un campo de imagen
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} - {self.usuario.username}'

    def actualizar_calificacion_promedio(self):
        """Método para actualizar la calificación promedio del producto"""
        calificaciones = self.calificaciones.all()
        if calificaciones.exists():
            promedio = sum([calificacion.estrellas for calificacion in calificaciones]) / calificaciones.count()
            self.calificacion_promedio = promedio
        else:
            self.calificacion_promedio = 0.0
        self.save()

class Calificacion(models.Model):
    producto = models.ForeignKey(Producto, related_name='calificaciones', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estrellas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estrellas} estrellas para {self.producto.nombre}"
