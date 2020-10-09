import requests
from requests_html import HTMLSession

url = 'https://www.billboard.com/charts/hot-100/2020-10-03'

try:
    session = HTMLSession()
    response = session.get(url)

except requests.exceptions.RequestException as e:
    print(e)

print(response.html)