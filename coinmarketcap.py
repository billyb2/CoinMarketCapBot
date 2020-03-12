def convert(cryptocurrency, amount):
    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    from credentials import api_key
    import json

    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'
    parameters = {
    'symbol':cryptocurrency,
    'amount': amount,
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = response.text
    return json.loads(data)["data"]["quote"]["USD"]["price"]
