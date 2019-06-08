from django.db import models
from django.core.validators import MaxValueValidator

# create your model here

# create user 
class User(models.Model):
    user_id = models.IntegerField()
    user_firstname = models.TextField(null=True)
    user_lastname = models.TextField(null=True)

# create company 
class Company(models.Model):
    company_id = models.IntegerField(default=170)
    company_name = models.TextField(null=True)
    fiscal_end_of_year = models.DateField()

# create chart_of_account
class Chart_Of_Account(models.Model):
    no_compte = models.BigIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    account = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)
    detailed_type = models.CharField(max_length=100)
    field_subtype = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

# create Group
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    # groupparent_id = models.ForeignKey('self', on_delete=models.CASCADE)
    group_name = models.CharField(max_length=100)

# create subGroup
class SubGroup(models.Model):
    subgroup_id = models.AutoField(primary_key=True)
    subgroup_name = models.CharField(max_length=100)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

# create Varification_balance
class Varification_balance(models.Model):
    field_id = models.BigIntegerField()
    field_account = models.CharField(max_length=200)
    company = models.CharField(max_length=200, default="")
    debit = models.IntegerField(default=170)
    credit = models.IntegerField(default=170)
    fiscal_year = models.IntegerField(default=170, null=True)
    month = models.IntegerField(default=170)
    currency = models.TextField(null=True)
    upload_version = models.IntegerField()
    upload_file = models.FileField(upload_to='media', null=True, default="")