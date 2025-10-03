from database import db
class Destinos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(60))
    ubicacion = db.Column(db.String(60))
    descripcion = db.Column(db.String(800))
    disponibilidad = db.Column(db.Boolean, default = True)
    precio = db.Column(db.Float, nullable = True)
    imagen = db.Column(db.String(1000))
    
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombreUsuario = db.Column(db.String(60))
    contactoUsuario = db.Column(db.String(60))