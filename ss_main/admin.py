from django.contrib import admin
from .models import Shirt


# Register your models here.


class ShirtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating')
    search_fields = ('id', 'title', 'rating', 'tegs')
    exclude = ()

    class Meta:
        model = Shirt


admin.site.register(Shirt, ShirtAdmin)