import requests

def disable_domain_hosting(access_token, domain_name, org_id,zoho_domain):
    print('ZOHO.disable_domain_hosting.STARTS')

    import requests


    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    body_json = {
        "mode": "disableMailHosting"
    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "PUT", api_end_point, headers=headers, json=body_json).json()

    print('ZOHO.disable_domain_hosting.ENDS')


def delete_domain(domain_name, access_token, org_id,zoho_domain):
    print('ZOHO.delete_domain.STARTS')
    disable_domain_hosting(access_token, domain_name, org_id,zoho_domain)

    # Define API End Point

    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/domains/{domain_name}'

    # Define Body And Json Here

    # body_json = {'domainName': f'{domain_name}', }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "DELETE", api_end_point, headers=headers).json()
    print(response)

    print('ZOHO.delete_domain.ENDS')



