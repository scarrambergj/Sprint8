# Generated by Django 4.1 on 2022-08-31 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0008_alter_cliente_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='branch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.sucursal'),
        ),
    ]
