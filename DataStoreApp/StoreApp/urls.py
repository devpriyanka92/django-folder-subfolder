from django.urls import path
from django.conf.urls import url
from .import views
from django.conf.urls.static import static
from django.conf import settings
from django.core.files.storage import FileSystemStorage

urlpatterns = [
	# Route for template
	url(r'^$', views.index, name='index'),
	url(r'^company$', views.company, name='company'),
	url(r'^creategroup$', views.group_create, name='creategroup'),
	url(r'^function$', views.function, name='function'),
	url(r'^Varification_balance$', views.Import_Varification_balance, name='Varification_balance'),
	url(r'^Chart_of_account$', views.Accounting_Chart_of_account, name='Chart_of_account'),
	url(r'^list_of_file$', views.list_of_file, name='list_of_file'),
	url(r'^progress$', views.list_of_file, name='progress'),
	url(r'^grouping$', views.read_data, name='grouping'),

	# Route for views(function)
	url(r'^read_data$', views.read_data, name='read_data'),
	url(r'^dataupload$', views.dataupload, name='dataupload'),
	url(r'^group_create$', views.group_create, name='group_create'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)