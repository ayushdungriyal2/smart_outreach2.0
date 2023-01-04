from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, EditUserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser



# Create your views here.



def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name")
        company_name = request.POST.get("company_name")
        user = CustomUser.objects.create_user(email, password)

        if user is not None:
            current_user = CustomUser.objects.get(email=email)
            current_user.name = name
            current_user.company_name = company_name
            current_user.save()

            print(current_user.name)
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})



def logout_view(request):
    logout(request)


def sign_in(request):

    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = CustomUser.objects.get(email = email)
        if user.check_password(password):
            login(request, user)
        # user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)
            return redirect('/home')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {"form": form})


def profile(request):
    
    form = EditUserProfileForm(instance=request.user)

    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        session_token = request.POST.get("session_token")
        refresh_token = request.POST.get("refresh_token")
        zoho_domain = request.POST.get("zoho_domain")
        client_id = request.POST.get("client_id")
        client_secret = request.POST.get("client_secret")
        cloudfare_email = request.POST.get("cloudfare_email")
        cloudfare_auth_code = request.POST.get("cloudfare_auth_code")
        user.name = name
        user.email = email
        user.phone = phone
        user.session_token = session_token
        user.refresh_token = refresh_token
        user.zoho_domain = zoho_domain
        user.client_id = client_id
        user.client_secret = client_secret
        user.cloudfare_email = cloudfare_email
        user.cloudfare_auth_code = cloudfare_auth_code
        user.save()
        return redirect('home')

        # form = UserForm(data=request.POST, instance=request.user)

        


    return render(request, 'registration/profile.html',{"form":form})