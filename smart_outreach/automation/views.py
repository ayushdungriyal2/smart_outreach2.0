from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .main import main
from .main import get_domains_zoho as get_domains_zoho
# from django.contrib.auth.models import User
from ..user.models import CustomUser



@csrf_exempt
def zoho_cloudfare_dns_automation(request):

    if request.method == 'POST':
        print('got request')
        
        # collect request data
        request_data = JSONParser().parse(request)
        # -----------
        # get data via post request
        domain_name = request_data['domain_name']
        mail_1 = request_data['mail_1']
        mail_2 = request_data['mail_2']
        refresh_token = request_data['refresh_token']
        client_id = request_data['client_id']
        client_secret = request_data['client_secret']
        zoho_domain = request_data['zoho_domain']
        cloudfare_email = request_data['cloudfare_email']
        cloudfare_auth_code = request_data['cloudfare_auth_code']



        # execute the automation
        status = main.zoho_cloudfare_dns_automation(domain_name, mail_1, mail_2,refresh_token,client_id,client_secret,zoho_domain,cloudfare_email,cloudfare_auth_code)
        # send api response

        if status == True:
            response_data = {"status":"Done With The Dns Automation"}

        else:
            response_data = {"status" :"Some Error Occurred"}

        return JsonResponse(response_data)

    else:
        return JsonResponse({"Message": "Something Wen't Wrong🤒, Contact Support"})


# create user end point 

@csrf_exempt
def zoho_create_users(request):

    if request.method == 'POST':

        # collect request data
        request_data = JSONParser().parse(request)

        # user details form request
        email = request_data['email']
        name = request_data['name']
        password = request_data['password']

        refresh_token = request_data['refresh_token']
        client_id = request_data['client_id']
        client_secret = request_data['client_secret']
        zoho_domain = request_data['zoho_domain']

        # -----------

        # execute the automation
        status = main.zoho_create_users(refresh_token,client_id,client_secret,email,name,password, zoho_domain)
        # send api response

        if status == True:
            # # enable IMAP and active sync
            # from .main import  user_main
            # print()
            # user_main.enable_imap_active_s.enable_imap_active_s(refresh_token, org_id,zu_id, account_id, zoho_domain)

            response_data = {"status":"Done With The User Creation"}

        else:
            response_data = {"status" :"Some Error Occurred","error":f"{status}"}

        return JsonResponse(response_data)

    else:
        return JsonResponse({"Message": "Something Wen't Wrong🤒, Contact Support"})


@csrf_exempt
def get_domains_zoho_view(request):

    if request.method == 'POST':

        request_data = JSONParser().parse(request)
        # -----------
        # get data via post request
        refresh_token = request_data['refresh_token']
        client_id = request_data['client_id']
        client_secret = request_data['client_secret']
        zoho_domain = request_data['zoho_domain']

        zoho_domains = get_domains_zoho.get_domains_zoho(refresh_token,client_id,client_secret,zoho_domain)
        return JsonResponse(zoho_domains)

    else:
        return JsonResponse({'error':'400'})

