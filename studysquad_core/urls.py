from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
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
