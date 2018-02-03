"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from accounts import views
from django.contrib.auth.views import ( login, logout, password_reset, password_reset_done,
 password_reset_confirm, password_reset_complete )


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html', 'redirect_authenticated_user': True}),
    url(r'^logout/$', logout,{'next_page': 'index'}, name='logout'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    # url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    # url(r'^profile/change-password/$', views.change_password, name='change_password'),
    # url(r'^profile/reset-password/$', password_reset, name='reset_password'),
    # url(r'^profile/reset-password/done/$', password_reset_done, name='password_reset_done'),
    # url(r'^profile/reset-password/confirm/(?P<uidb64>[0-9A-ZA-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    # url(r'^profile/reset-password/complete/$', password_reset_complete, name='password_reset_complete'),



]
