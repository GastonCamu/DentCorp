from django.contrib import admin
from DentCorpApp.models import User, Ciudades, Provincias, Coberturas, Cajas,CoberturasXUsuario,Consultorios,AsignacionesConsultorio,Especialidades,EspecXUsuario,PagosServExt,FacturasServExt,ServiciosOdontologicos,Turnos,Planes,PlanXCobertura,FacturasOdontologicas
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name','dni_usu','dom_usu',)

class CiudadesAdmin(admin.ModelAdmin):
    list_display = ('nom_ciu','id_prov',)

    # def get_provincias (self, obj):
    #     return obj.id_prov_id.nombre_prov
    # get_provincias.short_description = 'Provincias'

class ProvinciasAdmin(admin.ModelAdmin):
    list_display = ('nom_prov',)

class CoberturasAdmin(admin.ModelAdmin):
    list_display = ('nom_cob',)

class CajasAdmin(admin.ModelAdmin):
    list_display = ('fecha_hr_ap_cj', 'fecha_hr_cr_cj', 'monto_ap_cj', 'monto_cr_cj', 'comentarios', 'id_rol_usu',)

class CoberturasXUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_plan_cob', 'id_rol_usu',)

class ConsultoriosAdmin(admin.ModelAdmin):
    list_display = ('num_cons',)

class AsignacionesConsultorioAdmin(admin.ModelAdmin):
    list_display = ('fecha_inicio_asig', 'fecha_fin_asig', 'get_consultorios', 'get_especialidades',)

    def get_consultorios(self, obj):
        return obj.id_cons_id.num_cons if obj.id_cons_id else None
    get_consultorios.short_description = 'Número de Consultorio'

    def get_especialidades(self, obj):
        return obj.id_espec_usu_id.id_espec.nombre_espec if obj.id_cons_usu_id else None
    get_especialidades.short_description = 'Especialidad'

class EspecialidadesAdmin(admin.ModelAdmin):
    list_display = ('nombre_espec',)

class EspecXUsuarioAdmin(admin.ModelAdmin):
    list_display = ('matricula',);

class PagosServExtAdmin(admin.ModelAdmin):
    list_display = ('nombre_serv', 'fecha_cad_cont',)

class FacturasServExtAdmin(admin.ModelAdmin):
    list_display = ('link_fact', 'costo_fact', 'fecha_cad_fact', 'fecha_pago_fact', 'comprobante_pago', 'id_caja', 'id_serv_ext',)

class ServiciosOdontologicosAdmin(admin.ModelAdmin):
    list_display = ('nombre_serv_odon', 'costo_serv_odon',)

class TurnosAdmin(admin.ModelAdmin):
    list_display = ('fecha_hr_turno', 'autorizado', 'get_servicio_odontologico', 'get_cobertura_usuario','get_plan_cob', 'get_rol_usuario', 'get_asignacion_consultorio',)

    def get_servicio_odontologico(self, obj):
        return obj.id_serv_odon.nombre_serv_odon if obj.id_serv_odon else None
    get_servicio_odontologico.short_description = 'Servicio'

    def get_cobertura_usuario(self, obj):
        return obj.id_cob_usu.id_plan_cob.id_cob.nom_cob if obj.id_cob_usu else None
    get_cobertura_usuario.short_description = 'Cobertura'

    def get_rol_usuario(self, obj):
        return obj.id_rol_usu.name if obj.id_rol_usu else None
    get_rol_usuario.short_description = 'Usuario'

    def get_asignacion_consultorio(self, obj):
        return obj.id_asig_cons.id_cons.num_cons
    get_asignacion_consultorio.short_desciption = 'Consultorio'

    def get_plan_cob(self,obj):
        return obj.id_cob_usu.id_plan_cob.id_plan.nombre_plan
    get_plan_cob.short_description = "Tipo de plan"

class PlanesAdmin(admin.ModelAdmin):
    list_display = ('nombre_plan',);

class PlanXCoberturaAdmin(admin.ModelAdmin):
    list_display = ('porcentaje_cob', 'id_plan', 'id_cob',)

    

class FacturasOdontologicasAdmin(admin.ModelAdmin):
    list_display = ('costo_fact_pac', 'costo_fact_cob', 'costo_total_fact_odon', 'fecha_fact_odon', 'id_turno', 'id_caja',)

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