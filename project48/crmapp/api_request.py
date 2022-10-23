import requests
import pprint

url = 'http://127.0.0.1:8000/api/v01/leads/'
token_alex = '08525097e529243430cd508d01df6f2b9c21d85e'
headers ={'Authorization': f'Token {token_alex}'}

#responce = requests.get(url)

responce = requests.get(url, headers=headers)


pprint.pprint(responce.json())
