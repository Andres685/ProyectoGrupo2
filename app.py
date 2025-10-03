from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from database import db
from forms import ContactForm
from model import Destinos, Usuarios 

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'un_secret_key_seguro'  # Necesario para CSRF de Flask-WTF

# Config DB
USUARIO = 'postgres'
PASSWORD = 'admin'
URL = 'localhost'
DATABASE = 'destinosbolivar'
FULL_LINK = f'postgresql://{USUARIO}:{PASSWORD}@{URL}/{DATABASE}'
app.config['SQLALCHEMY_DATABASE_URI'] = FULL_LINK
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def inicio():
    destinos = Destinos.query.all()
    form = ContactForm()
    return render_template("index.html", destinos=destinos, form=form)
@app.route("/registro", methods=['GET', 'POST'])
def registro():
    usuario = Usuarios()
    usuarioForm = ContactForm(obj = usuario)
    if request.method == 'POST':
        if usuarioForm.validate_on_submit():
            usuarioForm.populate_obj(usuario)
            db.session.add(usuario)
            db.session.commit()
            flash("Usuario registrado con éxito", "success")
    else:
        flash("Hubo un error en el formulario", "danger")
    return redirect(url_for("inicio"))