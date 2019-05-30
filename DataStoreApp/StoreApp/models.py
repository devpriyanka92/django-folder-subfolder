from django.db import models
from django.core.validators import MaxValueValidator

class User(models.Model):
    user_id = models.IntegerField()
    user_firstname = models.TextField(null=True)
    user_lastname = models.TextField(null=True)

class Company(models.Model):
    company_id = models.IntegerField()
    company_name = models.TextField(null=True)
    fiscal_end_of_year = models.DateField()

class Chart_Of_Account(models.Model):
    field_id = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    field_account = models.CharField(max_length=100)
    field_account_libaccount = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)
    field_subtype = models.CharField(max_length=100)

class Group_subgroup(models.Model):
    field_id = models.AutoField(primary_key=True)
    groupparent_id = models.ForeignKey('self', on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100)

class Varification_balance(models.Model):
    field_id = models.BigIntegerField()
    field_account = models.CharField(max_length=100)
    company = models.CharField(null=True,max_length=100)
    debit = models.IntegerField()
    credit = models.IntegerField()
    fiscal_year = models.IntegerField()
    month = models.IntegerField()
    currency = models.TextField(null=True)
    upload_version = models.IntegerField()
    upload_file = models.FileField(upload_to='media', null=True, default="")