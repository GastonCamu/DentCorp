from django.db import models
from django.contrib.auth.models import  AbstractUser, Group, Permission
from DentCorp import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
    
    
class Provincias(models.Model):
    nom_prov = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.nom_prov}'
    
class Ciudades(models.Model):
    nom_ciu = models.CharField(max_length=20)
    id_prov = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING)

    def _str_(self):
        return f'{self.nom_ciu}'


class User(AbstractUser):
    user_permissions = models.ManyToManyField(Permission, related_name='DentCorpApp_users_permissions')
    image = models.ImageField(upload_to='users/image', null=True, blank=True)
    # image = models.ImageField(upload_to='img/', null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    fecha_alta_usu = models.DateField(null=True, blank=True)
    fecha_baja_usu = models.DateField(null=True, blank=True)
    dni_usu = models.CharField(max_length=9)
    dom_usu = models.CharField(max_length=50)
    tel_usu = models.CharField(max_length=14)
    id_ciu = models.ForeignKey(Ciudades, null=True, blank=True, on_delete=models.PROTECT)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_image(self):
        if self.image:
            return '{}{}'.format(settings.MEDIA_URL, self.image)
        
        return '{}{}'.format(settings.STATIC_URL, 'img/user-default.png')
    
    def get_absolute_url(self):
        return reverse('infoUsuarios', args=[str(self.id)])

    def _str_(self):
        return f'{self.dni_usu}, {self.dom_usu}, {self.tel_usu}, {self.email}'
        
    
class Especialidades(models.Model):
    nombre_espec = models.CharField(max_length=50)

    def _str_(self):
        return f'{self.nombre_espec}'
    
class Consultorios(models.Model):
    num_cons = models.CharField(max_length=3)

    def _str_(self):
        return f'{self.num_cons}'

class ServiciosOdontologicos(models.Model):
    nombre_serv_odon = models.CharField(max_length=20)
    costo_serv_odon = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('serviciosInfo', args=[str(self.id)])

    def _str_(self):
        return f'{self.nombre_serv_odon}, {self.costo_serv_odon}'



class Planes(models.Model):
    nombre_plan = models.CharField(max_length=20)

    def _str_(self):
        return f'{self.nombre_plan}'

class Coberturas(models.Model):
    nom_cob = models.CharField(max_length=20)
    
    def _str_(self):
        return f'{self.nom_cob}'

class PagosServExt(models.Model):
    nombre_serv = models.CharField(max_length=50)
    fecha_cad_cont = models.DateField()

    def get_absolute_url(self):
        return reverse('pagosServInfo', args=[str(self.id)])

    def _str_(self):
        return f'{self.nombre_serv}, {self.fecha_cad_cont}'

    
class EspecXUsuario(models.Model):
    matricula = models.IntegerField()
    id_rol_usu = models.ForeignKey(Group, related_name='especialidad_usuario', on_delete=models.PROTECT)
    id_espec = models.ForeignKey(Especialidades, on_delete=models.PROTECT, max_length=5)

    def get_absolute_url(self):
        return reverse('infoEspecXUsuario', args=[str(self.id)])

    def _str_(self):
        return f'{self.matricula}'
    # consultaas ver

class AsignacionesConsultorio(models.Model):
    fecha_inicio_asig = models.DateTimeField()
    fecha_fin_asig = models.DateTimeField()
    id_cons = models.ForeignKey(Consultorios, on_delete=models.PROTECT)
    id_espec_usu = models.ForeignKey(EspecXUsuario, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('asignacionesConsultorio', args=[str(self.id)])

    def _str_(self):
        return f'{self.fecha_inicio_asig}, {self.fecha_fin_asig}'

class Cajas(models.Model):
    fecha_hr_ap_cj = models.DateTimeField()
    fecha_hr_cr_cj = models.DateTimeField()
    monto_ap_cj = models.FloatField()
    monto_cr_cj = models.FloatField()
    comentarios = models.CharField(max_length=100)
    id_rol_usu = models.ForeignKey(Group, related_name='cajas_roles', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('infoCajas', args=[str(self.id)])

    def _str_(self):
        return f'{self.fecha_hr_ap_cj}, {self.fecha_hr_cr_cj}, {self.monto_ap_cj}, {self.monto_cr_cj}, {self.comentarios}'

class FacturasServExt(models.Model):
    link_fact = models.CharField(max_length=200)
    costo_fact = models.FloatField()
    fecha_cad_fact = models.DateField()
    fecha_pago_fact = models.DateField()
    comprobante_pago = models.BooleanField()
    id_caja = models.ForeignKey(Cajas, on_delete=models.PROTECT)
    id_serv_ext = models.ForeignKey(PagosServExt, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('infoFacturasServExt', args=[str(self.id)])

    def _str_(self):
        return f'{self.link_fact}, {self.costo_fact}, {self.fecha_cad_fact}, {self.fecha_pago_fact}, {self.comprobante_pago}'

class PlanXCobertura(models.Model):
    porcentaje_cob = models.CharField(max_length=3)
    id_plan = models.ForeignKey(Planes, on_delete=models.PROTECT)
    id_cob = models.ForeignKey(Coberturas, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse ('infoPanXCobertura', args=[str(self.id)])

    def _str_(self):
        return f'{self.porcentaje_cob}'

class CoberturasXUsuario(models.Model):
    
    id_plan_cob = models.ForeignKey(PlanXCobertura, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('infoCoberturasXUsuario', args=[str(self.id)])


class Turnos(models.Model):
    fecha_hr_turno = models.DateTimeField()
    autorizado = models.BooleanField()
    id_serv_odon = models.ForeignKey(ServiciosOdontologicos, on_delete=models.PROTECT)
    id_cob_usu = models.ForeignKey(CoberturasXUsuario, on_delete=models.PROTECT)
    id_rol_usu = models.ForeignKey(Group, related_name='turnos_usuarios', on_delete=models.PROTECT)
    id_asig_cons = models.ForeignKey(AsignacionesConsultorio, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('infoTurnos', args=[str(self.id)])

    def _str_(self):
        return f'{self.fecha_hr_turno}, {self.autorizado}'

class FacturasOdontologicas(models.Model):
    costo_fact_pac = models.FloatField()
    costo_fact_cob = models.FloatField()
    costo_total_fact_odon = models.FloatField()
    fecha_fact_odon = models.DateTimeField()
    id_turno = models.ForeignKey(Turnos, on_delete=models.PROTECT)
    id_caja = models.ForeignKey(Cajas, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('facturasOdontologicas', args=[str(self.id)])

    def _str_(self):
        return f'{self.costo_fact_cob}, {self.costo_fact_pac}, {self.costo_total_fact_odon}'