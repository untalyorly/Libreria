#Validamos el formulario de ingresar un nuevo dato(libro)
from wtforms import Form, StringField,IntegerField, TextField, validators, DecimalField

class Contenido_formulario(Form):
    codigo = StringField('Codigo',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.length(min=5, max=5, message='Ingrese un Codigo de 5 caracteres')
                ])
    nombre = StringField('Nombre',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.length(min=3, max=20, message='Ingrese un Nombre con un minimo de 3 caracteres y maximo 20')
                ])
    categoria = StringField('Categoria',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.length(min=3, max=20, message='Ingrese una Categoria con un minimo de 3 caracteres y maximo 20')
                ])
    autor = StringField('Autor',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.length(min=3, max=20, message='Ingrese un Autor con un minimo de 3 caracteres y maximo 20')
                ])
    anio = IntegerField('Año',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.NumberRange(min=1000, max=2020, message='Error Año')
                ])
    editorial = StringField('Editorial',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.length(min=3, max=20, message='Ingrese una Editorial con un minimo de 3 caracteres y maximo 20')
                ])
    ciudad = StringField('Ciudad',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.length(min=3, max=20, message='Ingrese una Ciudad con un minimo de 3 caracteres y maximo 20')
                ])
    cantidad = IntegerField('Cantidad',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.NumberRange(min=1, message='Error, numero no valido')
                ])
    precio_compra = DecimalField('Precio Compra',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.NumberRange(min=1, message='Error, numero no valido')
                ])
    precio_venta = DecimalField('Precio Venta',
                [
                    validators.Required(message='Campo Requerido'),
                    validators.NumberRange(min=1, message='Error, numero no valido')
                ])
