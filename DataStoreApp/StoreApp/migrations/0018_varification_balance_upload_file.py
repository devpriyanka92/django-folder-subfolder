# Generated by Django 2.2.1 on 2019-06-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0017_remove_varification_balance_upload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='varification_balance',
            name='upload_file',
            field=models.FileField(default='', null=True, upload_to='media'),
        ),
    ]
