import requests
import json
from pprint import pprint

tag = 'Python'
URL = f'https://api.stackexchange.com/2.3/questions?fromdate=1631232000&todate=1631318400&order=desc&sort=activity&tagged={tag}&site=stackoverflow'

res = requests.get(URL).json()
pprint(res)