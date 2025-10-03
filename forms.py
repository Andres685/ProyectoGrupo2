from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    nombreUsuario = StringField("Nombre", validators=[DataRequired()])
    contactoUsuario = StringField("Contacto", validators=[DataRequired()])
    
    submit = SubmitField("Enviar")
