# Generated by Django 2.2.1 on 2019-05-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0011_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='varification_balance',
            name='upload_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
