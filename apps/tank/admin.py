from django.contrib import admin

from .models import List


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('company')


admin.site.register(List, ListAdmin)