from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contactos.db'
db = SQLAlchemy(app)

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

@app.route('/version1')
def index():
    return render_template('/version1/index.html')

@app.route('/version1/productos')
def productos():
    return render_template('/version1/productos.html')

@app.route('/version1/contacto.html', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        nuevo_contacto = Contacto(nombre=nombre, email=email, mensaje=mensaje)
        db.session.add(nuevo_contacto)
        db.session.commit()
        return '¡Gracias! Nos pondremos en contacto contigo pronto.'
    return render_template('version 1/contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
