import requests
from requests.structures import CaseInsensitiveDict
from decouple import config

API_KEY = config('secret_key')


def is_valid_email(email):
    url = f"https://api.emailvalidation.io/v1/info?email={email}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
         json_res = response.json()
         format_valid = json_res['format_valid']
         mx_found = json_res['mx_found']
         smtp_check = json_res['smtp_check']
         state = json_res['state']
         return format_valid and mx_found and smtp_check and state == 'deliverable'
    return False

