import requests
from bs4 import BeautifulSoup as soup
import random
import mysql.connector
import urllib.request
import json


def get_img(url, img_name):
    full_path ="Images/"+ img_name+'.jpg'
    urllib.request.urlretrieve(url, full_path)

def get_api(country="Poland"):
    url = f"https://api.unsplash.com/search/photos?query={country}&client_id=OKkkHGZeE_A6U9jpUoNg4yc40ePbw93OPc-EMYFCEtg"
    req = requests.get(url)
    sp = soup(req.content, 'lxml')
    return sp
    


def main():
    additional_countries = ['Kosovo']
    results = []
     
    request = requests.get("https://en.wikipedia.org/wiki/Europe")


    data = soup(request.content, "lxml")

    countries = data.select(".wikitable.sortable")[0]

     
    countries = countries.find("tbody").findAll("tr")
    indexes = ["title", "area", "population", "density", "capital", "language", "qwe", "qwe"]   #about




    for i in countries[1:-1]:
        element = {}
         
        temp = indexes.copy()
        content = i.findAll("td")[2:]
     
        for x in content:
            element[temp.pop(0)] = x.text[:-1]
     
        
     
        link = r"https://en.wikipedia.org"+content[0].a['href']
     
        
        req = requests.get(link)
        info = soup(req.content, 'lxml')
        tags = info.findAll("p")
        tags.sort(key=len, reverse=True)
        element['about'] = random.choice(tags[:10]).text
        country = (element['title'], element['population'], element['about'], element['area'], element['density'], element['capital'],
                   element['language'])
        results.append(country)
        
     

    for country_name in additional_countries:
        element = {}
        link = "https://en.wikipedia.org/wiki/"+country_name
        req = requests.get(link)
        info = soup(req.content, 'lxml')
        tags = info.findAll("p")
        tags.sort(key=len, reverse=True)
        try:
            print(element['title'])
        except:
            pass
        element['about'] = random.choice(tags[:10]).text
        element['title'] = country_name
        element['population'] = info.select_one("tr.mergedrow:nth-child(32) > td:nth-child(2)").text
        element['area']= info.select_one("tr.mergedrow:nth-child(29) > td:nth-child(2)").text
        element['density']=info.select_one("tr.mergedbottomrow:nth-child(33) > td:nth-child(2)").text
        element['capital']=info.select_one("table.infobox:nth-child(5) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2) > span:nth-child(1)").text
        element['language']=info.select_one("tr.mergedtoprow:nth-child(7) > td:nth-child(2) > div:nth-child(1) > ul:nth-child(1)").text
     
        country = (element['title'], element['population'], element['about'], element['area'], element['density'], element['capital'],
                   element['language'])
        results.append(country)
        
main()

'''    
ok = get_api()
par = json.loads(ok.text)
for res in par['results'][:4]:
    print(res['urls']['regular'])
'''


''' 
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="maps")
cur = mydb.cursor()
formula = "INSERT INTO countries(title, population, about, area, density, capital, language) VALUES (%s,%s,%s,%s,%s,%s,%s ) "
cur.executemany(formula, results)
mydb.commit()
'''
 
