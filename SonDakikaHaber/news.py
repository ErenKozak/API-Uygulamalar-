
#! ilk yöntem
# import requests

# url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=8b26e15cb0514251beae6dd8cacf0b3e"

# response = requests.get(url)
# haberler = response.json()["articles"]

# for i in haberler:
#     print(i["title"])
    
#! ikinci yöntem
# import requests

# headLineUrl = "https://newsapi.org/v2/top-headlines"
# api_key="8b26e15cb0514251beae6dd8cacf0b3e"

# response = requests.get(headLineUrl,params={
#     "apiKey": api_key,
#     "country": "tr"  
# })
# haberler = response.json()["articles"]

# for i in haberler:
#     print(i["title"])
    
import requests # request modülünün import edilmesi

everyThingUrl = "https://newsapi.org/v2/everything" # url 
api_key="8b26e15cb0514251beae6dd8cacf0b3e" # api key

response = requests.get(everyThingUrl,params={
    "apiKey": api_key,
    "q":"futbol"  
}) # get ile servisten apinin alınması
haberler = response.json()["articles"] # json tipinde döndürülmesi

for i in haberler:
    print(i["title"]) # haberlerin başlıklarının yazdırılması
    
    