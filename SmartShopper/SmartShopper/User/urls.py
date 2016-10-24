from django.conf.urls import url
from . import views

app_name = 'user' 

urlpatterns = [
    # /SignUp/
    url(r'^$', views.index, name='index'),
    #url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /user/712/
    url(r'^(?P<SignUp_id>[0-9]+)$', views.detail, name='detail'), 
    ]