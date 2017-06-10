"""Tools URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from MainApp.views import *
from UserManagementApp.views import *
from django.http import HttpResponse

# index page
urlpatterns = [
    url(r'^$', main, name='main')
]
# user management
urlpatterns += [
    url(r'^user/login/$', login, name='login'),
    url(r'^user/logout/$', logout, name='logout'),
    url(r'^user/registration/$', registration, name='registration'),
    url(r'^user/stats/$', user_stats, name='user_stats'),
    url(r'^user/check_nickname/$', check_nickname, name='check_nickname'),
    url(r'^user/check_email/$', check_email, name='check_email')
]
# admin page
urlpatterns += [
    url(r'^admin/$', admin_page),
    url(r'^admin/delete/user/(\d+)$', delete_user)
]
# setting up robots.txt
urlpatterns += [
    url(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow:", content_type="text/plain"), name="robots_file")
]

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
