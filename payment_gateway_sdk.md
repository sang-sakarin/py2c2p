# Payment Gateway SDK - 2c2p

A Python library for [mobile SDK](https://developer.2c2p.com/docs/mobile-v4-how-it-work)

## Table of Contents

- [Instalation](#instalation)
- [Usage](#usage)
  - [Creating a object](#creating)
  - [Payment token](#paymenttoken)
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
  * ```api_root``` <b>string</b> api endpoint ```default``` <b>APIEnvironment.SANDBOX</b> [more option](#apienvironment)

### Payment token <a name="paymenttoken"></a>

#### Description:
  In order to use 2C2P PGW SDK making payment request, merchant is required to generate payment token

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
  If you want more detail per parameter. Please cick link [here](#https://developer.2c2p.com/docs/mobile-v4-api-parameters#section--payment-token-request-parameters-).

  * ```invoice_no``` <b>string</b> invoice number ```required```
  * ```desc``` <b>string</b> payment detail description ```required```
  * ```amount``` <b>number</b> transaction amount ```required```
  * ```currency_code``` <b>string</b> transaction currency code in 3 alphabet values as specified in ISO 4217. ```required```
  * ```payment_channel``` <b>string</b> payment channel ```required``` ```default``` <b>PaymentChannel.CREDIT_CARD</b> [more option](#paymentchannel)
  * ```user_defined1``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined2``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined3``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined4``` <b>string</b> for merchant to submit merchant's specific data
  * ```user_defined5``` <b>string</b> for merchant to submit merchant's specific data
  * ```interest_type``` <b>string</b> pay interest type [more option](#interesttype)
  * ```product_code``` <b>string</b> installment product code
  * ```recurring``` <b>string</b> recurring payment. to enable RPP (Recurring Payment Plan) transaction feature for credit card payment  ```default``` <b>Recurring.NO</b> [more option](#recurring)
  * ```invoice_prefix``` <b>string</b> invoice prefix
  * ```recurring_amount``` <b>number</b> the amount to be charged on RPP process
  * ```allow_accumulate``` <b>string</b> allow accumulation of failed authorization
  * ```max_accumulate_amt``` <b>int</b> limit for the accumulate amount before terminating
  * ```recurring_interval``` <b>int</b> recurring interval in days
  * ```recurring_count``` <b>int</b> recurring total count allowed
  * ```charge_next_date``` <b>string</b> the next date of recurring payment
  * ```promotion``` <b>string</b> promotion Code for the payment
  * ```request_3ds``` <b>string</b> 3D Secure option ```default``` <b>CardSecureMode.YES</b> [more option](#cardsecuremode)
  * ```tokenize_only``` <b>string</b> tokenization for Credit Card as card token without perform transaction
  * ```statement_descriptor``` <b>string</b> dynamic statement description

## References <a name="references"></a>


### API Environment <a name="apienvironment"></a>

#### List:

| Variables                  | API Environment                                     |
| -------------------------- |-----------------------------------------------------|
| SANDBOX                    | https://demo2.2c2p.com/2C2PFrontend/PaymentActionV2 |
| PRODUCTION                 | https://t.2c2p.com/paymentActionV2                  |
| zebra PRODUCTION_INDONESIA | https://payid.2c2p.com/paymentActionV2              |

#### How to use:

    from py2c2p.payment_gateway_sdk import APIEnvironment


    APIEnvironment.SANDBOX


### Payment Channel <a name="paymentchannel"></a>

#### List:

| Variables         | Description                                             |
| ----------------- |---------------------------------------------------------|
| ALL               | All available payment (Only use for Payment Token API)  |
| CREDIT_CARD       | Credit Card payment                                     |
| zebra INSTALLMENT | Installment payment                                     |

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