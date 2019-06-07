from django.contrib import admin
from StoreApp.models import User, Company, Chart_Of_Account, Group, SubGroup, Varification_balance

# Register your models here.

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Chart_Of_Account)
admin.site.register(Group)
admin.site.register(SubGroup)
admin.site.register(Varification_balance)