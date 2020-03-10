import mysql.connector 
import json
import requests
from bs4 import BeautifulSoup as soup
import urllib.request
import os
from pprint import pprint


import shutil
base_dir = os.getcwd()
enumeration = {1: 'Albania', 2: 'Andorra', 3: 'Armenia', 4: 'Austria', 5: 'Azerbaijan', 6: 'Belarus', 7: 'Belgium',
                8: 'Bosnia and Herzegovina', 9: 'Bulgaria', 10: 'Croatia', 11: 'Cyprus', 12: 'Czech Republic',
                13: 'Denmark', 14: 'Estonia', 15: 'Finland', 16: 'France', 17: 'Georgia', 18: 'Germany', 19: 'Greece',
                20: 'Hungary', 21: 'Iceland', 22: 'Ireland', 23: 'Italy', 24: 'Kazakhstan', 25: 'Latvia', 26: 'Liechtenstein',
                27: 'Lithuania', 28: 'Luxembourg', 29: 'Malta', 30: 'Moldova', 31: 'Monaco', 32: 'Montenegro', 33: 'Netherlands',
                34: 'North Macedonia', 35: 'Norway', 36: 'Poland', 37: 'Portugal', 38: 'Romania', 39: 'Russia', 40: 'San Marino',
                41: 'Serbia', 42: 'Slovakia', 43: 'Slovenia', 44: 'Spain', 45: 'Sweden', 46: 'Switzerland', 47: 'Turkey', 48: 'Ukraine',
                49: 'United Kingdom', 50: 'Vatican City', 51: 'Kosovo', 52: 'UID'}

def get_img(url, img_name):
    full_path =img_name+'.jpg'
    urllib.request.urlretrieve(url, full_path)
    
def get_api(country="Poland"):
    url = f"https://api.unsplash.com/search/photos?query={country}&client_id=OKkkHGZeE_A6U9jpUoNg4yc40ePbw93OPc-EMYFCEtg"
    req = requests.get(url)
    sp = soup(req.content, 'lxml')
    return sp
def main():
    ok = get_api()
    par = json.loads(ok.text)
    for res in par['results'][:4]:
        print(res['urls']['regular'])


'''
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="maps")
cur = mydb.cursor()
formula = "select * from countries"
cur.execute(formula)
data = cur.fetchall()
'''
def initial_state(prev_state=None):
    if prev_state=="images":
        print("RETURNING FROM IMAGES")
        f = open("log.txt", "w")
        log = f"Number of countries: {len(os.listdir(os.getcwd()))}"
        f.write( log )
    os.chdir(base_dir)

def save_images(country_name):
    ok = get_api(country_name)
    par = json.loads(ok.text)
    counter = 1
    for res in par['results'][:3]:
        get_img(res['urls']['regular'], country_name+str(counter) )
        counter+=1

def debugger():
    print("its ok ")
def venture(func, **kwargs):
    country = kwargs['country']
    os.chdir(country)
    func(country)
    os.chdir('..')
def load_images(enumeration = enumeration, overwrite=True):
    initial_state()
    _path, _dir = os.path.split(os.getcwd())
    files = os.listdir(os.getcwd())

    if "tuta" not in _dir:
        return

    if "images" not in os.listdir(os.getcwd()):
        os.mkdir("images")
    
    os.chdir("images")
 
 
    for country in list(enumeration.items()):
        if country[1] not in os.listdir(os.getcwd()):
            os.mkdir(country[1])
            pass
        else:
            shutil.rmtree(country[1], ignore_errors=True)
            os.mkdir(country[1])

        venture(save_images, country = country[1])

 
        
    return initial_state(os.path.split(os.getcwd())[1])
    

def scan_files():
    rest = {}
    for i in list(enumeration.items()):
        rest[i[1]]=  i[0]
    results= []
    if 'tuta' in  os.path.split(os.getcwd())[1]  and 'images' in os.listdir(os.getcwd()):
        print("its ok")
    os.chdir('images')
    for file in os.listdir(os.getcwd()):
        if '.' not in file:
            os.chdir(file)
            obj = {}
            obj['id']=  rest[os.path.split(os.getcwd())[1]]
            obj['country'] = os.path.split(os.getcwd())[1]
            obj['images'] = []
            for image in os.listdir(os.getcwd()):
                obj['images'].append(os.path.realpath(image) )
            results.append(obj)
            os.chdir("..")
    return results
            
load_images()        


#data = scan_files()
#load_images()
