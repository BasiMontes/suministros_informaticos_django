/* 
Datatype: 
nombre = models.CharField(max_length=50)
cif_dni = models.CharField(max_length=9)
direccion = models.CharField(max_length=50)
cp = models.IntegerField(max_length=5)
email = models.EmailField(blank=True, null=True)
tfno = models.IntegerField(max_length=9)
frecuencia = models.ForeignKey(Frecuencia, on_delete=models.DO_NOTHING) COMPLETAR LA FRECUENCIA EN ADMIN
facturacion = models.IntegerField(max_length=10)
descuento = models.IntegerField(max_length=3)
iva = models.IntegerField(max_length=2)

FUENTE: https://www.proveedores.com/informatica/zaragoza
*/
INSERT INTO suministros_informaticos_app_proveedores (nombre, cif_dni, direccion, cp, email, tfno, frecuencia_id, facturacion, clientes_perfil_id, esCliente, esProveedor))
VALUES ('Cool Accesorios', '12345678A' , 'Carril Huerto Alix, 34, Murcia', 30012, 'info@coolaccesorios.com', 968296989, 3, 2000, 5, 8),
	   ('Retrocables', '23456789B' , 'C/Polonia, 6, Leganés - Madrid', 28916, 'info@retrocables.com', 916882599, 4, 3000, 5, 8),
	   ('ASERSA', '34567890C' , 'C/Fomento,14 P.I.S.A., Mairena del Aljarafe - Sevilla', 41927, 'info@asersa.com', 670857263, 2, 1000, 3, 10),
	   ('TPVClick', '45678901D' , 'Garrotxa 6, Vidreres - Girona', 17411, 'info@tpvclick.com', 972020845, 4, 4500, 6, 9),
	   ('Dimara Canarias', '56789012E' , 'Cortijo de San Gregorio, Palmas de Gran Canaria (Las) - Las Palmas', 35018, 'info@dimaracanarias.com', 619620485, 5, 500, 5, 10),
	   ('Consulpyme', '67890123F' , 'Grupo Santo Domingo de Guzmán 14, lonja 8, Bilbao - Vizcaya', 48006, 'info@consulpyme.com', 944761124, 3, 1500, 8, 12),
	   ('Wontech Consultores Neutrales', '78901234G' , 'Electronica 19 6D Badalona, Badalona - Barcelona', 08915, 'info@wontech.com', 683361084, 4, 2000, 4, 8),
	   ('BZ Proyecta', '89012345H' , 'Duquesa de Parcent,10 1ºF, Málaga (Ciudad) - Málaga', 29001, 'info@bzproyecta.com', 951212369, 3, 1000, 2, 5),
	   ('Setiglobal', '90123456I' , 'Manuel Cueto Guisasola, 1, Oviedo - Asturias', 33013, 'info@setiglobal.com', 985963020, 3, 2500, 6, 12),
	   ('Globaltec', '12345678U' , 'C/ PARÍS, 35, LOCAL 7 A, Sevilla', 41089, 'info@globaltec.com', 954129123, 3, 2500, 6, 9)
	   ;

/*______________________________________________________________*/

Consultpyme
Globaltec
Retrocables
Setiglobal
TPVClick

INSERT INTO suministros_informaticos_app_proveedores (nombre, cif_dni, direccion, cp, email, tfno, frecuencia_id, facturacion, proveedor_perfil_id, esCliente, esProveedor)
VALUES ('Retrocables', '23456789B' , 'C/Polonia, 6, Leganés - Madrid', 28916, 'info@retrocables.com', 916882599, 4, 3000, 1, 0, 1),
	   ('TPVClick', '45678901D' , 'Garrotxa 6, Vidreres - Girona', 17411, 'info@tpvclick.com', 972020845, 4, 4500, 2, 0, 1),
	   ('Consulpyme', '67890123F' , 'Grupo Santo Domingo de Guzmán 14, lonja 8, Bilbao - Vizcaya', 48006, 'info@consulpyme.com', 944761124, 3, 1500, 3, 0, 1),
	   ('Setiglobal', '90123456I' , 'Manuel Cueto Guisasola, 1, Oviedo - Asturias', 33013, 'info@setiglobal.com', 985963020, 3, 2500, 4, 0, 1),
	   ('Globaltec', '12345678U' , 'C/ PARÍS, 35, LOCAL 7 A, Sevilla', 41089, 'info@globaltec.com', 954129123, 3, 2500, 5, 0, 1)
	   ;

/* Consultar datos*/  
SELECT * FROM suministros_informaticos_app_proveedores;

/* Borrar datos*/
DELETE FROM suministros_informaticos_app_proveedores;