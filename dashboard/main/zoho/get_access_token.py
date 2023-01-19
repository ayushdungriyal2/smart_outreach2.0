import requests

def get_access_token(refresh_token,client_id,client_secret,zoho_domain):

    print('ZOHO.get_access_token.STARTS')

    refresh_token = f'{refresh_token}'
    client_id = f'{client_id}'
    client_secret = f'{client_secret}'

    api_end_point = f'https://accounts.{zoho_domain}/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token'

    response = requests.request("POST", api_end_point).json()

    try :
        access_token =  response['access_token']
        print('ZOHO.get_access_token.ENDS')
        return access_token

    except:
        print('error')
        print(response)
        print('ZOHO.get_access_token.ENDS')