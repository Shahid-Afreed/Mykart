# Generated by Django 5.1.1 on 2024-10-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delete_status',
            field=models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')], default=1),
        ),
    ]
