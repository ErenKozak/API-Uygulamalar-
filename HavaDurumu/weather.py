import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "0a72c9eafec440ffa6290717241408"

response = requests.get(url,params={
    "key":access_key,
    "q":"istanbul"
})

sonuc = response.json()

print(sonuc["location"]["region"])