# On importe la fonction 'get' (téléchargement) de 'requests' 
# Et la classe 'Selector' (Parsing) de 'scrapy'
from requests import get
from scrapy import Selector
import numpy as np
import requests

headers = {
    'authority': 'collecte.io',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://collecte.io',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://collecte.io/la-nuit-du-styx-14-octobre-2021-845208/fr?fbclid=IwAR3m3p6h6MkMZZMISlcTtGOIROTYOjlfR4xuMMhPTnU19cjXKJF8jV9vn34',
    'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ga=GA1.2.1456033153.1631446326; _gid=GA1.2.1086895127.1631446326; amplitude_idundefinedcollecte.io=eyJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOm51bGwsImxhc3RFdmVudFRpbWUiOm51bGwsImV2ZW50SWQiOjAsImlkZW50aWZ5SWQiOjAsInNlcXVlbmNlTnVtYmVyIjowfQ==; __vero_visit=true; __veroc4=%5B%5D; amplitude_id_6ea3b2837a247b7d3064238484e628eecollecte.io=eyJkZXZpY2VJZCI6IjljZDc5MDFmLWQwYmQtNDVlMy05Y2UxLTU0ZGI3NTNmYzMzMVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYzMTQ0NjMyNjYwMSwibGFzdEV2ZW50VGltZSI6MTYzMTQ0ODA5MzMxNCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; fuelmid=EQA8jA9FWYzuAkI6kBFoj0UiBPyMrffNsCDZywTrOxZS5XzPLpt1vEL9WA71AiqpobINgFqzJjm-lRnUowZPs2I4wkVjJjoi6kMYOQkJX4vyTOIzuuWHmfiGpKXkkky9xMR1eh3FZb03jzyMoepsayRNI6o2qlHoh9w-aKfuIOrLjYpuHV3UfeZV194u6WEFVTEiBd_j99JQa4kmA-b_dR21CYe0uAxq1Dntt3kF4naDTgC53ZXTBdX3ylhrkdb9DJkvIr1-xklBanb0_RGbm4X2POymb87ssFLBN3OCl6BLBkwwVeBo3YFoKfUHz-zuTVsJtIxjRI6GCcZVXIxqhYJnikYkbb8n2buMZDxD_KjqxtrwK81knj0PP_zXdbQkx_TcJkIBIC0OVKgtoIMs014f16zU9EbEFjtJFcu2rfH8ExE9S7Z5bGEhxw-nIUzUaK0hLcNvIMzYsGna7ltBHdZ1n7Dee2TJX3nM6ImaD1zKUpPNUkTGLeNMKUr_CkMypb0HZ1cN7jT8APdzLjmvplJuNUhCM1lJaFJTcXNSYWFqVHktVkFNdHBRd1JkLXhMMm1yVGhEaWt5ODQ',
}

params = (
    ('fbclid', 'IwAR3m3p6h6MkMZZMISlcTtGOIROTYOjlfR4xuMMhPTnU19cjXKJF8jV9vn34'),
)

data = {
  'slug': 'la-nuit-du-styx-14-octobre-2021-845208',
  'customdata[val1]': '',
  'customdata[val2]': '',
  'customdata[val6]': '',
  'customdata[val3]': '',
  'customdata[val4]': '',
  'customdata[val5]': '',
  'customdata[val7]': 'Agro Grignon (21h30)',
  'customdata[val8]': '',
  'customdata[val9]': '',
  'price': '0'
}

res = requests.post('https://collecte.io/checkprice', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.post('https://collecte.io/checkprice?fbclid=IwAR3m3p6h6MkMZZMISlcTtGOIROTYOjlfR4xuMMhPTnU19cjXKJF8jV9vn34', headers=headers, data=data)
# Lien de la page à scraper
url = "https://collecte.io/la-nuit-du-styx-14-octobre-2021-845208/fr?fbclid=IwAR3m3p6h6MkMZZMISlcTtGOIROTYOjlfR4xuMMhPTnU19cjXKJF8jV9vn34"
response = get(url)
source = None # Le code source de la page 
if response.status_code == 200 :
    # Si la requete s'est bien passee
    source = response.text

if source :
    # Si le code source existe
    selector = Selector(text=source)
    IDs = selector.xpath("/html/body/div[3]/div[2]/div[2]/div/form/div[7]/select/option")
    A=[]
    for index,ID in enumerate(IDs):
        id=ID.xpath('@id').get()
        nom=ID.css('::text').get()
        A.append({'id':id,'nom':nom})

    deleteIDS=res.json()["disabled_ids"]
    for a in A[1:] :
        if a['id'] in deleteIDS:
            print(a['nom']+' n est pas disponible')
        else:
            print(a['nom']+' est disponible')




    
   



