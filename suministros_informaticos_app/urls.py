"""suministros_informaticos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from suministros_informaticos_app import views
#Importa las vistas del Proyecto
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="Home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('acceso/', views.acceso, name="Acceso"),
    #Proveedores
    path('crear_proveedores/', views.crear_proveedores, name="Crear Proveedores"),
    path('editar_proveedores/<id>', views.editar_proveedores, name="Editar Proveedores"),
    path('eliminar_proveedores', views.eliminar_proveedores, name="Eliminar Proveedores"),
    #Clientes
    path('crear_clientes/', views.crear_clientes, name="Crear Clientes"),
    path('editar_clientes/<id>', views.editar_clientes, name="Editar Clientes"),
    path('eliminar_clientes', views.eliminar_clientes, name="Eliminar Clientes"),
    #Productos
    path('crear_productos/', views.crear_productos, name="Crear Productos"),
    path('editar_productos/<id>', views.editar_productos, name="Editar Productos"),
    path('eliminar_productos/<id>', views.eliminar_productos, name="Eliminar Productos"),
    #CompraVentas
    path('registrar_compra/', views.registrar_compraventa, name="Registrar Compraventa"),
    path('error_cantidad.html', views.error_cantidad, name="Error cantidad"),
    #Base
    path('base/', views.base, name="base"),
    path('signup/', views.sign_up, name="signup"),
    path('terms/', views.terms, name="terms"),
    path('privacy/', views.privacy, name="privacy"),

]