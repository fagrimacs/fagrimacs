from django.urls import path

from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin-homepage'),
    path('profile/<int:pk>/', views.AdminProfileView.as_view(), name='admin-profile'),
    path('profile/<int:pk>/update/', views.AdminProfileUpdateView.as_view(), name='admin-profile-update'),
    path('farmers/list/', views.FarmersListView.as_view(), name='farmer-list'),
    path('owners/list/', views.OwnersListView.as_view(), name='owner-list'),
    path('register/farmer/', views.RegisterFarmerView.as_view(), name='register-farmer'),
    path('register/owner/', views.RegisterOwnerView.as_view(), name='register-owner'),
    path('export/farmers/csv/', views.ExportFarmersCsv.as_view(), name='export-farmers-csv'),
    path('export/owners/csv/', views.ExportOwnersCsv.as_view(), name='export-owners-csv'),
]
