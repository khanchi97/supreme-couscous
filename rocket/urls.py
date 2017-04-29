from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns=[
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name':'rocket/login.html'}),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),



]