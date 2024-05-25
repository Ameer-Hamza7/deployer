from django.urls import path
from .views import create_deployment


urlpatterns = [
    path('create_deployment', create_deployment, name="create_deployment"),
]
