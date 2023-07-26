import requests
import random
from django.conf import settings

def send_otp_to_phone(phone):
    try:
        otp = random.randint(100000, 999999)
        # url = f'http://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone}/{otp}'
        # response = requests.get(url)
        return otp
    except:
        None