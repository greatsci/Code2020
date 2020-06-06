from bs4 import BeautifulSoup
import csv
import requests
import time

url = 'https://www.ieltsusatest.org/IELTS?countryId=222&testCentreLocationId=1876'

print(requests.get(url))
