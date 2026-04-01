from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Expense Analyzer API is running 🚀")

urlpatterns = [
    path('', home),  # ✅ THIS FIXES YOUR 404
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # keep your existing api routing
]