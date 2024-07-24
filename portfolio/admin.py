from django.contrib import admin
from .models import EmailTracking

@admin.register(EmailTracking)
class EmailTrackingAdmin(admin.ModelAdmin):
    list_display = ('email', 'tracking_id', 'opened', 'clicked', 'open_timestamp', 'click_timestamp')
    search_fields = ('email', 'tracking_id')
