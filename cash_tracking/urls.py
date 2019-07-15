from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'), 
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    url(r'^blog_posts/', include('blog_posts.urls', namespace='blog_posts')),
    url(r'^agents/', include('agents.urls', namespace='agents')),
    url(r'^clients/', include('clients.urls', namespace='clients')),
    url(r'^cashdrops/', include('cashdrops.urls', namespace='cashdrops')),
    
]
