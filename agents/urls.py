from django.conf.urls import url
from django.contrib import admin
from agents import views

app_name = 'agents'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.agent_list, name='agent_list'),
    url(r'^new$', views.agent_create, name='agent_new'),
    url(r'^edit/(?P<pk>\d+)$', views.agent_update, name='agent_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.agent_delete, name='agent_delete'),
]