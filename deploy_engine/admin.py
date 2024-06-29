from django.contrib import admin
from .models import AppDeploymentHistory
# Register your models here.


class AppDeploymentHistoryDataPreview(admin.ModelAdmin):
    list_display = ('app_name', 'source_branch', 'pushed_at', 'build_status')  # List the fields you want to display

admin.site.register(AppDeploymentHistory, AppDeploymentHistoryDataPreview)
