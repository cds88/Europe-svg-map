import os
import requests
import bs4
import time


def ls():
    return os.listdir(os.getcwd())

enumeration = {1: 'Albania', 2: 'Andorra', 3: 'Armenia', 4: 'Austria', 5: 'Azerbaijan', 6: 'Belarus', 7: 'Belgium',
                8: 'Bosnia and Herzegovina', 9: 'Bulgaria', 10: 'Croatia', 11: 'Cyprus', 12: 'Czech Republic',
                13: 'Denmark', 14: 'Estonia', 15: 'Finland', 16: 'France', 17: 'Georgia', 18: 'Germany', 19: 'Greece',
                20: 'Hungary', 21: 'Iceland', 22: 'Ireland', 23: 'Italy', 24: 'Kazakhstan', 25: 'Latvia', 26: 'Liechtenstein',
                27: 'Lithuania', 28: 'Luxembourg', 29: 'Malta', 30: 'Moldova', 31: 'Monaco', 32: 'Montenegro', 33: 'Netherlands',
                34: 'North Macedonia', 35: 'Norway', 36: 'Poland', 37: 'Portugal', 38: 'Romania', 39: 'Russia', 40: 'San Marino',
                41: 'Serbia', 42: 'Slovakia', 43: 'Slovenia', 44: 'Spain', 45: 'Sweden', 46: 'Switzerland', 47: 'Turkey', 48: 'Ukraine',
                49: 'United Kingdom', 50: 'Vatican City', 51: 'Kosovo', 52: 'UID'}



reversedDict = {}

for i in list(enumeration.items()):
    reversedDict[i[1]] = i[0]


BASE_DIR = os.getcwd()  



os.chdir('images')
for country in ls():
    os.chdir(country)
    for image in ls():
        print(os.path.realpath(image), country, reversedDict[country], sep="  ")
        with open(os.path.realpath(image), "rb") as f:
            binary_data = f.read()
        data = {}
        data['country_id'] = reversedDict[country]
        data['country_name'] = country
        resp =  requests.post("http://127.0.0.1:8000/api/image", files = {   'image': (  image , binary_data)}, data = data)
        time.sleep(1)
    os.chdir('..')

    












