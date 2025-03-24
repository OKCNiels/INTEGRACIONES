from django.db import models

# Create your models here.
class UsuariomgcModel(models.Model):
    id = models.IntegerField(primary_key=True)    
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    nombre_corto = models.CharField(max_length=15)
    activo = models.BooleanField(default=False)
    celular_usuario = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_renovacion = models.DateField()
    vendedor = models.BooleanField(default=False)
    renueva = models.BooleanField(default=True)
    sap_id = models.CharField(max_length=255)
    temp_token = models.CharField(max_length=200)
    token_expiration = models.DateTimeField()
    fingerprint_template = models.CharField(max_length=200)
    login_huella = models.BooleanField(default=False,null=True, blank=True)
    habilitar_huella = models.BooleanField(default=True,null=True, blank=True)
  
    def __str__(self):
            return str(self.added_by)
    class Meta:
        db_table = '"mgcp_usuarios"."users"'    # Especifica el nombre de la tabla
        managed = False
    