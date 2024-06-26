from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import AppDeploymentHistory


@api_view(['POST'])
@csrf_exempt
def create_deployment(request):
    push_detail = request.data.get("push_data")
    repo_detail = request.data.get("repository")
    try:
        AppDeploymentHistory.objects.create(
            app_name=repo_detail.get("name"),
            source_branch=repo_detail.get("repo_name"),
            build_tag=push_detail.get("tag"),
            pushed_at=push_detail.get("pushed_at"),
            build_status=repo_detail.get("status")
        )
        return Response({"message" : "SUCCESS"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"message" : f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
