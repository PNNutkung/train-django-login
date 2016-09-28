from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create_new_user/$', views.create_new_user, name='create_new_user'),
    url(r'^logout/', views.log_out, name='logout'),
]
