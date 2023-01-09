import random
import zoho.get_access_token as access_token
import zoho_user.create_user as create_user
import zoho_user.enable_imap_active_s as enable_imap_active_s
import sys
sys.path.insert(
    0, r'C:\Users\ayush\OneDrive\Desktop\Zoho Email Verification\main/')



# inputs from user 

org_id = 60018218815
email = f'test@dropdegree.com'
name = 'Ayush'
password = '#%*&%#@!^&'

# get acces token 

access_token = access_token.get_access_token()

# create new users 

zuid_accountid_list = create_user.create_user(access_token, org_id, email, name, password)

zu_id = zuid_accountid_list[0]
account_id = zuid_accountid_list[1]

# Enable IMAP & Active Sync 

enable_imap_active_s.enable_imap_active_s(access_token,org_id,zu_id,account_id)