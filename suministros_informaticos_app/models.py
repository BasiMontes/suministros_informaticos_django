from django.db import models
from django.contrib.auth.models import User


#Tabla de Proveedores
class Proveedores(models.Model):

    frecuencia_select = (
        ('1', 'Diaria'),
        ('2', 'Bisemanal'),
        ('3', 'Semanal'),
        ('4', 'Quincenal'), 
        ('5', 'Mensual'), 
        ('6', 'Puntual')
    )

    proveedor_perfil = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    cif_dni = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    tfno = models.IntegerField(blank=True, null=True)
    frecuencia = models.CharField(max_length=20, choices = frecuencia_select)

    #Se ha añadido estas líneas de código para clasificar a los usuarios en Proveedores o Clientes
    esProveedor = models.BooleanField(default=True) 
    esCliente = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    '''
    @property
    def facturacion():
        proveedores = Proveedores.objects.all()
        productos = Producto.objects.all()
        ventas = Ventas.objects.all()
        precio_venta_con_impuestos = Producto.precio_venta_con_impuestos.objects.all()

        lista_facturacion = []

    #Obtiene la facturación de productos vendidos por proveedores
    for proveedor in proveedores:
        cont_seccion_ventas = 0
        for venta in ventas:
            for producto in venta.id_producto_ventas.all():
                if seccion.id == producto.seccion.id:
                    cont_seccion_ventas = cont_seccion_ventas + 1
        lista_seccion_venta_productos.append(cont_seccion_ventas)
    #print(lista_seccion_venta_productos)
    '''

#Tabla de Clientes
class Clientes(models.Model):
    cliente_perfil = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    cif_dni = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True) 
    tfno = models.IntegerField(default=0)

    esCliente = models.BooleanField(default=True)
    esProveedor = models.BooleanField(default=False)

    def __str__(self): 
        return self.nombre

#Tabla de productos
class Producto(models.Model):

    marca_choices = (
            (1, "Apple"),
            (2, "LG"),
            (3, "Samsung"),
            (4, "Xiaomi")
    )

    seccion_choices = (
            (1, "Telefonía"),
            (2, "Televisión"),
            (3, "Portátiles")
    )

    nombre = models.CharField(max_length=30)
    marca = models.IntegerField(choices=marca_choices)
    seccion = models.IntegerField(choices=seccion_choices, verbose_name='Sección')
    descripcion = models.CharField(max_length=50, verbose_name='Descripción')
    cantidad_stock = models.IntegerField(null=True, blank=True)
    precio_coste = models.FloatField(null=True, blank=True)
    precio_venta = models.FloatField(null=True, blank=True)
    creador = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre + ' - ' +str(self.cantidad_stock) + ' ud. disponibles ' +' - ' +str(self.precio_venta)+ '€ '


    #Cálculo del Beneficio por producto 
    @property
    def beneficio(self):
        return round(self.precio_venta - self.precio_coste, 2)
        self.save()

#Tabla de compraventa
class Compraventa(models.Model):
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    comprador = models.ForeignKey(Clientes, on_delete=models.CASCADE)   