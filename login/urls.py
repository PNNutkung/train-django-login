from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main_page/$', views.login, name='main_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^create_new_user/$', views.create_new_user, name='create_new_user'),
]
