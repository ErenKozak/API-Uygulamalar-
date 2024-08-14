
#!get
# veri talebi için kullanılır
# query string kullanılır
# server'a etkisi yoktur

#!post
# veri göndermek için kullanılır
# bilgi body ile gönderilir
# server'a etkisi vardır

import requests
import json
#! get kullanımı
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# sonuc = response
# sonuc = response.status_code
# sonuc = response.headers
# sonuc = response.headers["Content-Type"]
# sonuc = response.url
# sonuc = response.encoding
# sonuc = response.text
# sonuc = response.text
# todos = json.loads(response.text)
# sonuc = todos[0]["title"]

# for item in todos:
    # print(item)
    
# print(sonuc)
# print(type(response))

#! query string ile filtreleme
#? "?" sonrası olanlar filtreler ve birden fazla filtre "&" ile ayrılırlar"
#*birinci yontem
#response = requests.get("https://jsonplaceholder.typicode.com/todos?completed=true&userId=2")
#*ikinci yontem
# response = requests.get("https://jsonplaceholder.typicode.com/todos",params={
#     "userId":1,
#     "completed":"true"
# })

# print(response.text)
# list = response.json() #alınan response'u direkt json türüne çevirir
# print(list[0]["title"])
 
#! post kullanımı

response = requests.post("https://jsonplaceholder.typicode.com/posts",data=
    {
        "title":'deneme',
        "body":'deneme',
        "userId":1
    }
)

sonuc = response
sonuc = response.text
sonuc = response.json()
print(sonuc)