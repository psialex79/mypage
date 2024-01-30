from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('currency_tracker.urls')),
    path('log-viewer/', include('log_viewer.urls')),
    path('users-checker/', include('users_checker.urls')),  
]
