from django.urls import path

from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin-homepage'),
    path('profile/<int:pk>/', views.AdminProfileView.as_view(), name='admin-profile'),
    path('profile/<int:pk>/update/', views.AdminProfileUpdateView.as_view(), name='admin-profile-update'),
    path('farmers/list', views.FarmersView.as_view(), name='farmer-list'),
    path('owners/list', views.OwnersView.as_view(), name='owner-list'),
]
