from rest_framework import routers
from django.urls import path, include

from . import views

# router = routers.DefaultRouter()
# router.register(r'', views.dns_automationViewSet)

urlpatterns = [
    path('dns_automation', views.zoho_cloudfare_dns_automation),
    path('create_user', views.zoho_create_users),
    path('get_domains_zoho', views.get_domains_zoho_view),
]