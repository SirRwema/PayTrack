from django.conf.urls import url
from django.contrib import admin
from blog_posts import views

app_name = 'blog_posts'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^edit/(?P<pk>\d+)$', views.post_update, name='post_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
]