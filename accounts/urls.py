from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup/farmer/', views.farmer_signup, name='farmer-signup'),
    path('signup/owner/', views.owner_signup, name='owner-signup'),
    path('signup/admin/', views.admin_signup, name='admin-signup'),
    path('confirm-email/<str:user_id>/<str:token>/', views.ConfirmRegistrationView.as_view(), name='confirm-email'),
]
