# Generated by Django 2.1.7 on 2019-04-16 22:43

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('maker', '0012_auto_20190416_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='testID',
            new_name='id',
        ),
    ]
