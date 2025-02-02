from django import forms
from .models import Categoria,Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BusquedaProductoForm(forms.Form):
    # Campo de texto para buscar por nombre de producto
    nombre = forms.CharField(
        max_length=100,
        required=False,  # No obligatorio
        label='',  # No genera un label
        widget=forms.TextInput(attrs={'placeholder': 'Buscar Producto'})
    )
    
    # Campo oculto para la categoría (para filtrar sin mostrar el selector)
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,  # No obligatorio
        widget=forms.HiddenInput()  # Oculta el campo en el formulario
    )
 
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de Usuario', 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        label='Contraseña', 
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'})
    )


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'cantidad', 'estado', 'descripcion', 'categoria', 'imagen']
    

#   LuisArcani
#   luis12345