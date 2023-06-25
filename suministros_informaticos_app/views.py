from suministros_informaticos_app.models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import *
from django.template import RequestContext

# Habilitamos los formularios en Django
from django import forms

#Vistas de la web
def home(request):
    return render(request, "home.html")

def base(request):
    return render(request, "base.html")
    
def sign_up(request):
    return render(request, "signup.html")

def logout_view(request):
    logout(request)
    return redirect('Home')

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")


#Proveedores
def acceso(request):
    proveedores = Proveedores.objects.all()
    productos = Producto.objects.all()
    marcas = ["Apple", "LG", "Samsung", "Xiaomi"]
    secciones = ["Telefonía", "Televisión", "Portátiles"]
    compras = Compraventa.objects.all()


    lista_proveedores_ventas = []
    lista_marcas = []
    lista_secciones = []

    #Obtiene las seccion de los productos
    for producto in productos:
        lista_secciones.append(producto.seccion)

    #Obtiene las marcas de los productos
    for marca in marcas:
        cont_marcas = 0
        for producto in productos:
            if marca == producto.marca:
                cont_marcas = cont_marcas + 1
        lista_marcas.append(cont_marcas)

    #Obtiene las secciones de los productos
    for seccion in secciones:
        cont_secciones = 0
        for producto in productos:
            if seccion == producto.seccion:
                cont_secciones = cont_secciones + 1
        lista_secciones.append(cont_secciones)


    return render(request,'acceso.html', 
                {'proveedores':proveedores, 'productos':productos, 'compras':compras,
                 'lista_proveedores_ventas':lista_proveedores_ventas,
                 'secciones':secciones,'lista_secciones':lista_secciones, 
                 'marcas':marcas,'lista_marcas':lista_marcas
                 })

def crear_proveedores(request):
    if request.method =="POST":
        form = Crear_proveedores(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha creado el perfil de proveedor correctamente")
            return redirect('/login')
    else:
        form = Crear_proveedores()
        
    context = {'form':form}
    return render(request, 'crear_proveedores.html', context)

def eliminar_proveedores(request):
    usuario = request.user
    try:
        usuario.delete()
    except:
        pass

    return redirect('/')

def editar_proveedores(request, id):
    proveedores = get_object_or_404(Proveedores, id=id)

    data = {'form': Editar_Proveedores(instance=proveedores)}

    if request.method == "POST":
        form = Editar_Proveedores(data=request.POST, instance=proveedores)
        if form.is_valid():
            form.save()
            return redirect("/acceso")
        data['form'] = form
                
    return render(request, 'editar_proveedores.html', data)


#Clientes
def crear_clientes(request):
    if request.method =="POST":
        form = Crear_clientes(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha creado el perfil de cliente correctamente")
            return redirect('/login')
    else:
        form = Crear_clientes()
        
    context = {'form':form}
    return render(request, 'crear_clientes.html', context) 

def eliminar_clientes(request, id):
    clientes = get_object_or_404(Clientes, id=id)
    try:
        clientes.delete()
    except:
        pass

    return redirect('/logout')

def editar_clientes(request, id):
    clientes = get_object_or_404(Clientes, id=id)

    data = {'form': Editar_Clientes(instance=clientes)}

    if request.method == "POST":
        form = Editar_Clientes(data=request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('Acceso')
        data['form'] = form
                
    return render(request, 'editar_clientes.html', data)


#Productos
def crear_productos(request):
    if request.method =="POST":
        form = Crear_productos(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.creador = Proveedores(request.user.proveedores.id)
            producto.save()

            return redirect('Acceso')
    else:
        form = Crear_productos()
        
    context = {'form':form}
    return render(request, 'crear_productos.html', context)

def eliminar_productos(request, id):
    productos = get_object_or_404(Producto, id=id)
    try:
        productos.delete()
    except:
        pass

    return redirect("/acceso")

def editar_productos(request, id):
    productos = get_object_or_404(Producto, id=id)

    data = {'form': Editar_Productos(instance=productos)}

    if request.method == "POST":
        form = Editar_Productos(data=request.POST, instance=productos)
        if form.is_valid():
            form.save()
            return redirect("/acceso")
        data['form'] = form
                
    return render(request, 'editar_producto.html', data)


#COMPRAVENTA
def registrar_compraventa(request):
    if request.method =="POST":
        form = Registrar_compraventa(request.POST)
        if form.is_valid():
            compraventa = form.save(commit=False)
            compraventa.comprador = Clientes(request.user.clientes.id)
            if (compraventa.producto.cantidad_stock < compraventa.cantidad):
                response = redirect('Error cantidad')
                return response
            producto_id = form.cleaned_data.get('producto')
            cantidad_comprada = form.cleaned_data.get('cantidad')

            producto_comprado = Producto.objects.get(id=producto_id.id)    
            producto_comprado.cantidad_stock = producto_comprado.cantidad_stock - cantidad_comprada
            producto_comprado.save()
            compraventa.save()

            return redirect('Acceso')
    else:
        form = Registrar_compraventa()
        
    context = {'form':form}
    return render(request, 'registrar_compra.html', context)

def error_cantidad(request):
    return render(request, "error_cantidad.html")









    