# Generated by Django 4.0.5 on 2022-07-08 11:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('casa', '0005_cuota_alter_inquilino_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuota',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cuota',
            name='modificado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='año',
            field=models.PositiveSmallIntegerField(default=2022),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='mes',
            field=models.CharField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')], default='enero', max_length=15),
        ),
        migrations.AlterField(
            model_name='cuota',
            name='monto',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuota_abonada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casa.cuota', verbose_name='Cuota')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casa.propietario', verbose_name='Propietario')),
            ],
        ),
    ]
