# Generated by Django 2.2.14 on 2021-12-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20211203_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('J', 'Jewelry'), ('W', 'Watches'), ('OW', 'Outwear')], max_length=2),
        ),
    ]
