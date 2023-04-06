import requests

url = "https://eec19846-geocoder-us-census-bureau-v1.p.rapidapi.com/locations/onelineaddress"

querystring = {"benchmark":"Public_AR_Current","address":"1 Embarcadero street San Francisco","format":"json"}

headers = {
	"X-RapidAPI-Key": "e7c682c5f5mshd258584e0f9d222p190626jsnc7e39b81cf56",
	"X-RapidAPI-Host": "eec19846-geocoder-us-census-bureau-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())