from django.contrib import admin
from suministros_informaticos_app.models import Compraventa, Proveedores, Clientes, Producto
# Register your models here.

#Aquí se gestiona qué campos vamos a ver en el admin de Django, además de añadir filtros y ordenar valores
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cif_dni', 'direccion', 'email', 'tfno', 'frecuencia')
    ordering = ['nombre']
    search_fields = ['nombre', 'cif_dni', 'tfno']

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cif_dni', 'direccion', 'email', 'tfno')
    ordering = ['nombre']
    search_fields = ['nombre', 'cif_dni', 'tfno']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'seccion', 'descripcion', 'cantidad_stock', 'precio_coste', 'precio_venta', 'beneficio', 'creador')
    ordering = ['nombre', 'marca', 'seccion']
    search_fields = ['nombre', 'marca']

class CompraventaAdmin(admin.ModelAdmin):
    list_display = ('producto' , 'cantidad', 'comprador')
    ordering = ['producto' , 'cantidad', 'comprador']

#Se registra el modelo
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Compraventa, CompraventaAdmin)