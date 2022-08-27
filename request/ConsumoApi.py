import json

import requests


class ConsumoApi:
    url = 'http://127.0.0.1:8000/usuarios'
    response = requests.get(url=url)
    response = json.loads(response.content)
    print(response)
