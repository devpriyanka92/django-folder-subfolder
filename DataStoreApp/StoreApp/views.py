from django.http import HttpResponse
from django.shortcuts import render, redirect
from StoreApp.models import User, Company, Chart_Of_Account, Group, Varification_balance, SubGroup
from django.contrib import messages
import xlrd
from django.core.files.base import File
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.validators import FileExtensionValidator
from django.db import IntegrityError
import openpyxl
import datetime
import calendar

# read excel data
def read_data(request):
	# record getting from creategroup.html
	query_results = Group.objects.all()
	
	if "GET" == request.method:
		return render(request, 'upload.html', {})
	else:
		excel_file = {}
		excel_file = request.FILES["excel_file"]
		
		wb = openpyxl.load_workbook(excel_file)

		worksheet = wb.active 
		# worksheet = wb["Liste de comptes"]

		excel_data = list()
		row_data = list()

		for row in worksheet.iter_rows():
			row_data = list()
			for cell in row:
				row_data.append(str(cell.value).replace("None", ""))
			excel_data.append(row_data)

	return render(request, 'grouping.html', {"excel_data":excel_data,"GroupData":query_results})
	
# data upload 
def dataupload(request):

	if request.method == 'POST':
		# Get the form data from the request.

		company = request.POST.get('company')
		account_software = request.POST.get('account_software')
		fiscal_year = request.POST.get('fiscal_year')
		fiscal_month = request.POST.get('fiscal_month')
		currency = request.POST.get('currency')
		upload_file = request.POST.get('myfile')

		# Create a new record with the data.
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
		# Save logic
		upload_data.save()

		# Add save success message
		messages.info(request, 'Data Saved')
	else:
		# error message
		messages.info(request, 'Uploading error')

	return render(request, 'progress.html')


# logic for creating group
def group_create(request):

	if request.method == 'POST':

		# Get the form data from the request.
		group_name = request.POST.get('group_name')
		
		# Create a new group with the data.
		upload_data = Group.objects.create(
			group_name = group_name,)

		upload_data.save()

		# Add save success message
		messages.info(request, 'Data Saved')
	else:
		# Add error message
		messages.info(request, 'Uploading error')

	return render(request, 'creategroup.html')

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
	# list for List Select Account software

	List = [ 'Acomba', 'Sage 50', 'QuickBooks Online']

	# list for year

	years = []
	for year in range(2015, (datetime.datetime.now().year+1)):
		years.append(year)

	# list for month
	month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

	#list for currency
	currency = [ 'Dollar - USD', 'Euro - Euro']

	return render(request, 'import_menu.html', {'ListAccount':List,'dateList':years, 'AllMonths':month, 'currency':currency})

# logic for show data 
def list_of_file(request):
	query_results = Varification_balance.objects.all()
	return render(request, 'list_of_file.html', {"AllData":query_results})

def progress(request):
	return render(request, 'list_of_file.html')

def table(request):
	return render(request, 'table.html')