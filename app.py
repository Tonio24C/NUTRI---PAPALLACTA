from flask import Flask, request, render_template
from python.conexion import insertar_datos

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def registrarForm():
    msg = ''
    if request.method == 'POST':
        nombre = request.form['fullname']
        correo = request.form['email']
        telefono = request.form['phone']
        asunto = request.form['affair']
        mensaje = request.form['message']

        # Llamando a la función insertar_datos para guardar los datos en la base de datos
        insertar_datos(nombre, correo, telefono, asunto, mensaje)

        msg = 'Registro con éxito'

        return render_template('index.html', msg='Formulario enviado correctamente')
    else:
        return render_template('index.html', msg='Método HTTP incorrecto')

if __name__ == '__main__':
    app.run(debug=True, port=5500)
