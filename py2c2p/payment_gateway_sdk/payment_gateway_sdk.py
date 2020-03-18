import base64
import json
import hmac
import hashlib
import requests
import uuid

from .api_environment import APIEnvironment
from .constants import ENDPOINTS


class PaymentGatewaySDK:

    def __init__(self, mid, secret_key):
        self.mid = mid
        self.secret_key = secret_key
        self.API_ROOT = APIEnvironment.SANDBOX

    def _get_path(self, path_name):
        """
        Get full endpoint for a specific path.
        """
        return self.API_ROOT + ENDPOINTS[path_name]

    def _json_to_list(self, data):
        return [v for (k, v) in data.items()]

    def _base64_to_json(self, data):
        raw_response = base64.b64decode(data)
        data = json.loads(raw_response)

        return data

    def _hash_signature(self, signature):
        return hmac.new(self.secret_key.encode(), signature.encode(), hashlib.sha256).hexdigest()

    def _generate_signature(self, context):
        context = self._json_to_list(context)
        context.sort(key=str.lower)
        signature = ''.join(context)
        hash_signature = self._hash_signature(signature)

        return hash_signature

    def _validate_signature(self, response):
        context = self._base64_to_json(response)
        original_signature = context['signature']
        context['signature'] = ""
        hashed_signature = self._generate_signature(context)

        return original_signature.lower() == hashed_signature.lower()

    def _request_api(self, url, data):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        payment_request = str(data)
        data = base64.b64encode(payment_request.encode())

        return requests.post(url, headers=headers, data=data)

    def payment_token(self, invoice_no='', desc='', amount='', currency_code='', payment_channel='', user_defined1='', user_defined2='', user_defined3='', user_defined4='', user_defined5='', interest_type='', product_code='', recurring='', invoice_prefix='', recurring_amount='', allow_accumulate='', max_accumulate_amt='', recurring_interval='', recurring_count='', charge_next_date='', promotion='', request_3ds='', tokenize_only='', statement_descriptor=''):
        context = {}
        context['version'] = "10.01"
        context['merchantID'] = self.mid
        context['invoiceNo'] = invoice_no
        context['desc'] = desc
        context['amount'] = amount
        context['currencyCode'] = currency_code
        context['paymentChannel'] = payment_channel
        context['userDefined1'] = user_defined1
        context['userDefined2'] = user_defined2
        context['userDefined3'] = user_defined3
        context['userDefined4'] = user_defined4
        context['userDefined5'] = user_defined5
        context['interestType'] = interest_type
        context['productCode'] = product_code
        context['recurring'] = recurring
        context['invoicePrefix'] = invoice_prefix
        context['recurringAmount'] = recurring_amount
        context['allowAccumulate'] = allow_accumulate
        context['maxAccumulateAmt'] = max_accumulate_amt
        context['recurringInterval'] = user_defined1
        context['recurringCount'] = user_defined2
        context['chargeNextDate'] = user_defined3
        context['promotion'] = user_defined4
        context['request3DS'] = user_defined5
        context['tokenizeOnly'] = interest_type
        context['statementDescriptor'] = user_defined1
        context['nonceStr'] = str(uuid.uuid4())

        hash_signature = self._generate_signature(context)
        context['signature'] = hash_signature

        url = self._get_path("PAYMENT_TOKEN_PATH")

        response = self._request_api(url, context)
        response = response.text

        return self._base64_to_json(response)
