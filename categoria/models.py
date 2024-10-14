from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name="ID", db_column="id_categoria")
    nombre = models.CharField(unique=True, max_length=20, db_column="nombre")

    class Meta:
        db_table = "Categoria"
        ordering = ["nombre"]
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
    