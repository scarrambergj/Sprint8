# Generated by Django 4.1 on 2022-08-31 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0007_alter_cliente_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='branch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='Clientes.sucursal'),
        ),
    ]
