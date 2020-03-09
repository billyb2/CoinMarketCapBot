def convert(cryptocurrency, amount):
  
    #This example uses Python 2.7 and the python-request library.

    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json

    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    parameters = {
    'symbol':cryptocurrency,
    'amount': amount,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '6871cd4a-229d-46dd-9407-b3e861085e0f',
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = response.text
    return json.loads(data)["data"]["quote"]["USD"]["price"]
