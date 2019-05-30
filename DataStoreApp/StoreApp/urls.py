from django.urls import path
from django.conf.urls import url
from .import views
from .import data_views
from django.conf.urls.static import static
from django.conf import settings
from django.core.files.storage import FileSystemStorage

urlpatterns = [
	url(r'^data$', data_views.data, name='data'),
	url(r'^$', views.index, name='index'),
	url(r'^creategroup$', views.group_create, name='creategroup'),
	url(r'^function$', views.function, name='function'),
	url(r'^import_menu$', views.import_menu, name='import_menu'),
	url(r'^list_of_file$', views.Data_ListOfFileUpload, name='list_of_file'),
	url(r'^progress$', views.list_of_file, name='progress'),
	url(r'^grouping$', views.read_data, name='grouping'),

	url(r'^read_data$', views.read_data, name='read_data'),
	url(r'^dataupload$', views.dataupload, name='dataupload'),
	url(r'^group_create$', views.group_create, name='group_create'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)