from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('dashboard.urls') ),
    path("", include('custom_user.urls') ),
    # taildwin css 
    path("__reload__/", include("django_browser_reload.urls")),
]
