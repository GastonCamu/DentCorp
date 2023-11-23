from django.contrib import admin
from DentCorpApp.models import User, Ciudades, Provincias, Coberturas, Cajas,CoberturasXUsuario,Consultorios,AsignacionesConsultorio,Especialidades,EspecXUsuario,PagosServExt,FacturasServExt,ServiciosOdontologicos,Turnos,Planes,PlanXCobertura,FacturasOdontologicas
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'image', )

class CiudadesAdmin(admin.ModelAdmin):
    pass

class ProvinciasAdmin(admin.ModelAdmin):
    pass

class CoberturasAdmin(admin.ModelAdmin):
    pass

class CajasAdmin(admin.ModelAdmin):
    pass

class CoberturasXUsuarioAdmin(admin.ModelAdmin):
    pass

class ConsultoriosAdmin(admin.ModelAdmin):
    pass

class AsignacionesConsultorioAdmin(admin.ModelAdmin):
    pass

class EspecialidadesAdmin(admin.ModelAdmin):
    pass

class EspecXUsuarioAdmin(admin.ModelAdmin):
    pass

class PagosServExtAdmin(admin.ModelAdmin):
    pass

class FacturasServExtAdmin(admin.ModelAdmin):
    pass

class ServiciosOdontologicosAdmin(admin.ModelAdmin):
    pass

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('fecha_hr_turno', 'autorizado', 'get_servicio_odontologico', 'get_cobertura_usuario', 'get_rol_usuario', 'get_asignacion_consultorio')

    def get_servicio_odontologico(self, obj):
        return obj.id_serv_odon.nombre_serv_odon
    get_servicio_odontologico.short_description = 'Servicio Odontológico'

    def get_cobertura_usuario(self, obj):
        return obj.id_cob_usu.nom_cob
    get_cobertura_usuario.short_description = 'Cobertura del Usuario'

    def get_rol_usuario(self, obj):
        return obj.id_rol_usu.name if obj.id_rol_usu else None
    get_rol_usuario.short_description = 'Rol del Usuario'

    def get_asignacion_consultorio(self, obj):
        return obj.id_asig_cons.num_cons
    get_asignacion_consultorio.short_description = 'Número de Consultorio'

class PlanesAdmin(admin.ModelAdmin):
    pass

class PlanXCoberturaAdmin(admin.ModelAdmin):
    pass

class FacturasOdontologicasAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Ciudades, CiudadesAdmin)
admin.site.register(Provincias, ProvinciasAdmin)
admin.site.register(Coberturas, CoberturasAdmin)
admin.site.register(Cajas, CajasAdmin)
admin.site.register(CoberturasXUsuario, CoberturasXUsuarioAdmin)
admin.site.register(Consultorios, ConsultoriosAdmin)
admin.site.register(AsignacionesConsultorio, AsignacionesConsultorioAdmin)
admin.site.register(Especialidades, EspecialidadesAdmin)
admin.site.register(EspecXUsuario, EspecXUsuarioAdmin)
admin.site.register(PagosServExt, PagosServExtAdmin)
admin.site.register(FacturasServExt, FacturasServExtAdmin)
admin.site.register(ServiciosOdontologicos, ServiciosOdontologicosAdmin)
admin.site.register(Turnos, TurnosAdmin)
admin.site.register(Planes, PlanesAdmin)
admin.site.register(PlanXCobertura, PlanXCoberturaAdmin)
admin.site.register(Permission)