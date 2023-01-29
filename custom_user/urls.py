from django.urls import path, include
from .import views
from django.contrib import admin


admin.site.site_header = 'Smart Outreach'                   
admin.site.index_title = 'Features area'            
admin.site.site_title = 'Smart Outreach'


urlpatterns = [
    path('sign-up', views.sign_up, name='sign-up'),
    path('accounts/login', views.redirect_login, name='sign-up'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('sign-in', views.sign_in, name='sign-in'),
    path('profile', views.profile, name='profile'),
    path('change_password', views.change_password, name='change_password'),
    path('test', views.test, name='test'),
    
    # path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),  
    path('', include('django.contrib.auth.urls')),

]