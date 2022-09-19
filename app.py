import requests
from requests.adapters import HTTPAdapter, Retry


def make_request():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    url = 'https://reqres.in/api/users'
    response = session.get(url)

    parsed = response.json()

    print(parsed)

make_request()