from django.urls import path

from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin-homepage'),
]
