from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ComingSoonView.as_view(), name='coming-soon'),
    path('', include('main.urls', namespace='main')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('farmer/', include('farmers.urls', namespace='farmers')),
    path('owner/', include('owners.urls', namespace='owners')),
    path('admins/', include('admins.urls', namespace='admins')),
]
