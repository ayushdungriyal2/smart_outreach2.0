from celery import current_app
from django.shortcuts import render, redirect, HttpResponse
from .tasks import get_domain_from_cloudfare, add_domain_to_zoho_request, create_user_zoho, get_domain_from_zoho,create_user_zoho_smartlead, verify_access_token,get_clients_access_token
import json
from celery.result import AsyncResult
from .main.main import get_access_token


# Create your views here.

def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        print(user.password)
        return render(request, 'dashboard/dashboard.html')

    else:
        return redirect('sign-in')



def add_domain_to_zoho_from_cloudfare(request):

    if request.user.is_authenticated:
        user = request.user

        # check if acess allowed
        user = request.user

        if user.access_allowed == False:
            return HttpResponse('ACCESS DENIED, Please Contact mail@rithikrajput.com To Get Access.')
        # check if access allowed

        # check if zoho is connected 
        if user.zoho_domain:
            zoho_oauth = True
        else:
            return render(request, 'dashboard/message.html',context={'heading':'Zoho Not Connected','message':'Please connect your cloudflare & Zoho At Profile'})
            # return render(request, 'dashboard/message.html',context={'heading':'Zoho Not Connected','message':'Please connect your cloudflare & Zoho At Profile'})

        # check if zoho is connected ends 

        if user.api_calls >=50:
            return HttpResponse('50/50 FREE CREDITS USED, Please Contact mail@rithikrajput.com to get more.')

        user = request.user
        refresh_token = user.refresh_token
        zoho_domain = user.zoho_domain
        client_id = user.client_id
        client_secret = user.client_secret


        # checking access token 
        access_token = user.access_token
                
        if verify_access_token(access_token,zoho_domain) == False:
            # refresh access token for zoho
            access_token = get_access_token(refresh_token, client_id, client_secret, zoho_domain)

            user.access_token = access_token
            user.save()

        # get list of domain on cloudfare 

        try:

            cloudfare_email = user.cloudfare_email
            cloudfare_auth_code = user.cloudfare_auth_code
            domain_list = get_domain_from_cloudfare (cloudfare_email, cloudfare_auth_code)

        except:
            print('WRONG CLOUDFARE CREDS')
            return render(request, 'dashboard/add-domain-to-zoho-from-cloudfare.html', context={"cloudfareStatus": False})

        # get list of domain on cloudfare ends

        if request.method == 'POST':
            mail_1 = request.POST.get('email_1')
            mail_2 = request.POST.get('email_2')

            if mail_2:
                pass
            else:
                mail_2 = 'test@test.com'

            if (mail_2 == None) or (mail_2== ''):
                mail_2 == 'test@test.com' 
            
            print(mail_1)
            print(mail_2)

            if mail_2 == None:
                mail_2 == 'test@none.com'

            select_domain_list = request.POST.get('select_domain_list')
            print(select_domain_list)

            select_domain_list = select_domain_list.split(',')
            print(select_domain_list) # selected domain from frontend

            # defingin celery task id dictionary 

            celery_task_id_dictionary = {'domain_name':[],'task_id':[]}

            # looping the automation for domains form front end 

            for domain_name in select_domain_list:

                # counting api calls 

                api_calls = user.api_calls
                api_calls = api_calls +1 
                user.api_calls = api_calls
                user.save()

            # making celery task dictionary and running the task 

                print(domain_name)
                task_id = add_domain_to_zoho_request.delay(access_token, domain_name, mail_1, mail_2, zoho_domain, cloudfare_email, cloudfare_auth_code)
        
                celery_task_id_dictionary['domain_name'].append(domain_name)
                celery_task_id_dictionary['task_id'].append(task_id.task_id)
                
                # saving domain name and task id in database 
                            
                user.celery_task_id_add_domain_list = json.dumps(celery_task_id_dictionary)
                user.save()

                import time
                check_loop = 0
                result = AsyncResult(task_id.task_id, app=current_app)
                while result.status != 'STARTED':
                    time.sleep(1)
                    check_loop += 1
                    if check_loop == 20:
                        break
        
        try:

            # fetching task status and task name from database 
            jsonDec = json.decoder.JSONDecoder()
            celery_task_id_list = jsonDec.decode(user.celery_task_id_add_domain_list)
            print(celery_task_id_list)

            # storing active tasks 
            active_task_domain_name = []

            # running a loop to check if tasks are active

            for domain_name, task_id in zip(celery_task_id_list['domain_name'], celery_task_id_list['task_id']):
                result = AsyncResult(task_id, app=current_app)
                print(result.status)
                if result.status == 'STARTED':
                    active_task_domain_name.append(domain_name)

                elif result.status == 'RECEIVED':
                    active_task_domain_name.append(domain_name)

                else:
                    pass

            print('----------')
            print(active_task_domain_name)

        except:
            active_task_domain_name = []
        
        return render(request, 'dashboard/add-domain-to-zoho-from-cloudfare.html', context = {"domain_list": domain_list,"active_task_domain_name":active_task_domain_name})

    else:
        return redirect('sign-in')

# ``````````````````````````````````````````

                        
def create_bulk_users_in_zoho(request):
    if request.user.is_authenticated:
        
        user = request.user
        # check if zoho is connected 
        if user.zoho_domain:
            pass
        else:
            return render(request, 'dashboard/message.html',context={'heading':'Zoho Not Connected','message':'Please connect your cloudflare & Zoho At Profile'})
            # return HttpResponse('Please connect your cloudflare & Zoho At <a href="/profile">Profile Page</a>')
        # check if zoho is connected ends 

        # check if acess allowed
        if user.api_calls >=50:
            return HttpResponse('50/50 FREE CREDITS USED, Please Contact mail@rithikrajput.com to get more.')
        if user.access_allowed == False:
            return HttpResponse('ACCESS DENIED, Please Contact mail@rithikrajput.com To Get Access.')
        # check if access allowed
            
        # get user's data from database 
        user = request.user
        refresh_token = user.refresh_token
        client_id = user.client_id
        client_secret = user.client_secret
        zoho_domain = user.zoho_domain

        # checking access token 
        access_token = user.access_token
        if verify_access_token(access_token,zoho_domain) == False:
                    
            # refresh access token for zoho
            access_token = get_access_token(refresh_token, client_id, client_secret, zoho_domain)
                    
            user.access_token = access_token
            user.save()

        # get list of domain on zoho 

        try:
    
            domain_list = get_domain_from_zoho(refresh_token,client_id,client_secret,zoho_domain)

        except:
                print('WRONG CLOUDFARE CREDS')
                return render(request, 'dashboard/create_bulk_users_in_zoho.html', context={"error": "please see if you have added proper cloudfare creds"})

            # get list of domain on zoho

        if request.method == 'POST':                    

            username = request.POST.get('username')
            name = request.POST.get('name')
            password = request.POST.get('password')
            select_domain_list = request.POST.get('select_domain_list')
            print(select_domain_list)

            select_domain_list = select_domain_list.split(',')
            print(select_domain_list) # selected domain from frontend

            # defingin celery task id dictionary 

            celery_task_id_dictionary = {'domain_name':[],'task_id':[]}

            # looping the automation for domains form front end 

            for domain_name in select_domain_list:

                # counting api calls 

                api_calls = user.api_calls
                api_calls = api_calls +1 
                user.api_calls = api_calls
                user.save()


                # making email based on domain names from front end 

                created_email = username +'@'+ domain_name

                # making celery task dictionary and running the task 

                print(domain_name)
                task_id = create_user_zoho.delay(access_token, created_email,name,password,refresh_token,client_id,client_secret,zoho_domain)

                celery_task_id_dictionary['domain_name'].append(created_email)
                celery_task_id_dictionary['task_id'].append(task_id.task_id)

                # saving domain name and task id in database 

                user.celery_task_id_create_user_zoho_list = json.dumps(celery_task_id_dictionary)
                user.save()

                import time
                check_loop = 0
                from celery import current_app

                result = AsyncResult(task_id.task_id, app=current_app)
                while result.status != 'STARTED':
                    time.sleep(1)
                    check_loop += 1
                    if check_loop == 20:
                        break   

        try:

            # fetching task status and task name from database 
            jsonDec = json.decoder.JSONDecoder()
            celery_task_id_list = jsonDec.decode(user.celery_task_id_create_user_zoho_list)
            print(celery_task_id_list)

            # storing active tasks 
            from celery import current_app
            active_task_domain_name = []

            # running a loop to check if tasks are active

            for domain_name, task_id in zip(celery_task_id_list['domain_name'], celery_task_id_list['task_id']):
                result = AsyncResult(task_id, app=current_app)
                print(result.status)
                if result.status == 'STARTED':
                    active_task_domain_name.append(domain_name)

                elif result.status == 'RECEIVED':
                    active_task_domain_name.append(domain_name)

                else:
                    pass

                print('----------')
                print(active_task_domain_name)

        except:
                active_task_domain_name = []

        return render(request, 'dashboard/create_bulk_users_in_zoho.html', context = {"domain_list": domain_list,"active_task_domain_name":active_task_domain_name})

    else:
        
        return redirect('sign-in')


# -------------

def create_bulk_users_in_zoho_smartlead(request):

    if request.user.is_authenticated:

        user = request.user
        # check if zoho is connected 
        if user.zoho_domain:
            zoho_oauth = True
        else:
            return render(request, 'dashboard/message.html',context={'heading':'Zoho Not Connected','message':'Please connect your cloudflare & Zoho At Profile'})
            
            # return HttpResponse('Please connect your cloudflare & Zoho At <a href="/profile">Profile Page</a>')
        
        # check if zoho is connected ends 

        # check if smartlead api is added 
        if user.smart_lead_api_key:
            print('key')
            print(user.smart_lead_api_key)
        else:
            return HttpResponse('Please Connect Your Smartlead Account At <a href="/profile">Profile Page</a>')
        # check if smartlead api is added
        if user.api_calls >=50:
            return HttpResponse('50/50 FREE CREDITS USED, Please Contact mail@rithikrajput.com to get more.')
        # check if acess allowed
        if user.access_allowed == False:
            return HttpResponse('ACCESS DENIED, Please Contact mail@rithikrajput.com To Get Access.')
        # check if access allowed
        
        user = request.user
        zoho_domain = user.zoho_domain
        refresh_token = user.refresh_token
        client_id = user.client_id
        client_secret = user.client_secret
        zoho_domain = user.zoho_domain

        # checking access token 
        access_token = user.access_token
        if verify_access_token(access_token,zoho_domain) == False:
                    
            # refresh access token for zoho
            access_token = get_access_token(refresh_token, client_id, client_secret, zoho_domain)

            user.access_token = access_token
            user.save()

            # get list of domain on zoho 

        try:

            smart_lead_api_key = user.smart_lead_api_key
            domain_list = get_domain_from_zoho(refresh_token,client_id,client_secret,zoho_domain)
    
        except:

            print('WRONG CLOUDFARE CREDS')
            return render(request, 'dashboard/create_bulk_users_in_zoho_smartlead.html', context={"error": "please see if you have added proper cloudfare creds"})

            # get list of domain on zoho

        if request.method == 'POST':

            username = request.POST.get('username')
            name = request.POST.get('name')
            password = request.POST.get('password')
            select_domain_list = request.POST.get('select_domain_list')
            print(select_domain_list)

            select_domain_list = select_domain_list.split(',')
            print(select_domain_list) # selected domain from frontend

                # defingin celery task id dictionary 

            celery_task_id_dictionary = {'domain_name':[],'task_id':[]}

                # looping the automation for domains form front end 

            for domain_name in select_domain_list:

                    # counting api calls 

                api_calls = user.api_calls
                api_calls = api_calls +1 
                user.api_calls = api_calls
                user.save()

                # making email based on domain names from front end 

                created_email = username +'@'+ domain_name

                # making celery task dictionary and running the task 

                print(domain_name)
                task_id = create_user_zoho_smartlead.delay(access_token,created_email,name,password,refresh_token,client_id,client_secret,zoho_domain,smart_lead_api_key)
                celery_task_id_dictionary['domain_name'].append(created_email)
                celery_task_id_dictionary['task_id'].append(task_id.task_id)
                # saving domain name and task id in database 
                user.celery_task_id_create_user_zoho_smartlead_list = json.dumps(celery_task_id_dictionary)
                user.save()

                import time
                check_loop = 0
                from celery import current_app
                result = AsyncResult(task_id.task_id, app=current_app)
                while result.status != 'STARTED':
                    time.sleep(1)
                    check_loop += 1
                    if check_loop == 20:
                        break
        try:

            # fetching task status and task name from database 
            jsonDec = json.decoder.JSONDecoder()
            celery_task_id_list = jsonDec.decode(user.celery_task_id_create_user_zoho_smartlead_list)
            print(celery_task_id_list)

            # storing active tasks 
            from celery import current_app
            active_task_domain_name = []

            # running a loop to check if tasks are active

            for domain_name, task_id in zip(celery_task_id_list['domain_name'], celery_task_id_list['task_id']):
                result = AsyncResult(task_id, app=current_app)
                print(result.status)
                if result.status == 'STARTED':
                    active_task_domain_name.append(domain_name)

                elif result.status == 'RECEIVED':
                    active_task_domain_name.append(domain_name)

                else:
                    pass

                print('----------')
                print(active_task_domain_name)

        except:
            active_task_domain_name = []
            
        
        return render(request, 'dashboard/create_bulk_users_in_zoho_smartlead.html', context = {"domain_list": domain_list,"active_task_domain_name":active_task_domain_name})

    else:
        
        return redirect('sign-in')


def auth(request):
    return render(request,'dashboard/auth.html')


import urllib
from urllib import parse


def zoho_auth(request, url):
    if request.user.is_authenticated:
        
        url = request.get_full_path()
        split =dict(parse.parse_qs(parse.urlsplit(url).query))
        code = split['code'][0]
        location = split['location'][0]
        print(location)
        
        if location == 'us':
            zoho_domain =  'zoho.com'

        elif location == 'in':
            zoho_domain = 'zoho.in'

        elif location == 'eu':
            zoho_domain = 'zoho.eu'

        elif location == 'au':
            zoho_domain = 'zoho.com.au'

        elif location == 'jp':
            zoho_domain = 'zoho.jp'

        user = request.user

        user.zoho_domain = zoho_domain
        user.save()
        
        refresh_token = get_clients_access_token(code,user,zoho_domain)
        user.refresh_token = refresh_token
        print('--')
        print('--')
        print('--')
        print('--')
        print(zoho_domain)
        print(zoho_domain)
        print(zoho_domain)
        print(zoho_domain)
        user.save()
        return redirect('/')

    return render(request,'dashboard/auth.html')
