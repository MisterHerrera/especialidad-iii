from django.db import models
from proveedor.models import Proveedor
from categoria.models import Categoria

# Create your models here.
class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, verbose_name="ID", db_column="id_producto")
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20, db_column="nombre")
    precio_unitario = models.FloatField(db_column="precio_unitario")

    class Meta:
        db_table= "Producto"
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"
