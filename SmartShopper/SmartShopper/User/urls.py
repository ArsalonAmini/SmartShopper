from . import views

app_name = 'User' 

urlpatterns = [
    url(r'^register/$', views.UserFormView.as_view(), name='register')
    ]