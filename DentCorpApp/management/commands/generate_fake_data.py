# En el archivo generate_fake_data.py dentro del directorio commands de tu aplicación

from django.core.management.base import BaseCommand
from faker import Faker
from DentCorpApp.models import *

class Command(BaseCommand):
    help = 'Genera datos ficticios y los guarda en la base de datos'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Genera Provincias
        provincias = [Provincias(nom_prov=fake.state()) for _ in range(5)]
        Provincias.objects.bulk_create(provincias)

        # Genera Ciudades relacionadas con Provincias
        ciudades = [Ciudades(nom_ciu=fake.city(), id_prov=Provincias.objects.order_by('?').first()) for _ in range(20)]
        Ciudades.objects.bulk_create(ciudades)

        # Genera Usuarios relacionados con Ciudades
        users = [User(
            email=fake.email(),
            fecha_alta_usu=fake.date_this_decade(),
            fecha_baja_usu=fake.date_this_decade(),
            dni_usu=fake.unique.random_number(9),
            nom_usu=fake.first_name(),
            ape_usu=fake.last_name(),
            dom_usu=fake.street_address(),
            tel_usu=fake.phone_number(),
            id_ciu=Ciudades.objects.order_by('?').first()
        ) for _ in range(50)]
        User.objects.bulk_create(users)

        # Genera Especialidades
        especialidades = [Especialidades(nombre_espec=fake.word()) for _ in range(10)]
        Especialidades.objects.bulk_create(especialidades)

        # Genera Consultorios
        consultorios = [Consultorios(num_cons=fake.unique.random_number(3)) for _ in range(15)]
        Consultorios.objects.bulk_create(consultorios)

        # Genera ServiciosOdontologicos
        servicios_odontologicos = [
            ServiciosOdontologicos(
                nombre_serv_odon=fake.word(),
                costo_serv_odon=fake.random_number(2)
            ) for _ in range(30)
        ]
        ServiciosOdontologicos.objects.bulk_create(servicios_odontologicos)

        # Genera Planes
        planes = [Planes(nombre_plan=fake.word()) for _ in range(5)]
        Planes.objects.bulk_create(planes)

        # Genera Coberturas
        coberturas = [Coberturas(nom_cob=fake.word()) for _ in range(15)]
        Coberturas.objects.bulk_create(coberturas)

        # Genera PagosServExt
        pagos_serv_ext = [
            PagosServExt(
                nombre_serv=fake.word(),
                fecha_cad_cont=fake.date_this_year()
            ) for _ in range(50)
        ]
        PagosServExt.objects.bulk_create(pagos_serv_ext)

        # Genera EspecXUsuario relacionados con User y Especialidades
        espec_x_usuarios = [
            EspecXUsuario(
                matricula=fake.unique.random_number(5),
                id_rol_usu=fake.random_element(elements=User.objects.all()),
                id_espec=fake.random_element(elements=Especialidades.objects.all())
            ) for _ in range(100)
        ]
        EspecXUsuario.objects.bulk_create(espec_x_usuarios)

        # Genera AsignacionesConsultorio relacionados con Consultorios y EspecXUsuario
        asignaciones_consultorio = [
            AsignacionesConsultorio(
                fecha_inicio_asig=fake.date_this_decade(),
                fecha_fin_asig=fake.date_this_decade(),
                id_cons=fake.random_element(elements=Consultorios.objects.all()),
                id_espec_usu=fake.random_element(elements=EspecXUsuario.objects.all())
            ) for _ in range(30)
        ]
        AsignacionesConsultorio.objects.bulk_create(asignaciones_consultorio)

        # Genera Cajas relacionados con User
        cajas = [
            Cajas(
                fecha_hr_ap_cj=fake.date_time_this_decade(),
                fecha_hr_cr_cj=fake.date_time_this_decade(),
                monto_ap_cj=fake.random_number(5),
                monto_cr_cj=fake.random_number(5),
                comentarios=fake.text(),
                id_rol_usu=fake.random_element(elements=User.objects.all())
            ) for _ in range(10)
        ]
        Cajas.objects.bulk_create(cajas)

        # Genera FacturasServExt relacionados con Cajas y PagosServExt
        facturas_serv_ext = [
            FacturasServExt(
                link_fact=fake.url(),
                costo_fact=fake.random_number(5),
                fecha_cad_fact=fake.date_this_year(),
                fecha_pago_fact=fake.date_this_year(),
                comprobante_pago=fake.boolean(),
                id_caja=fake.random_element(elements=Cajas.objects.all()),
                id_serv_ext=fake.random_element(elements=PagosServExt.objects.all())
            ) for _ in range(20)
        ]
        FacturasServExt.objects.bulk_create(facturas_serv_ext)

        # Genera PlanXCobertura relacionados con Planes y Coberturas
        planes_x_cobertura = [
            PlanXCobertura(
                porcentaje_cob=fake.random_number(3),
                id_plan=fake.random_element(elements=Planes.objects.all()),
                id_cob=fake.random_element(elements=Coberturas.objects.all())
            ) for _ in range(50)
        ]
        PlanXCobertura.objects.bulk_create(planes_x_cobertura)

        # Genera CoberturasXUsuario relacionados con User y PlanXCobertura
        coberturas_x_usuario = [
            CoberturasXUsuario(
                id_rol_usu=fake.random_element(elements=User.objects.all()),
                id_plan_cob=fake.random_element(elements=PlanXCobertura.objects.all())
            ) for _ in range(100)
        ]
        CoberturasXUsuario.objects.bulk_create(coberturas_x_usuario)

        # Genera Turnos relacionados con ServiciosOdontologicos, CoberturasXUsuario, AsignacionesConsultorio
        turnos = [
            Turnos(
                fecha_hr_turno=fake.date_time_this_decade(),
                autorizado=fake.boolean(),
                id_serv_odon=fake.random_element(elements=ServiciosOdontologicos.objects.all()),
                id_cob_usu=fake.random_element(elements=CoberturasXUsuario.objects.all()),
                id_rol_usu=fake.random_element(elements=User.objects.all()),
                id_asig_cons=fake.random_element(elements=AsignacionesConsultorio.objects.all())
            ) for _ in range(200)
        ]
        Turnos.objects.bulk_create(turnos)

        # Genera FacturasOdontologicas relacionados con Turnos y Cajas
        facturas_odontologicas = [
            FacturasOdontologicas(
                costo_fact_pac=fake.random_number(5),
                costo_fact_cob=fake.random_number(5),
                costo_total_fact_odon=fake.random_number(5),
                fecha_fact_odon=fake.date_time_this_decade(),
                id_turno=fake.random_element(elements=Turnos.objects.all()),
                id_caja=fake.random_element(elements=Cajas.objects.all())
            ) for _ in range(20)
        ]
        FacturasOdontologicas.objects.bulk_create(facturas_odontologicas)

        self.stdout.write(self.style.SUCCESS('Datos ficticios generados exitosamente'))