"""dj110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from EADD_072 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^$', views.start, name='start'),
    url(r'^', include('WebApp.urls')),
    url(r'^login/$', views.login, {'template_name': 'registration/login.html',
                                   'redirect_authenticated_user': True}, name='login'),

    url(r'^.*logout/$', views.logout, {'template_name': 'registration/logout.html'}, name='logout'),

    url(r'^.*editprofile/$', views.editprofile, name='editprofile'),

    url(r'^successlogin/$', views.loginsuccess, name='loginsuccess'),

    url(r'^.*register/$', views.register.as_view(), name='register'),

]
