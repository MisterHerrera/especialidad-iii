from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True, verbose_name="ID", db_column="id_proveedor")
    nombre = models.CharField(max_length=20, unique=True, db_column="nombre")
    

    class Meta:
        db_table = "Proveedor"
        ordering = ["nombre"]
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"