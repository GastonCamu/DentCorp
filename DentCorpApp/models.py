from django.db import models
from django.contrib.auth.models import  AbstractUser, Group, Permission
from DentCorp import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
    
    
class Provincias(models.Model):
    nom_prov = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nom_prov}'

    class Meta:
        db_table = 'provincias'
        verbose_name_plural = "Provincias"

class Ciudades(models.Model):
    nom_ciu = models.CharField(max_length=20)
    id_prov = models.ForeignKey(Provincias, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nom_ciu} {self.id_prov.nom_prov}'

    class Meta:
        db_table = 'ciudades'
        verbose_name_plural = "Ciudades"

class User(AbstractUser):
    user_permissions = models.ManyToManyField(Permission, related_name='DentCorpApp_users_permissions')
    image = models.ImageField(upload_to='DentCorp\static\media\img', null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    fecha_alta_usu = models.DateField(null=True, blank=True)
    fecha_baja_usu = models.DateField(null=True, blank=True)
    dni_usu = models.CharField(max_length=9, verbose_name='DNI')
    dom_usu = models.CharField(max_length=50, verbose_name='Domicilio')
    tel_usu = models.CharField(max_length=14, verbose_name='teléfono' )
    id_ciu = models.ForeignKey(Ciudades, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Ciudad')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def get_absolute_url(self):
        return reverse('infoUsuarios', args=[str(self.id)])

    def __str__(self):
        return f'{self.dni_usu}, {self.dom_usu}, {self.tel_usu}, {self.email} '
    
    class Meta:
        db_table = 'users'
        verbose_name_plural = "Usuarios"
        
    
class Especialidades(models.Model):
    nombre_espec = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre_espec}'
    
    class Meta:
        db_table = 'especialidades'
        verbose_name_plural = "Especialidades"
    
class Consultorios(models.Model):
    num_cons = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.num_cons}'
    
    class Meta:
        db_table = 'consultorios'
        verbose_name_plural = "Consultorios"

class ServiciosOdontologicos(models.Model):
    nombre_serv_odon = models.CharField(max_length=20)
    costo_serv_odon = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse('serviciosInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre_serv_odon}, ${self.costo_serv_odon}'

    class Meta:
        db_table = 'servicios_odontologicos'
        verbose_name_plural = "Servicios Odontológicos"

class Planes(models.Model):
    nombre_plan = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.nombre_plan}'

    class Meta:
        db_table = 'planes'
        verbose_name_plural = "Planes"

class Coberturas(models.Model):
    nom_cob = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.nom_cob}'

    class Meta:
        db_table = 'coberturas'
        verbose_name_plural = "Coberturas"

class PagosServExt(models.Model):
    nombre_serv = models.CharField(max_length=50)
    fecha_cad_cont = models.DateField()

    def get_absolute_url(self):
        return reverse('pagosServInfo', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre_serv}, {self.fecha_cad_cont}'
    class Meta:
        db_table = 'pagos_serv_ext'
        verbose_name_plural = "Pagos de servicios"

    
class EspecXUsuario(models.Model):
    matricula = models.IntegerField()
    id_rol_usu = models.ForeignKey(Group, related_name='especialidad_usuario', on_delete=models.PROTECT, db_column='id_rol_usu')
    id_espec = models.ForeignKey(Especialidades, on_delete=models.PROTECT, max_length=5,db_column='id_espec')
    id_usu = models.ForeignKey(User, on_delete=models.PROTECT, related_name='especialidad_usuario', db_column='id_usu')

    def get_absolute_url(self):
        return reverse('infoEspecXUsuario', args=[str(self.id)])

    def __str__(self):
        return f'{self.matricula} {self.id_usu.first_name} {self.id_usu.last_name} {self.id_espec.nombre_espec} {self.id_rol_usu}'
    
    class Meta:
        db_table = 'espec_x_usuario'
        verbose_name_plural = "Especialidades por Usuario"

class AsignacionesConsultorio(models.Model):
    fecha_inicio_asig = models.DateTimeField()
    fecha_fin_asig = models.DateTimeField()
    id_cons = models.ForeignKey(Consultorios, on_delete=models.PROTECT)
    id_espec_usu = models.ForeignKey(EspecXUsuario, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('asignacionesConsultorio', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_inicio_asig}, {self.fecha_fin_asig} {self.id_cons.num_cons} {self.id_espec_usu.id_espec} {self.id_espec_usu.id_rol_usu} {self.id_espec_usu.id_usu.first_name} {self.id_espec_usu.id_usu.last_name}'
    
    class Meta:
        db_table = 'asignaciones_consultorio'
        verbose_name_plural = "Asignación de Consultorios"

class Cajas(models.Model):
    fecha_hr_ap_cj = models.DateTimeField()
    fecha_hr_cr_cj = models.DateTimeField()
    monto_ap_cj = models.FloatField()
    monto_cr_cj = models.FloatField()
    comentarios = models.CharField(max_length=100)
    id_rol_usu = models.ForeignKey(Group, related_name='cajas_roles', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('infoCajas', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_hr_ap_cj}, {self.fecha_hr_cr_cj}, {self.monto_ap_cj}, {self.monto_cr_cj}, {self.comentarios} {self.id_rol_usu}'
    
    class Meta:
        db_table = 'cajas'
        verbose_name_plural = "Cajas"

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

    def __str__(self):
        return f'{self.link_fact}, {self.costo_fact}, {self.fecha_cad_fact}, {self.fecha_pago_fact}, {self.comprobante_pago} {self.id_caja.id_rol_usu}'

    class Meta:
        db_table = 'facturas_serv_ext'
        verbose_name_plural = "Facturas de Servicios"


class PlanXCobertura(models.Model):
    porcentaje_cob = models.CharField(max_length=3)
    id_plan = models.ForeignKey(Planes, on_delete=models.PROTECT, db_column='id_plan')
    id_cob = models.ForeignKey(Coberturas, on_delete=models.PROTECT, db_column='id_cob')

    def get_absolute_url(self):
        return reverse ('infoPanXCobertura', args=[str(self.id)])

    def __str__(self):
        return f'{self.porcentaje_cob} {self.id_plan.nombre_plan} {self.id_cob.nom_cob}'

    class Meta:
        db_table = 'planesxcobertura'
        verbose_name_plural = "Planes x Coberturas"


class CoberturasXUsuario(models.Model):
    
    id_plan_cob = models.ForeignKey(PlanXCobertura, on_delete=models.PROTECT)
    id_rol_usu = models.ForeignKey(Group, related_name='coberturas_usuarios', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id_plan_cob} {self.id_rol_usu}'

    def get_absolute_url(self):
        return reverse('infoCoberturasXUsuario', args=[str(self.id)])
    
    class Meta:
        db_table = 'coberturas_x_usuario'


class Turnos(models.Model):
    fecha_hr_turno = models.DateTimeField( verbose_name='Fecha y hora del turno')
    autorizado = models.BooleanField(verbose_name='¿Esta autorizado?')
    id_serv_odon = models.ForeignKey(ServiciosOdontologicos, on_delete=models.PROTECT, verbose_name='servicio')
    id_cob_usu = models.ForeignKey(CoberturasXUsuario, on_delete=models.PROTECT, verbose_name='cobertura')
    id_rol_usu = models.ForeignKey(Group, related_name='turnos_usuarios', on_delete=models.PROTECT, verbose_name='rol')
    id_asig_cons = models.ForeignKey(AsignacionesConsultorio, on_delete=models.PROTECT, verbose_name='consultorio')
    id_usu = models.ForeignKey(User, on_delete=models.PROTECT, related_name='turnos_usuarios', db_column='id_usu', verbose_name='paciente')

    def get_absolute_url(self):
        return reverse('infoTurnos', args=[str(self.id)])

    def __str__(self):
        return f'{self.fecha_hr_turno}, {self.autorizado} {self.id_serv_odon.nombre_serv_odon} {self.id_cob_usu.id_plan_cob.id_cob.nom_cob} {self.id_cob_usu.id_plan_cob.id_plan.nombre_plan} {self.id_asig_cons.id_cons} {self.id_asig_cons.id_cons.num_cons}'

    class Meta:
        db_table = 'turnos'
        verbose_name_plural = "Turnos"

class FacturasOdontologicas(models.Model):
    costo_fact_pac = models.FloatField()
    costo_fact_cob = models.FloatField()
    costo_total_fact_odon = models.FloatField()
    fecha_fact_odon = models.DateTimeField()
    id_turno = models.ForeignKey(Turnos, on_delete=models.PROTECT)
    id_caja = models.ForeignKey(Cajas, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('facturasOdontologicas', args=[str(self.id)])

    def __str__(self):
        return f'{self.costo_fact_cob}, {self.costo_fact_pac}, {self.costo_total_fact_odon} {self.fecha_fact_odon} {self.id_turno.id_usu.first_name} {self.id_turno.id_usu.last_name} {self.id_caja}'
    
    class Meta:
        db_table = 'facturas_odontologicas'
        verbose_name_plural = "Facturas Odontológicas"