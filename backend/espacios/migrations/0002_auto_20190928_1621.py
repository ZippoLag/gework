# Generated by Django 2.1.10 on 2019-09-28 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='alta_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='apellido_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='inactivo_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre_usuario',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='pass_usuario',
        ),
        migrations.AlterField(
            model_name='contrato',
            name='estrellas_contrato',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='puesto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='espacios.Puesto'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='resenia_contrato',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='espacios.Usuario'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='contrato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='espacios.Contrato'),
        ),
    ]
