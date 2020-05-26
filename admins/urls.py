from django.urls import path

from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin-homepage'),
    path('farmers/list', views.FarmersView.as_view(), name='farmer-list'),
    path('owners/list', views.OwnersView.as_view(), name='owner-list'),
]
