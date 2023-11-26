# Generated by Django 4.2.7 on 2023-11-26 02:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionesConsultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio_asig', models.DateTimeField()),
                ('fecha_fin_asig', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Asignación de Consultorios',
                'db_table': 'asignaciones_consultorio',
            },
        ),
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hr_ap_cj', models.DateTimeField()),
                ('fecha_hr_cr_cj', models.DateTimeField()),
                ('monto_ap_cj', models.FloatField()),
                ('monto_cr_cj', models.FloatField()),
                ('comentarios', models.CharField(max_length=100)),
                ('id_rol_usu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cajas_roles', to='auth.group')),
            ],
            options={
                'verbose_name_plural': 'Cajas',
                'db_table': 'cajas',
            },
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ciu', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
                'db_table': 'ciudades',
            },
        ),
        migrations.CreateModel(
            name='Coberturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_cob', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Coberturas',
                'db_table': 'coberturas',
            },
        ),
        migrations.CreateModel(
            name='CoberturasXUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'coberturas_x_usuario',
            },
        ),
        migrations.CreateModel(
            name='Consultorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cons', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Consultorios',
                'db_table': 'consultorios',
            },
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_espec', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Especialidades',
                'db_table': 'especialidades',
            },
        ),
        migrations.CreateModel(
            name='PagosServExt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_serv', models.CharField(max_length=50)),
                ('fecha_cad_cont', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Pagos de servicios',
                'db_table': 'pagos_serv_ext',
            },
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Planes',
                'db_table': 'planes',
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prov', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Provincias',
                'db_table': 'provincias',
            },
        ),
        migrations.CreateModel(
            name='ServiciosOdontologicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_serv_odon', models.CharField(max_length=20)),
                ('costo_serv_odon', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Servicios Odontológicos',
                'db_table': 'servicios_odontologicos',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('fecha_alta_usu', models.DateField(blank=True, null=True)),
                ('fecha_baja_usu', models.DateField(blank=True, null=True)),
                ('dni_usu', models.CharField(max_length=9)),
                ('dom_usu', models.CharField(max_length=50)),
                ('tel_usu', models.CharField(max_length=14, verbose_name='teléfono')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('id_ciu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.ciudades')),
                ('user_permissions', models.ManyToManyField(related_name='DentCorpApp_users_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hr_turno', models.DateTimeField()),
                ('autorizado', models.BooleanField()),
                ('id_asig_cons', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.asignacionesconsultorio')),
                ('id_cob_usu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.coberturasxusuario')),
                ('id_rol_usu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='turnos_usuarios', to='auth.group')),
                ('id_serv_odon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.serviciosodontologicos', verbose_name='servicios')),
                ('id_usu', models.ForeignKey(db_column='id_usu', on_delete=django.db.models.deletion.PROTECT, related_name='turnos_usuarios', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Turnos',
                'db_table': 'turnos',
            },
        ),
        migrations.CreateModel(
            name='PlanXCobertura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_cob', models.CharField(max_length=3)),
                ('id_cob', models.ForeignKey(db_column='id_cob', on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.coberturas')),
                ('id_plan', models.ForeignKey(db_column='id_plan', on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.planes')),
            ],
            options={
                'verbose_name_plural': 'Planes x Coberturas',
                'db_table': 'planesxcobertura',
            },
        ),
        migrations.CreateModel(
            name='FacturasServExt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_fact', models.CharField(max_length=200)),
                ('costo_fact', models.FloatField()),
                ('fecha_cad_fact', models.DateField()),
                ('fecha_pago_fact', models.DateField()),
                ('comprobante_pago', models.BooleanField()),
                ('id_caja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.cajas')),
                ('id_serv_ext', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.pagosservext')),
            ],
            options={
                'verbose_name_plural': 'Facturas de Servicios',
                'db_table': 'facturas_serv_ext',
            },
        ),
        migrations.CreateModel(
            name='FacturasOdontologicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_fact_pac', models.FloatField()),
                ('costo_fact_cob', models.FloatField()),
                ('costo_total_fact_odon', models.FloatField()),
                ('fecha_fact_odon', models.DateTimeField()),
                ('id_caja', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.cajas')),
                ('id_turno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.turnos')),
            ],
            options={
                'verbose_name_plural': 'Facturas Odontológicas',
                'db_table': 'facturas_odontologicas',
            },
        ),
        migrations.CreateModel(
            name='EspecXUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('id_espec', models.ForeignKey(db_column='id_espec', max_length=5, on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.especialidades')),
                ('id_rol_usu', models.ForeignKey(db_column='id_rol_usu', on_delete=django.db.models.deletion.PROTECT, related_name='especialidad_usuario', to='auth.group')),
                ('id_usu', models.ForeignKey(db_column='id_usu', on_delete=django.db.models.deletion.PROTECT, related_name='especialidad_usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Especialidades por Usuario',
                'db_table': 'espec_x_usuario',
            },
        ),
        migrations.AddField(
            model_name='coberturasxusuario',
            name='id_plan_cob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.planxcobertura'),
        ),
        migrations.AddField(
            model_name='coberturasxusuario',
            name='id_rol_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='coberturas_usuarios', to='auth.group'),
        ),
        migrations.AddField(
            model_name='ciudades',
            name='id_prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='DentCorpApp.provincias'),
        ),
        migrations.AddField(
            model_name='asignacionesconsultorio',
            name='id_cons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.consultorios'),
        ),
        migrations.AddField(
            model_name='asignacionesconsultorio',
            name='id_espec_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DentCorpApp.especxusuario'),
        ),
    ]
