# Generated by Django 2.2.1 on 2019-05-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0003_auto_20190523_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='varification_balance',
            name='upload_file',
            field=models.FileField(null=True, upload_to='Varification_balance/'),
        ),
    ]
