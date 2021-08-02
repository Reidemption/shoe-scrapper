# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
import csv

response = response.get("https://www.rithmschool.com/blog")
print(response.text)