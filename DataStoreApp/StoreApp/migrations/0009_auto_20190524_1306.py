# Generated by Django 2.2.1 on 2019-05-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0008_auto_20190524_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varification_balance',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
