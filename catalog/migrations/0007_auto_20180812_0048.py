# Generated by Django 2.1 on 2018-08-12 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180812_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
