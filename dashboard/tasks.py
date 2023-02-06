import requests
from celery import Celery
from celery import shared_task
from .main import main
from .main import get_domains_zoho


def verify_access_token(access_token,zoho_domain):

    print('verify acces token starts')
    
    api_end_point = f'https://mail.{zoho_domain}/api/organization'
    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}
    response = requests.request(
        "GET", api_end_point, headers=headers).json()

    try:
        if response['data']['errorCode'] == 'INVALID_OAUTHTOKEN':
            print('validated access token - invalid')
            return False
        else:
            return True


    except:
        print('validated access token - valid')        
        return True






def get_domain_from_cloudfare(cloudfare_email, cloudfare_auth_code):
    api_end_point = f"https://api.cloudflare.com/client/v4/zones"

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Email": f"{cloudfare_email}",
        "Authorization": f"Bearer {cloudfare_auth_code}"
    }

    params = {
        "per_page":300,
    }

    response = requests.request("GET", api_end_point,params=params, headers=headers).json()

    domain_list = []

    for data in response['result']:
        domain_name = data['name']
        domain_list.append(domain_name)

    return domain_list


# ----------

def get_domain_from_zoho(access_token,client_id,client_secret,zoho_domain):

    response = get_domains_zoho.get_domains_zoho(access_token,client_id,client_secret,zoho_domain)

    domain_list = []
    for data in response['domain_name']:
            domain_list.append(data)

    return domain_list

@shared_task()
def add_domain_to_zoho_request(access_token, domain_name, mail_1, mail_2, zoho_domain, cloudfare_email, cloudfare_auth_code):
    # try:
    main.zoho_cloudfare_dns_automation(access_token, domain_name, mail_1, mail_2, zoho_domain, cloudfare_email, cloudfare_auth_code)
    # except:
        # pass
    return True

# --------

@shared_task
def create_user_zoho(access_token, email,name,password,refresh_token,client_id,client_secret,zoho_domain):

    try:
        main.zoho_create_users(access_token, refresh_token, client_id, client_secret, email, name, password, zoho_domain)
    except:
        pass
    return True


# ------------

@shared_task
def create_user_zoho_smartlead(access_token, email,name,password,refresh_token,client_id,client_secret,zoho_domain,smart_lead_api_key):

    try:

        main.zoho_create_users(access_token, refresh_token, client_id, client_secret, email, name, password, zoho_domain)

        # smart lead api call


        api_end_point = f"https://server.smartlead.ai/api/v1/email-accounts/save?api_key={smart_lead_api_key}"

        body_json = {

            "from_name": f"{name}",
            "from_email": f"{email}",
            "user_name": f"{email}",
            "password": f"{password}",
            "smtp_host": f"smtp.{zoho_domain}",
            "smtp_port": 465,
            "imap_host": f"imap.{zoho_domain}",
            "imap_port": 993,
            "max_email_per_day": 50,
            "custom_tracking_url": "",
            "bcc": "",
            "signature": "",
            "warmup_enabled": True,
            "total_warmup_per_day": 50, 
            "daily_rampup": 5, 
            "reply_rate_percentage": 30, 
        
        }

        try:
            response = requests.request("POST", api_end_point, json=body_json).json()
            print(response)
            
        except:
            print(response)
            pass
    except:
        pass

    return True



def get_clients_access_token(code,user,zoho_domain):
    
    api_end_point = f'https://accounts.{zoho_domain}/oauth/v2/token?code={code}&grant_type=authorization_code&client_id=1000.Z80WKB696P26IQF9OJ8N02WR37N0VY&client_secret=99191de808405a2f9bea51e79525fc0e1a3c7e73b9&redirect_uri=https://beta.smartoutreach.net/zoho_auth/&scope=ZohoMail.partner.organization.CREATE,ZohoMail.partner.organization.READ,ZohoMail.partner.organization.UPDATE,ZohoMail.partner.organization.DELETE,ZohoMail.organization.accounts.CREATE,ZohoMail.organization.accounts.READ,ZohoMail.organization.accounts.UPDATE,ZohoMail.organization.accounts.DELETE,ZohoMail.organization.domains.CREATE,ZohoMail.organization.domains.READ,ZohoMail.organization.domains.UPDATE,ZohoMail.organization.domains.DELETE'
    

    response = requests.request("POST", api_end_point).json()
    print(response)
    print(response)
    print(response)
    print(response)
    
    return response['refresh_token']