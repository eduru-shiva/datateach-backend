from django.urls import path
from django.http import JsonResponse
from .views import test_view

def root_view(request):
    return JsonResponse({"message": "API root is working"})

urlpatterns = [
    path('', root_view),  # root endpoint
    path('test/', test_view),
]
