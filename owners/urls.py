from django.urls import path

from . import views

app_name = 'owners'

urlpatterns = [
    path('', views.OwnerHomeView.as_view(), name='owner-homepage'),
    path('profile/<int:pk>/', views.OwnerProfileView.as_view(), name='owner-profile'),
    path('profile/<int:pk>/update/', views.OwnerProfileUpdateView.as_view(), name='owner-profile-update'),
]
