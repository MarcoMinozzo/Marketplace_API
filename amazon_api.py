import requests
from datetime import datetime
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import boto3

# SP-API Authentication
AWS_ACCESS_KEY = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
AWS_REGION = 'us-east-1'
ACCESS_TOKEN = 'YOUR_LWA_ACCESS_TOKEN'

# Order Feedback
def fetch_order_feedback():
    endpoint = "https://sellingpartnerapi-na.amazon.com"
    path = "/orders/v0/orders"
    url = f"{endpoint}{path}"
    params = {
        'MarketplaceIds': 'ATVPDKIKX0DER',
        'CreatedAfter': '2023-01-01T00:00:00Z',
    }
    headers = {
        'x-amz-access-token': ACCESS_TOKEN,
        'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
        'Host': 'sellingpartnerapi-na.amazon.com'
    }
    request = AWSRequest(method="GET", url=url, params=params, headers=headers)
    SigV4Auth(boto3.Session().get_credentials(), "execute-api", AWS_REGION).add_auth(request)
    response = requests.get(url, headers=dict(request.headers), params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Buyer Messages
def fetch_buyer_messages():
    endpoint = "https://sellingpartnerapi-na.amazon.com"
    path = "/messaging/v1/messages"
    url = f"{endpoint}{path}"
    headers = {
        'x-amz-access-token': ACCESS_TOKEN,
        'x-amz-date': datetime.utcnow().strftime('%Y%m%dT%H%M%SZ'),
        'Host': 'sellingpartnerapi-na.amazon.com'
    }
    request = AWSRequest(method="GET", url=url, headers=headers)
    SigV4Auth(boto3.Session().get_credentials(), "execute-api", AWS_REGION).add_auth(request)
    response = requests.get(url, headers=dict(request.headers))
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

# Run functions
order_feedback = fetch_order_feedback()
buyer_messages = fetch_buyer_messages()
print(order_feedback)
print(buyer_messages)
