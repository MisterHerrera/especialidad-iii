import mongoengine as me
from cliente.models import Cliente

class Sequence(me.Document):
    name = me.StringField(required=True, unique=True)
    current_value = me.IntField(default=0)

    @classmethod
    def get_next_value(cls, name):
        sequence = cls.objects(name=name).modify(upsert=True, new=True, inc__current_value=1)
        return sequence.current_value
class Receta(me.Document):
    id_receta = me.IntField(primary_key=True, required=True, default=lambda: Sequence.get_next_value('receta'))
    id_cliente = me.ReferenceField(Cliente)
    nombre_doctor = me.StringField(db_field="nombre")