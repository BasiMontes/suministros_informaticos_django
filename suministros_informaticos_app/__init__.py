'''
    ###Ejecutar servidor###
python manage.py runserver <puerto>
python manage.py runserver 127.0.0.1:8080

    ###Detener servidor###
CONTROL + C

    ###Iniciar App en Terminal###
python manage.py startapp <nombre_app>

    ###Checkear que todo este bien###
python manage.py check <nombre_app>

    1 ###Hacer los cambios-migraciones###
python manage.py makemigrations

    2 ###Del SQL/Django a la BBDD
python manage.py migrate
python manage.py migrate --run-syncdb (Para posibles errores con BBDD, django no such table)

    3 ###Por si no puedes acceder al admin y se ha cambiado la bbdd
python manage.py migrate sessions

    ###Crear un superUsuario para el panel de administracion de Django###
python manage.py createsuperuser

user: basi
mail: basi_montes@hotmail.com
pss: basi


Usuarios:
- clientes --> PSS: perfil_cliente
- proveedor --> PSS: perfil_proveedor

usuario = models.OneToOneField(User, on_delete=models.CASCADE)

PSS:
Cool_Accesorios_PR - proveedor
Simutec_CL - clientes
'''