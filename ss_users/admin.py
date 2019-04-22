from django.contrib import admin
from .models import SSUser

# Register your models here.


class SSUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'confirm_email')
    search_fields = ('id', 'username', 'email', 'first_name', 'last_name')
    exclude = ()

    class Meta:
        model = SSUser


admin.site.register(SSUser, SSUserAdmin)
