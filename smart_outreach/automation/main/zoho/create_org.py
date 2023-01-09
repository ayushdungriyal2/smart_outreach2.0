import requests


def create_org(access_token):
    print('ZOHO.create_org.STARTS')

    # Define API End Point

    api_end_point = f'https://mail.zoho.in/api/organization'

    # Define Body And Json Here

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    body_json = {
        "username": "dkfd9j1221",
        "domainName": "dropdegree.com",
        "emailId": "clairestark@zoho.com",
        "firstName": "Claire",
        "lastName": "Stark"
    }

    response = requests.request(
        "GET", api_end_point, headers=headers, json=body_json).json()

    print(response)
    org_id = response['data']['zoid']

    print('ZOHO.create_org.ENDS')


# for debugging
create_org('1000.651062012391a555a5c3334d5d7298ce.c6e8ff12f46b9d9707b9ef24dbfb508f')
