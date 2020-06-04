from django.urls import path

from . import views


app_name = 'equipments'

urlpatterns = [
    path('add/', views.ImplementView.as_view(), name='add-implement')

]
