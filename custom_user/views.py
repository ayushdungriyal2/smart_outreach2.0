from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, EditUserProfileForm, changePasswordForm, PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser, tempUsers
import requests
from django.core.mail import send_mail
from django.conf import settings
import uuid


def is_it_disposable(email):

    url = f"https://disposable.debounce.io/?email={email}"

    response = requests.request("GET", url).json()

    print(response)
    
    if response['disposable'] == 'true':
        print('true')
        return True
    else:
        return False


def ping_discord(email):
    url = "https://eo5fh1p01duvox9.m.pipedream.net/"

    body_json = {
        "email": f"{email}",
    }
    
    try:
        response = requests.request(
        "GET", url, json=body_json).json()

    except:
        pass


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

        if is_it_disposable(email) == True:
            error = 'Please use your work email'
            return render(request, 'registration/sign-up.html', context = {"form": form,"error":error})
        print(is_it_disposable(email))

        # --------------
        # create a user in tempuser table  
        auth_token = str(uuid.uuid4())
        temp_user = tempUsers(name=name,email=email,password=password,company_name=company_name,auth_token=auth_token)
        # save his details in temperoary table 
        temp_user.save()
        
        # send verification email 




        send_verification_email(email,auth_token)

        return HttpResponse('WE HAVE SENT YOU AN EMAIL WITH VERIFICATION CODE,CHECK IT OUT AND CONTINUE OVER THERE FUKC OFF FOR NOW')

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


def change_password(request):
    if request.user.is_authenticated:
    
        if request.method == 'POST':
            user = request.user
            if request.method == 'POST':
                new_password1 = request.POST.get('new_password1')
                user.set_password(new_password1)
                user.save()
                return redirect('sign-in')

            else:                
                return render(request, 'registration/password_change.html', {'form': form})
                
        form = changePasswordForm
        return render(request, 'registration/password_change.html', {'form': form})
    
    else:
        return redirect('sign-in')

    # ayush






def verify(request , auth_token):
    try:
        temp_user = tempUsers.objects.filter(auth_token = auth_token).first()
    
        if temp_user.verified == True:
                return redirect('sign-in')
            
        else:

            email = temp_user.email 
            password = temp_user.password
            user = CustomUser.objects.create_user(email, password)
            
            user = CustomUser.objects.get(email=email)
            user.name = temp_user.name
            user.company_name = temp_user.company_name
            user.save()
            temp_user.verified = True
            temp_user.auth_token = 'verified'
            
            temp_user.save()

            print(user.name)
            login(request, user)
            ping_discord(email)
            return redirect('/dashboard')
        

    except:
        return HttpResponse('The Verification Link Has Expired, Try Creating Account Again')






def send_verification_email(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


def password_reset_request(request):
    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    return redirect("homepage")
