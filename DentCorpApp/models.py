from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from DentCorp import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
import uuid

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='DentCorpApp_users_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='DentCorpApp_users_permissions')
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)
    email = models.EmailField(_('email adress'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL, self.image)
        
        return '{}{}'.format(settings.STATIC_URL, 'img/user-default.png')

class Especialidades(models.Model):
    nombre_espec = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_espec
    
class Consultorios(models.Model):
    num_cons = models.IntegerField(max_length=3)

class ServiciosOdontologicos(models.Model):
    nombre_serv_odon = models.CharField(max_length=20)
    costo_serv_odon = models.FloatField(max_length=10)

class Provincias(models.Model):
    nom_prov = models.CharField(max_length=50)

class Planes(models.Model):
    nombre_plan = models.CharField(max_length=20)

class Coberturas(models.Model):
    nom_cob = models.CharField(max_length=20)

class PagosServExt(models.Model):
    nombre_serv = models.CharField(max_length=50)
    fecha_cad_cont = models.DateField()

class Roles(models.Model):
    nombre_rol = models.CharField(max_length=50)

class Ciudades(models.Model):
    nom_ciu = models.CharField(max_length=20)
    id_prov = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING)

class Usuarios(models.Model):
    dni_usu = models.CharField(max_length=9)
    nom_usu = models.CharField(max_length=50)
    ape_usu = models.CharField(max_length=50)
    dom_usu = models.CharField(max_length=50)
    tel_usu = models.CharField(max_length=14)
    email_usu = models.EmailField()
    contra_usu = models.CharField(max_length=50)
    id_ciu = models.ForeignKey(Ciudades, on_delete=models.PROTECT)

class RolXUsuario(models.Model):
    fecha_alta_usu = models.DateField()
    fecha_baja_usu = models.DateField()
    id_usu = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    id_rol = models.ForeignKey(Roles, on_delete=models.DO_NOTHING)

class EspecXUsuario(models.Model):
    matricula = models.IntegerField()
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.PROTECT)
    id_espec = models.ForeignKey(Especialidades, on_delete=models.PROTECT, max_length=5)

class AsignacionesConsultorio(models.Model):
    fecha_inicio_asig = models.DateTimeField()
    fecha_fin_asig = models.DateTimeField()
    id_cons = models.ForeignKey(Consultorios, on_delete=models.PROTECT)
    id_espec_usu = models.ForeignKey(EspecXUsuario, on_delete=models.PROTECT)

class Cajas(models.Model):
    fecha_hr_ap_cj = models.DateTimeField()
    fecha_hr_cr_cj = models.DateTimeField()
    monto_ap_cj = models.FloatField()
    monto_cr_cj = models.FloatField()
    comentarios = models.CharField(max_length=100)
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.PROTECT)

class FacturasServExt(models.Model):
    link_fact = models.CharField(max_length=200)
    costo_fact = models.FloatField()
    fecha_cad_fact = models.DateField()
    fecha_pago_fact = models.DateField()
    comprobante_pago = models.BooleanField()
    id_caja = models.ForeignKey(Cajas, on_delete=models.PROTECT)
    id_serv_ext = models.ForeignKey(PagosServExt, on_delete=models.PROTECT)

class PlanXCobertura(models.Model):
    porcentaje_cob = models.IntegerField(max_length=3)
    id_plan = models.ForeignKey(Planes, on_delete=models.PROTECT)
    id_cob = models.ForeignKey(Coberturas, on_delete=models.PROTECT)

class CoberturasXUsuario(models.Model):
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.PROTECT)
    id_plan_cob = models.ForeignKey(PlanXCobertura, on_delete=models.PROTECT)

class Turnos(models.Model):
    fecha_hr_turno = models.DateTimeField()
    autorizado = models.BooleanField()
    id_serv_odon = models.ForeignKey(ServiciosOdontologicos, on_delete=models.PROTECT)
    id_cob_usu = models.ForeignKey(CoberturasXUsuario, on_delete=models.PROTECT)
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.PROTECT)
    id_asig_cons = models.ForeignKey(AsignacionesConsultorio, on_delete=models.PROTECT)

class FacturasOdontologicas(models.Model):
    costo_fact_pac = models.FloatField()
    costo_fact_cob = models.FloatField()
    costo_total_fact_odon = models.FloatField()
    fecha_fact_odon = models.DateTimeField()
    id_turno = models.ForeignKey(Turnos, on_delete=models.PROTECT)
    id_caja = models.ForeignKey(Cajas, on_delete=models.PROTECT)