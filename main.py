from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


base_url = "https://foursquare.com/v/dukes-grocery/522a9a0511d2b2f9a85cedb4"

requests.get(base_url)

#Send get http request
page = requests.get(base_url)
#print(type(page))

print(page.status_code)

#ensure successful webpage call
if page.status_code == requests.codes.ok:
  #get page in beautiful soup format
  bs = BeautifulSoup(page.text, 'lxml')

#find something you specify in the html
neighborhood = bs.select('span[class="venueNeighborhood"]')[0].text

print(neighborhood)