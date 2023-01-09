import requests


def get_dkim_key(domain_name, access_token, org_id,zoho_domain):
    print('ZOHO.get_dkim_key.STARTS')
    print(domain_name)
    print(access_token)
    print(org_id)
    print(zoho_domain)

    # Define API End Point
    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    # Define Body And Json Here

    body_json = {
        "mode": "addDkimDetail",
        "selector": "zoho",
        "isDefault": False
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "PUT", api_end_point, headers=headers, json=body_json).json()


    try :
        return response['data']['publicKey']

    except:
        print('ERROR:')
        print(response)

    print('ZOHO.get_dkim_key.ENDS')
