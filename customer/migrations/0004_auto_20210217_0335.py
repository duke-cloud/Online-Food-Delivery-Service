# Generated by Django 2.2 on 2021-02-17 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_is_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='State',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='Street',
            new_name='street',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='zipcode',
            new_name='zip_code',
        ),
    ]
