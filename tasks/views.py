from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto, Calificacion
from .forms import BusquedaProductoForm, RegistroForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User  # Corregido aquí
from .forms import LoginForm, ProductoForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer

def catalogo(request):
    # Obtener todas las categorías
    categorias = Categoria.objects.all()

    # Obtener todos los productos y ordenarlos por fecha de publicación (de más reciente a más antiguo)
    productos = Producto.objects.all().order_by('-fecha_publicacion')  # '-' para orden descendente (más reciente primero)

    # Procesar el formulario de búsqueda
    form = BusquedaProductoForm(request.GET or None)

    if form.is_valid():
        nombre = form.cleaned_data.get('nombre')

        # Filtrar productos por nombre si se proporcionó un término de búsqueda
        if nombre:
            productos = productos.filter(nombre__icontains=nombre)

        # Filtrar productos por categoría desde el parámetro de la URL, si está presente
        categoria_id = request.GET.get('categoria')
        if categoria_id:
            productos = productos.filter(categoria__id=categoria_id)

    return render(request, 'catalogo.html', {
        'categorias': categorias,
        'productos': productos,
        'form': form,
        'user': request.user  # Pasar el objeto user al contexto
    })
# Vista para mostrar el detalle de un producto
def producto_detalle(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'producto_detalle.html', {'producto': producto})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario directamente en User
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'registro_form.html', {'form': form})


def login_view(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Autentica al usuario y lo inicia sesión
                return redirect('catalogo')  # Redirige a la página deseada (cambiar según tu necesidad)
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos')
                
    return render(request, 'login_form.html', {'form': form})


# Vista de la página de administración
@login_required
def admin_page(request):
    # Verificar que el usuario sea un administrador
    if not request.user.is_staff:
        return HttpResponseForbidden("No tienes permisos para acceder a esta página.")

    return render(request, 'admin_page.html')  # Una plantilla HTML para el administrado

@login_required  # Asegúrate de que solo los usuarios autenticados puedan agregar productos
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            # Asignar el usuario autenticado al producto
            producto = form.save(commit=False)
            producto.usuario = request.user  # Aquí asignas el usuario autenticado
            producto.save()
            
            # Mostrar mensaje de éxito
            messages.success(request, "Producto agregado exitosamente.")
            
        else:
            # Mostrar mensaje de error si el formulario no es válido
            messages.error(request, "Hubo un error al agregar el producto.")
    else:
        form = ProductoForm()

    return render(request, 'agregar_producto.html', {'form': form})

@login_required
def gestion_usuarios(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("No tienes permisos para gestionar usuarios.")
    
    usuarios = User.objects.all()  # Mostrar todos los usuarios registrados
    return render(request, 'gestion_usuarios.html', {'usuarios': usuarios})


@login_required
def editar_usuario(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("No tienes permisos para editar usuarios.")
    
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('gestion_usuarios')
    else:
        form = UserChangeForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form})

@login_required
def eliminar_usuario(request, id):
    if not request.user.is_staff:
        return HttpResponseForbidden("No tienes permisos para eliminar usuarios.")
    
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('gestion_usuarios')

@login_required
def calificar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        estrellas = request.POST.get('estrellas')
        if estrellas:
            # Verificar si el usuario ya ha calificado este producto
            calificacion_existente = Calificacion.objects.filter(producto=producto, usuario=request.user).first()
            if calificacion_existente:
                calificacion_existente.estrellas = int(estrellas)
                calificacion_existente.save()
            else:
                Calificacion.objects.create(producto=producto, usuario=request.user, estrellas=int(estrellas))

            # Actualizar el promedio de calificación del producto
            producto.actualizar_calificacion_promedio()

            # Mostrar mensaje de éxito usando el sistema de mensajes de Django
            messages.success(request, "¡Calificación enviada con éxito! Gracias por tu opinión.")
    
    return render(request, 'producto_detalle.html', {'producto': producto})

class ProductoList(APIView):
    def get(self, request):
        # Obtén todos los productos de la base de datos
        productos = Producto.objects.all()
        # Serializa los productos (convierte a JSON)
        serializer = ProductoSerializer(productos, many=True)
        # Devuelve la respuesta con los productos serializados
        return Response(serializer.data)

# usuario = JoseAntonio
# JoseAntonio@gmail.com
# 12345