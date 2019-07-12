from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')), 
    url(r'^blog_posts/', include('blog_posts.urls', namespace='blog_posts')),
    url(r'^agents/', include('agents.urls', namespace='agents')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^cashdrops/', include('cashdrops.urls', namespace='cashdrops')),
    
]
