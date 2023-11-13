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
    num_cons = models.CharField(max_length=3)

    def __str__(self):
        return self.num_cons

class ServiciosOdontologicos(models.Model):
    nombre_serv_odon = models.CharField(max_length=20)
    costo_serv_odon = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse('serviciosInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre_serv_odon}, {self.costo_serv_odon}'

class Provincias(models.Model):
    nom_prov = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_prov

class Planes(models.Model):
    nombre_plan = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_plan

class Coberturas(models.Model):
    nom_cob = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nom_cob

class PagosServExt(models.Model):
    nombre_serv = models.CharField(max_length=50)
    fecha_cad_cont = models.DateField()

    def get_absolute_url(self):
        return reverse('pagosServInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre_serv}, {self.fecha_cad_cont}'
    
class Roles(models.Model):
    nombre_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_rol

class Ciudades(models.Model):
    nom_ciu = models.CharField(max_length=20)
    id_prov = models.ForeignKey(Provincias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_ciu

class Usuarios(models.Model):
    dni_usu = models.CharField(max_length=9)
    nom_usu = models.CharField(max_length=50)
    ape_usu = models.CharField(max_length=50)
    dom_usu = models.CharField(max_length=50)
    tel_usu = models.CharField(max_length=14)
    email_usu = models.EmailField()
    contra_usu = models.CharField(max_length=50)
    id_ciu = models.ForeignKey(Ciudades, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('infoUsuarios', args=[str(self.id)])

    def __str__(self):
        return f'{self.dni_usu}, {self.nom_usu}, {self.ape_usu}, {self.dom_usu}, {self.tel_usu}, {self.email_usu}, {self.contra_usu}'
    
class RolXUsuario(models.Model):
    fecha_alta_usu = models.DateField()
    fecha_baja_usu = models.DateField()
    id_usu = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def get_absolte_url(self):
        return reverse ('infoRolXUsuario', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_alta_usu}, {self.fecha_baja_usu}'
    
class EspecXUsuario(models.Model):
    matricula = models.IntegerField()
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.CASCADE)
    id_espec = models.ForeignKey(Especialidades, on_delete=models.CASCADE, max_length=5)

    def get_absolute_url(self):
        return reverse('infoEspecXUsuario', args=[str(self.id)])

    def __str__(self):
        return self.matricula
    # consultaas ver

class AsignacionesConsultorio(models.Model):
    fecha_inicio_asig = models.DateTimeField()
    fecha_fin_asig = models.DateTimeField()
    id_cons = models.ForeignKey(Consultorios, on_delete=models.CASCADE)
    id_espec_usu = models.ForeignKey(EspecXUsuario, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('asignacionesConsultorio', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_inicio_asig}, {self.fecha_fin_asig}'

class Cajas(models.Model):
    fecha_hr_ap_cj = models.DateTimeField()
    fecha_hr_cr_cj = models.DateTimeField()
    monto_ap_cj = models.FloatField()
    monto_cr_cj = models.FloatField()
    comentarios = models.CharField(max_length=100)
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('infoCajas', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_hr_ap_cj}, {self.fecha_hr_cr_cj}, {self.monto_ap_cj}, {self.monto_cr_cj}, {self.comentarios}'

class FacturasServExt(models.Model):
    link_fact = models.CharField(max_length=200)
    costo_fact = models.FloatField()
    fecha_cad_fact = models.DateField()
    fecha_pago_fact = models.DateField()
    comprobante_pago = models.BooleanField()
    id_caja = models.ForeignKey(Cajas, on_delete=models.CASCADE)
    id_serv_ext = models.ForeignKey(PagosServExt, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('infoFacturasServExt', args=[str(self.id)])

    def __str__(self):
        return f'{self.link_fact}, {self.costo_fact}, {self.fecha_cad_fact}, {self.fecha_pago_fact}, {self.comprobante_pago}'

class PlanXCobertura(models.Model):
    porcentaje_cob = models.Field(max_length=3)
    id_plan = models.ForeignKey(Planes, on_delete=models.CASCADE)
    id_cob = models.ForeignKey(Coberturas, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse ('infoPanXCobertura', args=[str(self.id)])

    def __str__(self):
        return self.porcentaje_cob

class CoberturasXUsuario(models.Model):
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.CASCADE)
    id_plan_cob = models.ForeignKey(PlanXCobertura, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('infoCoberturasXUsuario', args=[str(self.id)])


class Turnos(models.Model):
    fecha_hr_turno = models.DateTimeField()
    autorizado = models.BooleanField()
    id_serv_odon = models.ForeignKey(ServiciosOdontologicos, on_delete=models.CASCADE)
    id_cob_usu = models.ForeignKey(CoberturasXUsuario, on_delete=models.CASCADE)
    id_rol_usu = models.ForeignKey(RolXUsuario, on_delete=models.CASCADE)
    id_asig_cons = models.ForeignKey(AsignacionesConsultorio, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('infoTurnos', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_hr_turno}, {self.autorizado}'



class FacturasOdontologicas(models.Model):
    costo_fact_pac = models.FloatField()
    costo_fact_cob = models.FloatField()
    costo_total_fact_odon = models.FloatField()
    fecha_fact_odon = models.DateTimeField()
    id_turno = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    id_caja = models.ForeignKey(Cajas, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('facturasOdontologicas', args=[str(self.id)])

    def __str__(self):
        return f'{self.costo_fact_cob}, {self.costo_fact_pac}, {self.costo_total_fact_odon}'