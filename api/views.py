from django.http import JsonResponse

def test_view(request):
    return JsonResponse({"message": "Hello from Railway + Django!"})
from django.shortcuts import render

# Create your views here.
