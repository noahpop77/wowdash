import json
import os
import requests
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

#Get the password
keys = config_object["KEYS"]
clientKey = keys["client"]
secretKey = keys["secret"]


def create_access_token(client_id, client_secret, region = 'us'):
    data = { 'grant_type': 'client_credentials' }
    response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
    return response.json()

accessToken = create_access_token(clientKey, secretKey)





URL = f"https://us.api.blizzard.com/data/wow/realm/index?namespace=dynamic-classic-us&locale=en_US&access_token={accessToken['access_token']}"

  
# sending get request and saving the response as response object
r = requests.get(url = URL)

# extracting data in json format
data = r.json()

#print(data)
for i in data['realms']:
    print(f"{i['name']} with ID {i['id']}")

