from django.urls import path

from . import views

app_name = 'farmers'

urlpatterns = [
    path('', views.FarmerHomeView.as_view(), name='farmer-homepage'),
    path('profile/<int:pk>/', views.FarmerProfileView.as_view(), name='farmer-profile'),
    path('profile/<int:pk>/update/', views.FarmerProfileUpdateView.as_view(), name='farmer-profile-update'),
]
