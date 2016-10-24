from django.conf.urls import url
from . import views

app_name = 'item' 

urlpatterns = [
    # /music /
    url(r'^$', views.index, name='index'),
    #
    ]