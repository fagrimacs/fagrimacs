from django.contrib import admin

from .models import OwnerProfile


class OwnerProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'profile_pic', 'email_confirmed', )

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(OwnerProfile, OwnerProfileAdmin)