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

from django.contrib import admin

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('fecha_hr_turno', 'autorizado', 'get_paciente_nombre', 'get_paciente_apellido', 'get_medico_nombre', 'get_medico_apellido', 'get_cobertura_usuario', 'get_asignacion_consultorio')

    def get_paciente_nombre(self, obj):
        return obj.id_rol_usu.first_name if obj.id_rol_usu else None
    get_paciente_nombre.short_description = 'Nombre del Paciente'

    def get_paciente_apellido(self, obj):
        return obj.id_rol_usu.last_name if obj.id_rol_usu else None
    get_paciente_apellido.short_description = 'Apellido del Paciente'

    def get_medico_nombre(self, obj):
        return obj.id_asig_cons.id_espec_usu.id_rol_usu.first_name if obj.id_asig_cons and obj.id_asig_cons.id_espec_usu and obj.id_asig_cons.id_espec_usu.id_rol_usu else None
    get_medico_nombre.short_description = 'Nombre del Médico'

    def get_medico_apellido(self, obj):
        return obj.id_asig_cons.id_espec_usu.id_rol_usu.last_name if obj.id_asig_cons and obj.id_asig_cons.id_espec_usu and obj.id_asig_cons.id_espec_usu.id_rol_usu else None
    get_medico_apellido.short_description = 'Apellido del Médico'

    def get_cobertura_usuario(self, obj):
        return self.get_nom_cob(obj.id_cob_usu)
    get_cobertura_usuario.short_description = 'Cobertura del Usuario'

    def get_nom_cob(self, obj):
        id_cob_usu = getattr(obj, 'id_cob_usu', None)
        
        if id_cob_usu:
            id_plan_cob = getattr(id_cob_usu, 'id_plan_cob', None)

            if id_plan_cob:
                id_cob = getattr(id_plan_cob, 'id_cob', None)

                if id_cob:
                    return id_cob.nom_cob

        return None

    def get_asignacion_consultorio(self, obj):
        return obj.id_asig_cons.num_cons if obj.id_asig_cons else None
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
admin.site.register(FacturasOdontologicas, FacturasOdontologicasAdmin)