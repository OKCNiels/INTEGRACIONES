# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClientesSoftlink(models.Model):
    tip_auxi = models.CharField(max_length=1, blank=True, null=True)
    cod_auxi = models.CharField(max_length=255, blank=True, null=True)
    nom_auxi = models.CharField(max_length=255, blank=True, null=True)
    dir_auxi = models.CharField(max_length=255, blank=True, null=True)
    tel_auxi = models.CharField(max_length=255, blank=True, null=True)
    doc_tipo = models.IntegerField(blank=True, null=True)
    ruc_auxi = models.CharField(max_length=255, blank=True, null=True)
    ult_edicion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_softlink'


class DistritosSb(models.Model):
    codigo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    provincia_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distritos_sb'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ejemplo(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejemplo'


class Evaluacion(models.Model):
    id_simulador = models.IntegerField(blank=True, null=True)
    oferta = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    resultado = models.CharField(max_length=255, blank=True, null=True)
    puntaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluacion'


class HistorialAcceso(models.Model):
    fecha = models.DateField(blank=True, null=True, db_comment='Fecha de la operacion')
    id_usuario = models.IntegerField(blank=True, null=True, db_comment='ID del usuario')
    ip = models.TextField(blank=True, null=True, db_comment='Direccion IP del equipo conectado')
    mac = models.TextField(blank=True, null=True, db_comment='Direccion MAC del equipo conectado')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_acceso'


class HistorialPeruCompras(models.Model):
    id_usuario = models.IntegerField()
    id_empresa = models.IntegerField()
    id_usuario_pc = models.IntegerField(blank=True, null=True)
    usuario_pc = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=50, blank=True, null=True)
    codigo_captcha = models.CharField(max_length=10, blank=True, null=True)
    fecha_conexion = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)
    cookie = models.TextField(blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    formulario = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_peru_compras'


class HistorialRenovacionClaves(models.Model):
    fecha = models.DateField(blank=True, null=True, db_comment='Fecha de renovacion')
    id_usuario = models.IntegerField(blank=True, null=True, db_comment='ID del usuario')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_renovacion_claves'


class LogActividadAcciones(models.Model):
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'log_actividad_acciones'


class LogsActividades(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_usuario = models.IntegerField()
    fecha = models.DateTimeField()
    formulario = models.CharField(max_length=255)
    id_accion = models.IntegerField()
    tabla = models.CharField(max_length=255, blank=True, null=True)
    valor_anterior = models.TextField(blank=True, null=True)
    nuevo_valor = models.TextField(blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_actividades'


class LogsLogin(models.Model):
    id_usuario = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    tipo_dispositivo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logs_login'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class MsGraphTokens(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    access_token = models.TextField()
    refresh_token = models.TextField(blank=True, null=True)
    expires = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ms_graph_tokens'


class Notificaciones(models.Model):
    id_usuario = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_usuario', db_comment='ID de usuario a quien se envi¾ la notificaci¾n')
    mensaje = models.TextField(db_comment='Mensaje')
    fecha = models.DateTimeField(db_comment='Fecha de la notificaci¾n')
    url = models.CharField(max_length=100, db_comment='URL para que pueda acceder a la notificaci¾n')
    leido = models.BooleanField(db_comment='Indicador si notificaci¾n fue leÝda')
    asunto = models.CharField(max_length=200, blank=True, null=True, db_comment='Asunto del mensaje: APROBACIËN CDP, RETIRO APROBACIËN DE CDP, APERTURA CDP')
    id_cc = models.IntegerField(blank=True, null=True, db_comment='ID cuadro de presupuesto')

    class Meta:
        managed = False
        db_table = 'notificaciones'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class ProveedoresSoftlink(models.Model):
    tip_auxi = models.CharField(max_length=1, blank=True, null=True)
    cod_auxi = models.CharField(max_length=255, blank=True, null=True)
    nom_auxi = models.CharField(max_length=255, blank=True, null=True)
    dir_auxi = models.CharField(max_length=255, blank=True, null=True)
    tel_auxi = models.CharField(max_length=200, blank=True, null=True)
    doc_tipo = models.IntegerField(blank=True, null=True)
    ruc_auxi = models.CharField(max_length=200, blank=True, null=True)
    ult_edicion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores_softlink'


class ProvinciasSb(models.Model):
    codigo = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    departamento_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'provincias_sb'


class Roles(models.Model):
    descripcion = models.CharField(max_length=100, db_comment='Descripci¾n del rol / permiso')
    id_tipo = models.ForeignKey('TiposRol', models.DO_NOTHING, db_column='id_tipo', db_comment='ID del tipo de rol')

    class Meta:
        managed = False
        db_table = 'roles'


class RolesUsuario(models.Model):
    id_usuario = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_usuario', db_comment='ID de usuario')
    id_rol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol', db_comment='ID del rol')

    class Meta:
        managed = False
        db_table = 'roles_usuario'


class Simulador(models.Model):
    part_number = models.CharField(max_length=100, blank=True, null=True, db_comment='Nro de parte del producto')
    tipo = models.IntegerField(blank=True, null=True, db_comment='Tipo de carga para el simulador')
    id_usuario = models.IntegerField(blank=True, null=True, db_comment='Usuario que registra el evento del simulador')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simulador'


class TiposRol(models.Model):
    tipo = models.CharField(max_length=50, db_comment='Tipo de rol')

    class Meta:
        managed = False
        db_table = 'tipos_rol'


class UserPasswordsHistorial(models.Model):
    user_id = models.IntegerField(blank=True, null=True, db_comment='Clave foranea del id de usuario')
    password = models.CharField(max_length=255, db_comment='Hash de la contrase±a')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha de creaci¾n')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha actualizaci¾n')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='Fecha Eliminaci¾n')

    class Meta:
        managed = False
        db_table = 'user_passwords_historial'


class Users(models.Model):
    name = models.CharField(max_length=255, db_comment='Nombre del usuario')
    email = models.CharField(unique=True, max_length=255, db_comment='Email, utilizado para iniciar sesi¾n')
    password = models.CharField(max_length=255, db_comment='Password encriptado del usuario')
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    nombre_corto = models.CharField(max_length=15, db_comment='Nombre corto del usuario (ejemplo: Wilmar G.)')
    activo = models.BooleanField(db_comment='N·mero de celular del usuario')
    celular_usuario = models.CharField(max_length=255, blank=True, null=True, db_comment='Utilizado para enviar mensajes por WhatsApp. Debe tener el c‗digo del paýs al inicio (51 para Per¨)')
    deleted_at = models.DateTimeField(blank=True, null=True)
    fecha_renovacion = models.DateField(blank=True, null=True, db_comment='Fecha de renovacion de clave')
    vendedor = models.BooleanField(blank=True, null=True, db_comment='Identificador que el usuario sea corporativo')
    renueva = models.BooleanField(blank=True, null=True, db_comment='Identificador de renovacion de clave')
    sap_id = models.CharField(blank=True, null=True, db_comment='Identificador de sap con el podremos editar y eliminar empleados')
    temp_token = models.CharField(max_length=200, blank=True, null=True)
    token_expiration = models.DateTimeField(blank=True, null=True)
    fingerprint_template = models.CharField(max_length=200, blank=True, null=True)
    login_huella = models.BooleanField(blank=True, null=True)
    habilitar_huella = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
