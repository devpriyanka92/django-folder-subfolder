from django.contrib import admin
from StoreApp.models import User, Company, Chart_Of_Account, Group_subgroup, Varification_balance

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Chart_Of_Account)
admin.site.register(Group_subgroup)
admin.site.register(Varification_balance)