import requests
from urllib.parse import urlencode
from core.config import settings

BASE_URL = "https://ob.sandbox.natwest.com"
TOKEN_URL = f"{BASE_URL}/token"
CONSENT_URL = f"{BASE_URL}/open-banking/v3.1/aisp/account-access-consents"
AUTHORIZE_URL = "https://api.sandbox.natwest.com/authorize"
CREDIT_SCORE_URL = f"{BASE_URL}/open-banking/v3.1/aisp/accounts/credit-score"
ACCOUNTS_URL = f"{BASE_URL}/open-banking/v3.1/aisp/accounts"

def get_access_token():
    payload = {
        'grant_type': 'client_credentials',
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'scope': 'accounts'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(TOKEN_URL, headers=headers, data=urlencode(payload))
    response.raise_for_status()
    return response.json()['access_token']

def create_account_access_consent(access_token):
    payload = {"Data": {"Permissions": ["ReadAccountsDetail", "ReadBalances", "ReadTransactionsCredits", "ReadTransactionsDebits", "ReadTransactionsDetail", "ReadAccountsBasic", "ReadCreditScore"]}, "Risk": {}}
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(CONSENT_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['Data']['ConsentId']

def authorize_consent(consent_id):
    params = {
        'client_id': settings.CLIENT_ID,
        'response_type': 'code id_token',
        'scope': 'openid accounts',
        'redirect_uri': settings.REDIRECT_URI,
        'state': 'ABC',
        'request': consent_id,
        'authorization_mode': 'AUTO_POSTMAN',
        'authorization_username': settings.AUTH_USERNAME
    }
    response = requests.get(AUTHORIZE_URL, params=params)
    response.raise_for_status()
    redirect_uri = response.json()['redirectUri']
    return redirect_uri.split('code=')[1].split('&')[0]

def exchange_code_for_tokens(auth_code):
    payload = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'redirect_uri': settings.REDIRECT_URI,
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(TOKEN_URL, headers=headers, data=urlencode(payload))
    response.raise_for_status()
    tokens = response.json()
    return tokens['access_token'], tokens['refresh_token'], tokens['id_token']

def get_credit_score(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(CREDIT_SCORE_URL, headers=headers)
    response.raise_for_status()
    return response.json()

def get_account_balances(access_token, account_id):
    url = f"{ACCOUNTS_URL}/{account_id}/balances"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_transactions(access_token, account_id):
    url = f"{ACCOUNTS_URL}/{account_id}/transactions"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
