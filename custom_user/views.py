from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, EditUserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser


def sign_up(request):
    form = RegisterForm()
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        company_name = request.POST.get("company_name")

        # check if already email exists
        try:
            CustomUser.objects.get(email=email)
            error = 'Sorry That Email Already Exist'
            return render(request, 'registration/sign-up.html', context = {"form": form,"error":error})

        except:
            pass
        
        user = CustomUser.objects.create_user(email, password)
        

        if user is not None:
            current_user = CustomUser.objects.get(email=email)
            current_user.name = name
            current_user.company_name = company_name
            current_user.save()

            print(current_user.name)
            login(request, user)
            return redirect('/dashboard')
    else:

        return render(request, 'registration/sign-up.html', {"form": form})


def sign_in(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')

        else:
            context = {'error':'Incorrent email or password'}
            return render(request, 'registration/login.html', context=context)
            
            
    else:
        
        return render(request, 'registration/login.html')
    




def profile(request):
    
    form = EditUserProfileForm(instance=request.user)

    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        session_token = request.POST.get("session_token")
        # refresh_token = request.POST.get("refresh_token")
        # zoho_domain = request.POST.get("zoho_domain")
        # client_id = request.POST.get("client_id")
        # client_secret = request.POST.get("client_secret")
        cloudfare_email = request.POST.get("cloudfare_email")
        cloudfare_auth_code = request.POST.get("cloudfare_auth_code")
        smart_lead_api_key = request.POST.get("smart_lead_api_key") 
        user.name = name
        user.email = email
        user.phone = phone
        user.session_token = session_token
        # user.refresh_token = refresh_token
        # user.zoho_domain = zoho_domain
        # user.client_id = client_id
        # user.client_secret = client_secret
        user.cloudfare_email = cloudfare_email
        user.cloudfare_auth_code = cloudfare_auth_code
        user.smart_lead_api_key = smart_lead_api_key
        user.save()
        return redirect('dashboard')

    user = request.user

    if user.zoho_domain:
        zoho_oauth = True
    else:
        zoho_oauth = False
     
    return render(request, 'registration/profile.html',context = {"form":form, "zoho_oauth":zoho_oauth})