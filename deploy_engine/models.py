from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class AppDeploymentHistory(models.Model):
    BUILD_STATUS_CHOICES = (
        ("ST", "Start"),
        ("PE", "Pending"),
        ("SC", "SUCCESS"),
        ("FL", "FAILED"),
    )

    app_name = models.CharField(verbose_name=_("Application Name"), max_length=225, null=False, blank=False)
    source_branch = models.CharField(verbose_name=_("Source Branch"), max_length=225, null=False, blank=False)
    build_tag = models.CharField(verbose_name=_("Tag"), max_length=225, null=False, blank=False)
    build_status = models.CharField(verbose_name=_("Build Status"), max_length=225, choices=BUILD_STATUS_CHOICES)
    # encryption_key = models.CharField(verbose_name=_("Encryption Key") ,max_length=80)

    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     if self.encryption_key == 'ISTLuHpofl98vMOqGVOcQibqImtPCg1C':
    #         super(AppDeploymentHistory, self).save(*args, **kwargs)
    #     else:
    #         raise Exception("Invalid Key Provided.")
        
    def __str__(self) -> str:
        return self.app_name + ' == ' + self.source_branch + ' == ' + self.build_tag