import mongoengine as me

class Sequence(me.Document):
    name = me.StringField(required=True, unique=True)
    current_value = me.IntField(default=0)

    @classmethod
    def get_next_value(cls, name):
        sequence = cls.objects(name=name).modify(upsert=True, new=True, inc__current_value=1)
        return sequence.current_value

class Cliente(me.Document):
    id_cliente = me.IntField(primary_key=True, db_field="id_cliente", default=lambda: Sequence.get_next_value('cliente'))
    rut = me.StringField(unique=True, required=True)
    nombre = me.StringField(db_field="nombre")
    apellido = me.StringField(db_field="apellido")

