import mongoengine as me

# Create your models here.
class Cliente(me.Document):
    id_cliente = me.IntField(primary_key=True, db_field="id_cliente")
    rut = me.StringField(unique=True, required=True)
    nombre = me.StringField(db_field="nombre")
    apellido = me.StringField(db_field="apellido")
