/*
Datatype:
nombre = models.CharField(max_length=30)
cif_dni = models.CharField(max_length=9)
direccion = models.CharField(max_length=50)
cp = models.IntegerField()
email = models.EmailField(blank=True, null=True)
tfno = models.IntegerField()

FUENTE: https://www.proveedores.com/informatica/zaragoza-3
*/

INSERT INTO suministros_informaticos_app_clientes (nombre, cif_dni, direccion, cp, email, tfno)
VALUES ('Simutec', '98765432A', 'Enrique Muñoz Ezquerra Brazal Zapateros 17, Zaragoza', 50016 , 'info@simutec.com', 958746222),
	   ('Franjosa', '87654321B', 'Vía Ramón Pignatelli, 33, Zaragoza', 50007 , 'info@franjosa.com', 976258625)
	   ('Tradetech International Logistics', '76543210C', 'Paseo María Agustín 4-6 ESC.3, Zaragoza', 50004 , 'info@tradetechIL.com', 876269391),
	   ('Aesa Aragonesa de Equipamiento', '65432109D', 'Calle Menendez Pelayo 34 local, Zaragoza', 50009 , 'info@aesa.com', 976351158),
	   ('Acesa', '54321098E', 'Calle Bari, 39, 50197 Zaragoza', 50197 , 'info@acesa.com', 902440220),
	   ('Accionet Consultoría', '43210987F', 'Avda. Juan Carlos I, 20 1ª B, Zaragoza', 50009 , 'info@accionet.com', 976373973),
	   ('ABC Ordina2', '90123456S' , 'C/Amalia Soler 23, Vilafranca del Penedès, Barcelona', 08720, 'info@abcordina2.com', 938902409),
	   ('OKPC Barcelona', '01234567T' , 'Passeig de Maragall, 123, Barcelona', 08041, 'info@okpcbcn.com', 932115973),
	   /**/
	   ('Megamax Infoline', '43210987F', 'Calle de Zubieta 7, Madrid', 28037 , 'info@megamax.com', 671156510),
	   ('Lotespc | Ordenadores de Segunda Mano', '32109876G', 'Calle Henri Dunant 17, Madrid', 28036 , 'info@lotespc.com', 688811747)
	   ;

SELECT *
FROM suministros_informaticos_app_clientes;

DELETE FROM suministros_informaticos_app_clientes;

INSERT INTO suministros_informaticos_app_clientes (nombre, cif_dni, direccion, cp, email, tfno, clientes_perfil_id, esCliente, esProveedor)
VALUES ('Simutec', '98765432A', 'Enrique Muñoz Ezquerra Brazal Zapateros 17, Zaragoza', 50016 , 'info@simutec.com', 958746222, 1, 1, 0),
	   ('Franjosa', '87654321B', 'Vía Ramón Pignatelli, 33, Zaragoza', 50007 , 'info@franjosa.com', 976258625, 2, 1, 0),
	   ('Acesa', '54321098E', 'Calle Bari, 39, 50197 Zaragoza', 50197 , 'info@acesa.com', 902440220, 3, 1, 0),
	   ('ABC Ordina2', '90123456S' , 'C/Amalia Soler 23, Vilafranca del Penedès, Barcelona', 08720, 'info@abcordina2.com', 938902409, 4, 1, 0),
	   ('OKPC Barcelona', '01234567T' , 'Passeig de Maragall, 123, Barcelona', 08041, 'info@okpcbcn.com', 932115973, 5, 1, 0);

Simutec
Franjosa
Acesa
OKPC Barcelona
ABC Ordina2

/* Consultar datos*/  
SELECT * FROM suministros_informaticos_app_clientes;

/* Borrar datos*/
DELETE FROM suministros_informaticos_app_clientes;