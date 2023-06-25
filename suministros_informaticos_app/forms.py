from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction


class Login_form(forms.Form):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'validate'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'input'}))

#CRUD PROVEEDORES
#Crear proveedores como usuarios
class Crear_proveedores(UserCreationForm):
    #Campos de Proveedor
    nombre = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cif_dni = forms.CharField(label='CIF - DNI', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label='Dirección', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    tfno = forms.IntegerField(label='Teléfono', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    frecuencia = forms.ChoiceField(label='Frecuencia', choices=((1, ('Diaria')), (2, ('Bisemanal')), (3, ('Semanal')),(4, ('Quincenal')), (5, ('Mensual')), (6, ('Puntual'))))
    
    class Meta(UserCreationForm.Meta):
        model = User
   
    @transaction.atomic
    def save(self):
        user = super(Crear_proveedores, self).save(commit=False)
        user.save()
        proveedor = Proveedores.objects.create(proveedor_perfil=user)
        proveedor.nombre = self.cleaned_data.get('nombre')
        proveedor.cif_dni = self.cleaned_data.get('cif_dni')
        proveedor.direccion = self.cleaned_data.get('direccion')
        proveedor.email = self.cleaned_data.get('email')
        proveedor.tfno = self.cleaned_data.get('tfno')
        proveedor.frecuencia = self.cleaned_data.get('frecuencia')
        proveedor.save()
        return user

class Editar_Proveedores(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'
        exclude = 'esCliente', 'esProveedor', 'proveedor_perfil'
    
    def get_object_(self):
        return self.request.user


#CRUD CLIENTES
#Crear clientes como usuarios
class Crear_clientes(UserCreationForm):
    #Campos de Clientes
    nombre = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cif_dni = forms.CharField(label='CIF - DNI', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label='Dirección', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    tfno = forms.IntegerField(label='Teléfono', required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
   
    @transaction.atomic
    def save(self):
        user = super(Crear_clientes, self).save(commit=False)
        user.save()
        clientes = Clientes.objects.create(cliente_perfil=user)
        clientes.nombre = self.cleaned_data.get('nombre')
        clientes.cif_dni = self.cleaned_data.get('cif_dni')
        clientes.direccion = self.cleaned_data.get('direccion')
        clientes.email = self.cleaned_data.get('email')
        clientes.tfno = self.cleaned_data.get('tfno')
        clientes.save()
        return user

class Editar_Clientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'
        exclude = 'esCliente', 'esProveedor', 'cliente_perfil'

            
    def get_object_(self):
        return self.request.user


#CRUD Productos
class Crear_productos(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'seccion', 'descripcion', 'cantidad_stock' , 'precio_coste', 'precio_venta']
        exclude = ['creador']

class Editar_Productos(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        exclude = 'creador',
    
    def get_object_(self):
        return self.request.user

#CRUD compraventa
class Registrar_compraventa(forms.ModelForm):

    class Meta:
        model = Compraventa
        fields = ['producto' , 'cantidad']
        exclude = ['comprador']

