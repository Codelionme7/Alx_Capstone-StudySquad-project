from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <--- 1. Add this import
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # 2. Add this redirect line at the very top of your patterns
    path('', RedirectView.as_view(url='/api/docs/', permanent=False)),
    
    path('admin/', admin.site.urls),
    
    # StudySquad Endpoints
    path('api/users/', include('users.urls')),
    path('api/academics/', include('academics.urls')),
    path('api/scheduling/', include('scheduling.urls')),
    path('api/groups/', include('groups.urls')),
    
    # Auto-Generated API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]