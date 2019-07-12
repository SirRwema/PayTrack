from django.conf.urls import url
from django.contrib import admin
from cashdrops import views

app_name = 'cashdrops'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.cashdrop_list, name='cashdrop_list'),
    url(r'^new$', views.cashdrop_create, name='cashdrop_new'),
    url(r'^edit/(?P<pk>\d+)$', views.cashdrop_update, name='cashdrop_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.cashdrop_delete, name='cashdrop_delete'),
]