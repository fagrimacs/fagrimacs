from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ComingSoonView.as_view(), name='coming-soon'),
    path('', include('main.urls', namespace='main')),
    path('equipments/', include('equipments.urls', namespace='equipments')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('farmer/', include('farmers.urls', namespace='farmers')),
    path('owner/', include('owners.urls', namespace='owners')),
    path('equipment/', include('equipments.urls', namespace='equipments')),
    path('admins/', include('admins.urls', namespace='admins')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)