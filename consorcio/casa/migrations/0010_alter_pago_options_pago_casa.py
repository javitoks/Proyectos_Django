# Generated by Django 4.0.5 on 2022-07-11 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casa', '0009_alter_cuota_mes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pago',
            options={'ordering': ['casa'], 'verbose_name': 'Pago', 'verbose_name_plural': 'Pagos'},
        ),
        migrations.AddField(
            model_name='pago',
            name='casa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='casa.casa', verbose_name='Casa'),
            preserve_default=False,
        ),
    ]
