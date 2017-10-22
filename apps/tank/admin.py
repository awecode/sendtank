from django.contrib import admin

from .models import List, Campaign, Customer


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    search_fields = ('name', 'company__name')
    list_filter = ('company',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('company')


admin.site.register(List, ListAdmin)


class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'list', 'company')
    search_fields = ('name', 'list__name', 'list__company__name')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('list__company')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'email', 'phone')


admin.site.register(Customer, CustomerAdmin)

admin.site.register(Campaign, CampaignAdmin)
