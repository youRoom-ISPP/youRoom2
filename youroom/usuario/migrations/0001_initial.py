# Generated by Django 2.2.18 on 2021-04-25 19:05

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioPerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('totalPuntos', models.BigIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('id_stripe', models.CharField(blank=True, default='', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaSuscripcion', models.DateField(auto_now_add=True)),
                ('fechaCancelacion', models.DateField(blank=True, null=True)),
                ('perfil', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.UsuarioPerfil')),
            ],
        ),
        migrations.CreateModel(
            name='ContadorVida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numVidasSemanales', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
                ('numVidasCompradas', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('estaActivo', models.BooleanField(default=True)),
                ('perfil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuario.UsuarioPerfil')),
            ],
        ),
    ]
