# Generated by Django 3.1 on 2022-10-16 01:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.user')),
                ('carnet_identidad', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Solo aceptan digitos')])),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'abstract': False,
            },
            bases=('user.user',),
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClienteEmpresa',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cliente.cliente')),
                ('nombre_empresa', models.CharField(max_length=100, unique=True)),
                ('direccion_empresa', models.TextField()),
                ('registro_empresa', models.CharField(max_length=100, unique=True)),
                ('telefono_empresa', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'abstract': False,
            },
            bases=('cliente.cliente',),
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cliente.cliente')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.clienteempresa')),
            ],
            options={
                'abstract': False,
            },
            bases=('cliente.cliente',),
            managers=[
                ('objects', user.models.CustomUserManager()),
            ],
        ),
    ]
