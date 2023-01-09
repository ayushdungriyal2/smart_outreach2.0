import requests

def create_user(access_token, org_id,email,name,password,zoho_domain):
    print('ZOHO.ZOHO_USER.create_user.STARTS')

    print(access_token)
    print(org_id)
    print(email)
    print(name)
    print(password)
    print(zoho_domain)



    # Define API End Point

    api_end_point = f'https://mail.{zoho_domain}/api/organization/{org_id}/accounts'

    # Define Body And Json Here

    body_json = {

        "role": "admin",
        "primaryEmailAddress": f"{email}",
        "timeZone": "Asia/Kolkata",
        "language": "En",
        "displayName": f"{name}",
        "password": f"{password}",
        "country": "in",
        # "groupMailList": ["newgroupmail@mybizemail.com", "newgroup@mybizemail.com"]

    }

    headers = {'Authorization': f'Zoho-oauthtoken {access_token}'}

    response = requests.request(
        "POST", api_end_point, headers=headers, json=body_json).json()

    print(response)

    try:
        zuid = response['data']['zuid']
        account_id = response['data']['accountId']
    except:
        error_code = response['data']['errorCode']
        return error_code

    print('ZOHO.ZOHO_USER.create_user.ENDS')
    return[zuid,account_id]