# py2c2p

A Python library for [2c2p](https://developer.2c2p.com/docs) API

## Table of Contents

- [Instalation](#instalation)
- [Usage Mobile SDK](#usagemobilesdk)
  - [Creating a PGW Object](#creatingpgw)


## Installation <a name="installation"></a>

    pip install py2c2p

## Usage Mobile SDK <a name="usagemobilesdk"></a>
  A section for [mobile SDK](https://developer.2c2p.com/docs/mobile-v4-how-it-work) (server)

    from py2c2p import PaymentGatewaySDK

### Creating a PGW Object <a name="creatingpgw"></a>

    MID = 'YOUR MERCHANT ID'
    SECRET_KEY = 'YOUR SECRET KEY'

    # initial object
    pgw = PaymentGatewaySDK(MID, SECRET_KEY)
