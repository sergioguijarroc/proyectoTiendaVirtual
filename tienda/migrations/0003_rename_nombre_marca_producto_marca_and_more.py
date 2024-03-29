# Generated by Django 4.2.7 on 2024-01-11 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_alter_compra_options_alter_producto_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_marca',
            new_name='marca',
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('modelo', 'marca')},
        ),
    ]
