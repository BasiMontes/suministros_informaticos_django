/*
Datatype:
    fecha = models.DateField()
    cantidad = models.IntegerField() #PONER LIMITACION DE CARACTERES
    seccion = models.CharField(max_length=20)
    id_producto_compras = models.ManyToManyField(Producto) #PONER LIMITACION DE CARACTERES
    id_proveedor_compras = models.ForeignKey(Proveedores, on_delete=models.CASCADE) #PONER LIMITACION DE CARACTERES
    #precio_coste_compras = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='precio_coste_compras', default=None) #PONER LIMITACION DE CARACTERES


*/
-- Con las secciones id, marca_id y trimestre_id
INSERT INTO suministros_informaticos_app_compras (id, fecha, cantidad, seccion_id, id_proveedor_compras_id, marca_id, trimestre_id)
VALUES 
	(1, '2016-01-01', 10, 1, 4, 1, 1);

--Sin secciones
INSERT INTO suministros_informaticos_app_compras (id, fecha, seccion, id_proveedor_compras_id, cantidad)
VALUES 
	(1, '2021-01-01', 'Sillas', 4, 10),
	(2, '2020-02-05', 'Periféricos', 5, 20),
    (3, '2021-03-01', 'Tablets', 6, 26),
	(4, '2020-04-05', 'Consolas', 1, 5),
    (5, '2021-05-01', 'Componentes ordenadores', 2, 45),
	(6, '2020-06-05', 'Portátiles', 5, 15),
    (7, '2021-07-01', 'Accesorios', 7, 38),
	(8, '2020-08-05', 'Audio', 8, 40),
    (9, '2021-09-01', 'Smartphones', 4, 14),
	(10, '2020-10-05', 'Smartphones', 6, 3),
    (11, '2021-11-01', 'Smartphones', 2, 8),
	(12, '2020-12-05', 'Smartphones', 5, 7);

DELETE FROM suministros_informaticos_app_compras;