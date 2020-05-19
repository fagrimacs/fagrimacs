from django.urls import path

from . import views

app_name = 'owners'

urlpatterns = [
    path('', views.OwnerHomeView.as_view(), name='owner-homepage'),
]
