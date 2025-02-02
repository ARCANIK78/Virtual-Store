from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto  # Asegúrate de que "Producto" es el nombre de tu modelo
        fields = '__all__'  # Esto incluirá todos los campos del modelo 