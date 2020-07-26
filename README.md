# APLICACION WEB CON FLASK, INVENTARIO DE LIBROS
# INSTALAR DEPENDENCIAS
- pip install flask
- pip install psycopg2
- pip install flask-wtf

# Utiliza una base de datos Postgresql
- PostgreSQL 9.5

# Nombre de la tabla
- tmovlibinv
# columnas de la tabla
- libro_cod -> character varying(5) -> Codigo de libro
- libro_nom -> character varying(20) -> Nombre del libro 
- libro_cat -> character varying(20) -> Categoria de libros
- libro_aut -> character varying(20) -> Autor del libro
- libro_año -> integer               -> Año de publicacion
- libro_edi -> character varying(20) -> Editorial del libro
- libro_ciu -> character varying(20) -> Ciudad en la que se publico
- libro_can -> integer               -> Cantidad de libros
- libro_prc -> integer               -> Precio de compra
- libro_prv -> integer               -> Precio de venta



