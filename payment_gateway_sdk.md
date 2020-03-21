# Payment Gateway SDK - 2c2p

A Python library for [mobile SDK](https://developer.2c2p.com/docs/mobile-v4-how-it-work)

## Table of Contents

- [Instalation](#installation)
- [Usage](#usage)
  - [Creating a Object](#creating)
  - [Payment Token](#paymenttoken)
  - [Backend Payment Response](#backendpaymentresponse)
- [References](#references)
  - [API Environment](#apienvironment)
  - [Payment Channel](#paymentchannel)
  - [Interest Type](#interesttype)
  - [Recurring](#recurring)
  - [Card Secure Mode](#cardsecuremode)

## Installation <a name="installation"></a>

    pip install py2c2p

## Usage <a name="usage"></a>

    from py2c2p.payment_gateway_sdk import PaymentGatewaySDK

### Creating a PGW Object <a name="creating"></a>

    from py2c2p.payment_gateway_sdk import APIEnvironment


    MERCHANT_ID = 'YOUR MERCHANT ID'
    SECRET_KEY = 'YOUR SECRET KEY'

    # initial object
    pgw = PaymentGatewaySDK(MERCHANT_ID, SECRET_KEY, api_root=APIEnvironment.PRODUCTION)

#### Parameter:

  * ```MERCHANT_ID``` <b>string</b> get merchant id when opening account with 2c2p ```required```
  * ```SECRET_KEY``` <b>string</b> get secret key from 2c2p PGW dashboard ```required```
  * ```api_root``` <b>string</b> api endpoint ```default``` <b>APIEnvironment.SANDBOX</b> [more](#apienvironment)

### Payment Token <a name="paymenttoken"></a>

#### Description:
  In order to use 2C2P PGW SDK making payment request, merchant is required to generate payment token. [more](https://developer.2c2p.com/docs/mobile-v4-payment-token-api)

#### Function:

    pgw.payment_token(invoice_no="1584728267", decs="2 days 1 night hotel room", amount="000000001000", currency_code="THB")

#### Response:

    {
      'version': '10.01',
      'paymentToken': 'roZG9I1hk/GYjNt+BYPYbzXcA++LZnSaJJXrgH1bseIhtmrkhlY1dxsbK+k99skbn3HUK+JSkcHC+ibt4rRI+5tR8I7CoQfYrF0kpcrEdkI0QDtmAfrry7sa0n9gHnn5Wi+OFPAq/MsM1xUnw0gtKA==',
      'respCode': '000',
      'respDesc': 'Success',
      'signature': 'FEF4396D6DA9095910437E9B46F9E6197EADCF02888631074F1D148B27CE0465'
    }

#### Parameter:
  If you want more detail per parameter. Please click link [here](#https://developer.2c2p.com/docs/mobile-v4-api-parameters#section--payment-token-request-parameters-).

  * ```invoice_no``` <b>string</b> invoice number ```required```
  * ```desc``` <b>string</b> payment detail description ```required```
  * ```amount``` <b>number</b> transaction amount ```required```
  * ```currency_code``` <b>string</b> transaction currency code in 3 alphabet values as specified in ISO 4217. ```required```
  * ```payment_channel``` <b>string</b> payment channel ```required``` ```default``` <b>PaymentChannel.CREDIT_CARD</b> [more
  ](#paymentchannel)
  * ```user_defined1``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined2``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined3``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined4``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined5``` <b>string</b> for merchant to submit merchant's specific data
  * ```interest_type``` <b>string</b> pay interest type [more](#interesttype)
  * ```product_code``` <b>string</b> installment product code
  * ```recurring``` <b>string</b> recurring payment. to enable RPP (Recurring Payment Plan) transaction feature for credit card payment  ```default``` <b>Recurring.NO</b> [more](#recurring)
  * ```invoice_prefix``` <b>string</b> invoice prefix
  * ```recurring_amount``` <b>number</b> the amount to be charged on RPP process
  * ```allow_accumulate``` <b>string</b> allow accumulation of failed authorization
  * ```max_accumulate_amt``` <b>int</b> limit for the accumulate amount before terminating
  * ```recurring_interval``` <b>int</b> recurring interval in days
  * ```recurring_count``` <b>int</b> recurring total count allowed
  * ```charge_next_date``` <b>string</b> the next date of recurring payment
  * ```promotion``` <b>string</b> promotion Code for the payment
  * ```request_3ds``` <b>string</b> 3D Secure option ```default``` <b>CardSecureMode.YES</b> [more](#cardsecuremode)
  * ```tokenize_only``` <b>string</b> tokenization for Credit Card as card token without perform transaction
  * ```statement_descriptor``` <b>string</b> dynamic statement description


### Backend Payment Response <a name="backendpaymentresponse"></a>

#### Description:
In order to receive payment result from 2C2P PGW, merchant required register return URL under 2C2P Merchant Dashboard. [more](https://developer.2c2p.com/docs/mobile-v4-backend-payment-response)

#### Function:

    pgw.backend_payment_response(payment_response="eyJ2ZXJzaW9uIjoiMS4xIiwibWVyY2hhbnRJRCI6Ijc2NDc2NDAwMDAwMTI5...")

#### Response:

    {
      'version': '1.1',
      'merchantID': 'JT01',
      'pan': '411111XXXXXX1111',
      'userDefined1': '',
      'userDefined2': '',
      'userDefined3': '',
      'userDefined4': '',
      'userDefined5': '',
      'currencyCode': 'THB',
      'recurringUniqueID': '',
      'tranRef': '1516320',
      'approvalCode': '399562',
      'eci': '07',
      'channelCode': 'VI',
      'agentCode': 'KTC',
      'issuerCountry': 'US',
      'respCode': '000',
      'amount': '000000000100',
      'invoiceNo': '1584728267',
      'cardToken': '09071513062949492475',
      'referenceNo': '2059290',
      'transactionDateTime': '20190909175344',
      'signature': '1DEA03D8CA74B870C366BE00E03180B54AE773E63D683BA4E57578A89C03818F'
    }

#### Parameter:
  * ```payment_response``` <b>string</b> payment response from POST method ```required```


## References <a name="references"></a>


### API Environment <a name="apienvironment"></a>

#### List:

| Variables                  | API Environment                                     |
| -------------------------- |-----------------------------------------------------|
| SANDBOX                    | https://demo2.2c2p.com/2C2PFrontend/PaymentActionV2 |
| PRODUCTION                 | https://t.2c2p.com/paymentActionV2                  |
| PRODUCTION_INDONESIA       | https://payid.2c2p.com/paymentActionV2              |

#### How to use:

    from py2c2p.payment_gateway_sdk import APIEnvironment


    APIEnvironment.SANDBOX


### Payment Channel <a name="paymentchannel"></a>

#### List:

| Variables         | Description                                             |
| ----------------- |---------------------------------------------------------|
| ALL               | All available payment (Only use for Payment Token API)  |
| CREDIT_CARD       | Credit Card payment                                     |
| INSTALLMENT       | Installment payment                                     |

#### How to use:

    from py2c2p.payment_gateway_sdk import PaymentChannel


    PaymentChannel.ALL



### Interest Type <a name="interesttype"></a>

#### List:

| Variables         | Description            |
| ----------------- |------------------------|
| C                 | Customer Pay Interest  |
| M                 | Merchant Pay Interest  |

#### How to use:

    from py2c2p.payment_gateway_sdk import InterestType


    InterestType.C



### Recurring <a name="recurring"></a>

#### List:

| Variables         | Description            |
| ----------------- |------------------------|
| YES               | Enable recurring       |
| NO                | Disable recurring      |

#### How to use:

    from py2c2p.payment_gateway_sdk import Recurring


    Recurring.YES



### Card Secure Mode <a name="cardsecuremode"></a>

#### List:

| Variables         | Description                                     |
| ----------------- |-------------------------------------------------|
| FORCE             | Force 3DS (Only ECI 02 / 05 are accepted)       |
| YES               | Do 3DS                                          |
| NO                | Don’t do 3DS                                    |

#### How to use:

    from py2c2p.payment_gateway_sdk import CardSecureMode


    CardSecureMode.FORCE
