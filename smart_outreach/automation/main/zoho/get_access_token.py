import requests
def get_access_token(refresh_token,client_id,client_secret,zoho_domain):
    print('ZOHO.get_access_token.STARTS')

    # Query Parameters 
    refresh_token = f'{refresh_token}'
    client_id = f'{client_id}'
    client_secret = f'{client_secret}'

    # Define API End Point 

    api_end_point = f'https://accounts.{zoho_domain}/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token'

    # Making a POST request
    response = requests.request("POST", api_end_point).json()
    try :
        print('ZOHO.get_access_token.ENDS')
        return response['access_token']

    except:
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print('error')
        print(response)

    print('ZOHO.get_access_token.ENDS')


# get_access_token('1000.acadeffc66d111debd8dd3440712b048.2d34357f8b557a15106d687c8b78c236','1000.ON97GNOU3L0JPWXL7MKWMERYWX6PGV','1db51eb9f7a0673b04117db75126e7ccb55c18938e')
