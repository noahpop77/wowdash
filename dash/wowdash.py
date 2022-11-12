import json
import os
from unicodedata import name
import requests
from configparser import ConfigParser


def getrealms():
    # Read config.ini file
    config_object = ConfigParser()
    config_object.read("wowdash/dash/config.ini")
    print(os.getcwd())
    # Get the password
    keys = config_object["apikeys"]
    clientKey = keys['client']
    secretKey = keys['secret']

    def create_access_token(client_id, client_secret, region = 'us'):
        data = { 'grant_type': 'client_credentials' }
        response = requests.post('https://%s.battle.net/oauth/token' % region, data=data, auth=(client_id, client_secret))
        return response.json()

    accessToken = create_access_token(clientKey, secretKey)
    print(accessToken)

    URL = f"https://us.api.blizzard.com/data/wow/realm/index?namespace=dynamic-classic-us&locale=en_US&access_token={accessToken['access_token']}"


    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()
    realms = []
    population = ""
    ids = []
    for i in data['realms']:
        ids.append(i['id'])

    for i in ids:
        print(i)
        try:
            populationURL = f"https://us.api.blizzard.com/data/wow/connected-realm/{i}?namespace=dynamic-classic-us&locale=en_US&access_token={accessToken['access_token']}"

            r = requests.get(url = populationURL)

            population = r.json()

            realms.append([{
                'name' : population['realms'][0]['name'],
                'id' : population['id'],
                'population' : population['population']['type'],
                'has_queue' : population['has_queue']
            }])
        except KeyError:
            print('fail')
            continue
    print(realms)
    return realms

