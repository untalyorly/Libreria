from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import formulario

# Inicializamos
app = Flask(__name__)
# Estrablecemos conexion a la base de datos que esta alojada en Heroku 
conexion = psycopg2.connect(dbname="d7ort2krdktr8",
                            user="ubqatqumfpxvoe", 
                            password="de4650e1c018a208792346b62f5bcc2b753e04ee4564c78accb48ce7faad986c", 
                            host="ec2-35-172-85-250.compute-1.amazonaws.com", port="5432")
# configuracion
app.secret_key = "mysecretkey"

class inventario:
    # rutas
    #Ruta Inicio(menu)
    @app.route('/')
    def Index():
        cur = conexion.cursor()
        cur.execute('SELECT * FROM tmovlibinv')#buscamos todos los datos de la tabla
        data = cur.fetchall()
        cur.close()
        return render_template('FRM-Menu.html', libros=data)#enviamos para mostrarlos

    #Ruta formulario Ingresar Datos     #Agregar nuevos libros
    @app.route('/ingresar', methods=['POST', 'GET'])
    def Ingresar():
        formularios= formulario.Contenido_formulario(request.form)
        if request.method == 'POST' and formularios.validate():
            codigo = formularios.codigo.data
            nombre= formularios.nombre.data
            categoria = formularios.categoria.data
            autor = formularios.autor.data
            año = formularios.anio.data
            editorial = formularios.editorial.data
            ciudad = formularios.ciudad.data
            cantidad = formularios.cantidad.data
            precio_compra = formularios.precio_compra.data
            precio_venta = formularios.precio_venta.data
            cur = conexion.cursor()
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_cod = '{0}')" .format(codigo))
            veri = cur.fetchall()
            if veri == [(True,)]:
                flash('El Codigo ya existe','error')
                return render_template('FRM-Ingreso.html', form=formularios)
            else:
                cur.execute("INSERT INTO tmovlibinv (libro_cod, libro_nom, libro_cat, libro_aut, libro_año, libro_edi, libro_ciu, libro_can, libro_prc, libro_prv) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                                    (codigo, nombre, categoria, autor, año, editorial, ciudad, cantidad, precio_compra, precio_venta))
                conexion.commit()
                flash('Agregado Correctamente','success')
                return render_template('FRM-Ingreso.html', form=formularios)
        return render_template('FRM-Ingreso.html', form=formularios)

    #Ruta formulario Consultar Datos
    @app.route('/consultar', methods=['POST', 'GET'])
    def Consultar():
        return render_template('FRM-Consulta.html', libros=[0])

    #Ruta formulario Modificar Datos
    @app.route('/modificar', methods=['POST', 'GET'])
    def Modificar():
        return render_template('FRM-Modificar.html', libros=[])

    #Ruta formulario Eliminar Datos
    @app.route('/eliminar', methods=['POST', 'GET'])
    def Eliminar():
        return render_template('FRM-Eliminar.html', libros=[0])



    #Consultar libros
    @app.route('/cosulta_libro', methods=['POST', 'GET'])
    def cosulta_libro():
        if request.method == 'POST':
            codigo = request.form['codigo']
            nombre = request.form['nombre']
            categoria = request.form['categoria']
            autor = request.form['autor']
        cur = conexion.cursor()
        if codigo != "":
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_cod = '{0}')" .format(codigo))
            veri = cur.fetchall()
            if veri == [(True,)]:
                cur.execute("SELECT * FROM tmovlibinv WHERE libro_cod = '{0}'" .format(codigo))
                data = cur.fetchall()
                return render_template('FRM-Consulta.html', libros=data)
            else:
                flash('No existe el dato','error')
                return render_template('FRM-Consulta.html')
        if nombre != "":
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_nom = '{0}')" .format(nombre))
            veri = cur.fetchall()
            if veri == [(True,)]:
                cur.execute("SELECT * FROM tmovlibinv WHERE libro_nom = '{0}'" .format(nombre))
                data = cur.fetchall()
                return render_template('FRM-Consulta.html', libros=data)
            else:
                flash('No existe el dato','error')
                return render_template('FRM-Consulta.html')
        if categoria != "":
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_cat = '{0}')" .format(categoria))
            veri = cur.fetchall()
            if veri == [(True,)]:
                cur.execute("SELECT * FROM tmovlibinv WHERE libro_cat = '{0}'" .format(categoria))
                data = cur.fetchall()
                return render_template('FRM-Consulta.html', libros=data)
            else:
                flash('No existe el dato','error')
                return render_template('FRM-Consulta.html')
        if autor != "":
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_aut = '{0}')" .format(autor))
            veri = cur.fetchall()
            if veri == [(True,)]:
                cur.execute("SELECT * FROM tmovlibinv WHERE libro_aut = '{0}'" .format(autor))
                data = cur.fetchall()
                return render_template('FRM-Consulta.html', libros=data)
            else:
                flash('No existe el dato','error')
                return render_template('FRM-Consulta.html')
        flash('Debe llenar al menos un campo','error')
        return render_template('FRM-Consulta.html')

    #Modificar libros
    @app.route('/modifica_libro', methods=['POST', 'GET'])
    def modifica_libro():
        if request.method == 'POST':
            codigo = request.form['codigo']
        cur = conexion.cursor()
        if codigo != "":
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_cod = '{0}')" .format(codigo))
            veri = cur.fetchall()
            if veri == [(True,)]:
                cur.execute("SELECT * FROM tmovlibinv WHERE libro_cod = '{0}'" .format(codigo))
                data = cur.fetchall()
                cur.close()
                print(data)
                return render_template('FRM-Modificar.html', libros=data[0])
            else:
                flash('No existe el dato','error')
                return render_template('FRM-Modificar.html', libros=[])  
        flash('Debe llenar el campo','error')
        return render_template('FRM-Modificar.html', libros=[])

    #Actualizar datos del libro
    @app.route('/actualiza/<codigo>', methods=['POST'])
    def actualiza_libro(codigo):
        if request.method == 'POST':
            codigo = request.form['codigo']
            nombre = request.form['nombre']
            categoria = request.form['categoria']
            autor = request.form['autor']
            año = request.form['año']
            editorial = request.form['editorial']
            ciudad = request.form['ciudad']
            cantidad = request.form['cantidad']
            precio_compra = request.form['precio_compra']
            precio_venta = request.form['precio_venta']
            cur = conexion.cursor()
            cur.execute("""UPDATE tmovlibinv SET libro_cod = %s, libro_nom = %s, libro_cat = %s, libro_aut = %s, libro_año = %s,
                libro_edi = %s,
                libro_ciu = %s,
                libro_can = %s,
                libro_prc = %s,
                libro_prv = %s WHERE libro_cod = %s """, 
                (codigo, nombre, categoria, autor, año, editorial, ciudad, cantidad, precio_compra, precio_venta, codigo))
            flash('Actualizado Correctamente','success')
            conexion.commit()
            return redirect(url_for('Modificar'))

    #Buscar libro a eliminar
    @app.route('/consulta_libro_eliminar', methods=['POST', 'GET'])
    def consulta_libro_eliminar():
        if request.method == 'POST':
            codigo = request.form['codigo']
        cur = conexion.cursor()
        if codigo != "":
            cur.execute("SELECT EXISTS( SELECT * FROM tmovlibinv WHERE libro_cod = '{0}')" .format(codigo))
            veri = cur.fetchall()
            if veri == [(True,)]:
                cur.execute("SELECT * FROM tmovlibinv WHERE libro_cod = '{0}'" .format(codigo))
                data = cur.fetchall()
                return render_template('FRM-Eliminar.html', libros=data)
            else:
                flash('No existe el dato','error')
                return render_template('FRM-Eliminar.html')
        flash('Debe llenar el campo','error')
        return render_template('FRM-Eliminar.html')

    #Eliminar libro
    @app.route('/borrar/<codigo>', methods=['POST', 'GET'])
    def eliminar_libro(codigo):
        cur = conexion.cursor()
        cur.execute("DELETE FROM tmovlibinv WHERE libro_cod = '{0}'" .format(codigo))
        conexion.commit()
        flash('Borrado Correctamente','success')
        return redirect(url_for('Eliminar'))


#Iniciamos la aplicacion en el puerto 3000
if __name__ == "__main__":
    app.run(port=5000, debug=False)
