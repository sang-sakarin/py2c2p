import hmac
import hashlib

from .api_environment import APIEnvironment
from .decorators import check_in_kwargs


class PaymentGatewayRedirect:

    def __init__(self, merchant_id, secret_key, result_url, api_root=APIEnvironment.SANDBOX):
        self.merchant_id = merchant_id
        self.secret_key = secret_key
        self.result_url = result_url
        self.version = "8.5"
        self.API_ROOT = api_root

    def _json_to_list(self, data):
        return [v for (k, v) in data.items()]

    def _hash_signature(self, signature):
        return hmac.new(self.secret_key.encode(), signature.encode(), hashlib.sha256).hexdigest()

    def _generate_signature(self, context):
        context = self._json_to_list(context)
        signature = ''.join(context)
        hash_signature = self._hash_signature(signature)

        return hash_signature

    @check_in_kwargs(["order_id", "payment_description", "amount"])
    def prepare_payment(self, order_id='', payment_description='', amount='', currency=''):
        context = {}
        context['version'] = self.version
        context['merchant_id'] = self.merchant_id
        context['payment_description'] = payment_description
        context['order_id'] = order_id
        context['currency'] = currency
        context['amount'] = amount
        context['result_url_1'] = self.result_url
        context['hash'] = self._generate_signature(context)
        context['action_url'] = self.API_ROOT

        return context
