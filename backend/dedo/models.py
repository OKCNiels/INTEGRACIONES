from django.db import models

# Create your models here.
class DedoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length = 255)
    estado = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False)
  
    def __str__(self):
            return str(self.added_by)
    class Meta:
        db_table = '"mgcp_integraciones"."dedos"'    # Especifica el nombre de la tabla
        managed = False