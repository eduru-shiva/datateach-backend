from django.http import JsonResponse
from django.contrib import admin
from django.urls import path, include

def home_view(request):
    return JsonResponse({"message": "Welcome to DataTeach Backend API"})

urlpatterns = [
    path('', home_view),  # root URL
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
