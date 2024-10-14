import mongoengine as me
from cliente.models import Cliente

# Create your models here.
class Receta(me.Document):
    id_receta = me.IntField(primary_key=True, required=True, db_field="id_receta")
    id_cliente = me.ReferenceField(Cliente)
    nombre_doctor = me.StringField(db_field="nombre")
