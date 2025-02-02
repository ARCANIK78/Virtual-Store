from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import ProductoList

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),  # Ruta para la vista del catálogo
    path('login/', views.login_view, name='login'),  # Ruta para el formulario de inicio de sesión
    path('registro/', views.registro_view, name='registro'),  # Ruta para la vista de registro
    path('admin_page/', views.admin_page, name='admin_page'),
    path('producto/<int:id>/', views.producto_detalle, name='producto_detalle'),  # Ruta para el detalle de un producto, con el ID como parámetro
    path('logout/', LogoutView.as_view(), name='logout'),  # Ruta para cerrar sesión usando la vista predeterminada de Django
    path('admin_page/agregar_producto/', views.agregar_producto, name='agregar_producto'),  # Ruta para agregar productos desde la administración
    path('admin_page/usuarios/', views.gestion_usuarios, name='gestion_usuarios'),  # Ruta para gestionar usuarios desde la administración
    path('producto/<int:producto_id>/calificar/', views.calificar_producto, name='calificar_producto'),
    path('api/productos/', ProductoList.as_view(), name='productos-list'),
]