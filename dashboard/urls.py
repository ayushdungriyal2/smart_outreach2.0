from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('add-domain-to-zoho-from-cloudfare', views.add_domain_to_zoho_from_cloudfare),
    path('create_bulk_users_in_zoho', views.create_bulk_users_in_zoho),
    path('create_bulk_users_in_zoho_smartlead', views.create_bulk_users_in_zoho_smartlead),
    path('dashboard', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='home'),

]
