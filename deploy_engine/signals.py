from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppDeploymentHistory
from .tasks import deployer_script


@receiver(post_save, sender=AppDeploymentHistory)  # Replace YourModel with your actual model
def handle_model_save(sender, instance, created, **kwargs):
  if created:
    print("handle_model_save ..........................", instance)
    deployer_script.delay()
