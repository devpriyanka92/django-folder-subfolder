from django.http import HttpResponse
from django.shortcuts import render, redirect
from StoreApp.models import User, Company, Chart_Of_Account, Group_subgroup, Varification_balance
from django.contrib import messages
import xlrd
from django.core.files.base import File
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import openpyxl

def read_data(request):
	if "GET" == request.method:
		return render(request, 'upload.html', {})
	else:
		excel_file = {}
		excel_file = request.FILES["excel_file"]
		
		wb = openpyxl.load_workbook(excel_file)

		worksheet = wb["Liste de comptes"]
		excel_data = list()

		for row in worksheet.iter_rows():
			row_data = list()
			for cell in row:
				row_data.append(str(cell.value).replace("None", ""))
			excel_data.append(row_data)

	return render(request, 'grouping.html', {"excel_data":excel_data})
	
#------------------------------------------------------------------------------

def dataupload(request):

	if request.method == 'POST':
	
		company = request.POST.get('company')
		account_software = request.POST.get('account_software')
		fiscal_year = request.POST.get('fiscal_year')
		fiscal_month = request.POST.get('fiscal_month')
		currency = request.POST.get('currency')
		upload_file = request.POST.get('myfile')

		upload_data = Varification_balance.objects.create(
		company = company,
		field_account = account_software,
		fiscal_year = fiscal_year,
		month = fiscal_month,
		currency = currency,
		field_id = "000",
		debit = "000",
		credit = "000",
		upload_version = "000",
		upload_file = upload_file,
		)
		upload_data.save()

		messages.info(request, 'Data Saved')
	else:
		messages.info(request, 'Uploading error')

	return render(request, 'progress.html')

# -----------------------------------------------------------

# def formfield_for_foreignkey(self, Group_subgroup, request, **kwargs):
#     if Group_subgroup.groupparent_id == "groupparent_id":
#         kwargs['queryset'] = Group_subgroup.objects.exclude(pk=self.field_id)
#     return super(IdolAdmin, self).formfield_for_foreignkey(Group_subgroup, request, **kwargs)

def group_create(request):

	if request.method == 'POST':
	
		group_name = request.POST.get('group_name')
		group_available = request.POST.get('group_available')
		subgroup_name = request.POST.get('subgroup_name')

		upload_data = Group_subgroup.objects.create(
		
			groupparent_id = Group_subgroup.objects.exclude(pk=self.field_id),
			group_name = group_name,)

		upload_data.save()

		messages.info(request, 'Data Saved')
	else:
		messages.info(request, 'Uploading error')

	return render(request, 'creategroup.html')

#-------------------------------------------------------------

def Data_ListOfFileUpload(request):
    query_results = Varification_balance.objects.all()
    return render(request, 'list_of_file.html', {"AllData":query_results})

#--------------------------------------------------------------------

def upload(request):
	return render(request, 'upload.html')

def index(request):
	return render(request, 'index.html')

def grouping(request):
	return render(request, 'grouping.html')

def creategroup(request):
	return render(request, 'creategroup.html')

def function(request):
	return render(request, 'function.html')

def import_menu(request):
	return render(request, 'import_menu.html')

def list_of_file(request):
	return render(request, 'list_of_file.html')

def progress(request):
	return render(request, 'list_of_file.html')

def table(request):
	return render(request, 'table.html')