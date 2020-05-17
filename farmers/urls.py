from django.urls import path

from . import views

app_name = 'farmer'

urlpatterns = [
    path('', views.FarmerHomeView.as_view(), name='farmer-homepage'),
]
