import requests
import json
api_key = "0d4f284fa32f0bd3d3f5fb85"
url = F" https://v6.exchangerate-api.com/v6/{api_key}/latest/"

bozulanDoviz = input("Bozulan döviz türü:") # USD
alinanDoviz = input("Alınan döviz türü:") # TRY
miktar = input(f"ne kadar {bozulanDoviz} bozdurmak istiyorsunuz: ") # ne kadar USD

sonuc = requests.get(url+bozulanDoviz)
sonuc_json = json.loads(sonuc.text)

# print(sonuc_json["conversion_rates"]["TRY"])
print(float(miktar)*sonuc_json["conversion_rates"][alinanDoviz],alinanDoviz)