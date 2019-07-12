from django.conf.urls import url
from django.contrib import admin
from clients import views

app_name = 'clients'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.client_list, name='client_list'),
    url(r'^new$', views.client_create, name='client_new'),
    url(r'^edit/(?P<pk>\d+)$', views.client_update, name='client_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.client_delete, name='client_delete'),
]