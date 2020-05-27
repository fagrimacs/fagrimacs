from django.urls import path

from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.AdminHomeView.as_view(), name='admin-homepage'),
    path('profile/<int:pk>/', views.AdminProfileView.as_view(), name='admin-profile'),
    path('profile/<int:pk>/update/', views.AdminProfileUpdateView.as_view(), name='admin-profile-update'),
    path('farmers/list', views.FarmersListView.as_view(), name='farmer-list'),
    path('owners/list', views.OwnersListView.as_view(), name='owner-list'),
    path('register/farmer', views.register_farmer, name='register-farmer'),
    path('register/owner', views.register_owner, name='register-owner'),
    path('export/farmer/csv/', views.export_farmers_csv, name='export-farmers-csv'),
    path('export/owner/csv/', views.export_owners_csv, name='export-owners-csv'),
]
