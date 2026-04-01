from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Expense Analyzer API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

def home(request):
    return HttpResponse("Expense Analyzer API is running 🚀")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # 🔥 MUST BE HERE
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]