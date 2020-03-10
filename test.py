import mysql.connector
 
titlesZero = {0: 'Norway', 1: 'Finland', 2: 'Russia', 3: 'Sweden', 4: 'Iceland', 5: 'Estonia', 6: 'United Kingdom', 7: 'Latvia', 8: 'Denmark',
                9: 'Lithuania', 10: 'Denmark', 11: 'Belarus', 12: 'Ireland', 13: 'United Kingdom', 14: 'Russia', 15: 'Germany', 16: 'Poland',
                17: 'Netherlands', 18: 'Ukraine', 19: 'Belgium', 20: 'France', 21: '', 22: 'Czech Republic', 23: 'UID', 24: 'Slovakia', 25: 'Austria',
                26: 'Hungary', 27: 'Moldova', 28: 'Romania', 29: 'Switzerland', 30: 'Italy', 31: 'Slovenia', 32: 'Croatia', 33: 'Serbia',
                34: 'Bosnia and Herzegovina', 35: 'Bulgaria', 36: 'Spain', 37: 'Montenegro', 38: 'Cosovo', 39: 'Italy', 40: 'Albania', 41: 'North Macedonia',
                42: 'Portugal', 43: 'Greece', 44: 'Italy', 45: 'Italy'}

titles = {1: 'Norway', 2: 'Finland', 3: 'Russia', 4: 'Sweden', 5: 'Iceland', 6: 'Estonia', 7: 'United Kingdom', 8: 'Latvia',
           9: 'Denmark', 10: 'Lithuania', 11: 'Denmark', 12: 'Belarus', 13: 'Ireland', 14: 'United Kingdom', 15: 'Russia', 16: 'Germany',
           17: 'Poland', 18: 'Netherlands', 19: 'Ukraine', 20: 'Belgium', 21: 'France', 22: 'UID', 23: 'Czech Republic', 24: 'UID', 25: 'Slovakia',
           26: 'Austria', 27: 'Hungary', 28: 'Moldova', 29: 'Romania', 30: 'Switzerland', 31: 'Italy', 32: 'Slovenia', 33: 'Croatia', 34: 'Serbia',
           35: 'Bosnia and Herzegovina', 36: 'Bulgaria', 37: 'Spain', 38: 'Montenegro', 39: 'Kosovo', 40: 'Italy', 41: 'Albania', 42: 'North Macedonia',
           43: 'Portugal', 44: 'Greece', 45: 'Italy', 46: 'Italy'}


enumerationZero = {0: 'Albania', 1: 'Andorra', 2: 'Armenia', 3: 'Austria', 4: 'Azerbaijan', 5: 'Belarus', 6: 'Belgium',
               7: 'Bosnia and Herzegovina', 8: 'Bulgaria', 9: 'Croatia', 10: 'Cyprus', 11: 'Czech Republic', 12: 'Denmark',
               13: 'Estonia', 14: 'Finland', 15: 'France', 16: 'Georgia', 17: 'Germany', 18: 'Greece', 19: 'Hungary',
               20: 'Iceland', 21: 'Ireland', 22: 'Italy', 23: 'Kazakhstan', 24: 'Latvia', 25: 'Liechtenstein', 26: 'Lithuania',
               27: 'Luxembourg', 28: 'Malta', 29: 'Moldova', 30: 'Monaco', 31: 'Montenegro', 32: 'Netherlands',
               33: 'North Macedonia', 34: 'Norway', 35: 'Poland', 36: 'Portugal', 37: 'Romania', 38: 'Russia',
               39: 'San Marino', 40: 'Serbia', 41: 'Slovakia', 42:'Slovenia', 43: 'Spain', 44: 'Sweden', 45: 'Switzerland',
               46: 'Turkey', 47: 'Ukraine', 48: 'United Kingdom', 49: 'Vatican City', 50 : 'Kosovo', 51:'UID'}

enumeration = {1: 'Albania', 2: 'Andorra', 3: 'Armenia', 4: 'Austria', 5: 'Azerbaijan', 6: 'Belarus', 7: 'Belgium',
                8: 'Bosnia and Herzegovina', 9: 'Bulgaria', 10: 'Croatia', 11: 'Cyprus', 12: 'Czech Republic',
                13: 'Denmark', 14: 'Estonia', 15: 'Finland', 16: 'France', 17: 'Georgia', 18: 'Germany', 19: 'Greece',
                20: 'Hungary', 21: 'Iceland', 22: 'Ireland', 23: 'Italy', 24: 'Kazakhstan', 25: 'Latvia', 26: 'Liechtenstein',
                27: 'Lithuania', 28: 'Luxembourg', 29: 'Malta', 30: 'Moldova', 31: 'Monaco', 32: 'Montenegro', 33: 'Netherlands',
                34: 'North Macedonia', 35: 'Norway', 36: 'Poland', 37: 'Portugal', 38: 'Romania', 39: 'Russia', 40: 'San Marino',
                41: 'Serbia', 42: 'Slovakia', 43: 'Slovenia', 44: 'Spain', 45: 'Sweden', 46: 'Switzerland', 47: 'Turkey', 48: 'Ukraine',
                49: 'United Kingdom', 50: 'Vatican City', 51: 'Kosovo', 52: 'UID'}

def advertio(dictio):
    newDictio = {}
    last_element = len(list(dictio.items()))
    for key, val in dictio.items():
        newDictio[key+1] = val
    return newDictio



def revertio(dictio):
    newDictio={}
    for key,val in dictio.items():
        newDictio[key-1]=val
    return newDictio



def convert(dictio):
    newDictio = {}
    for key, val in dictio.items():
        newDictio[val] = key
    return newDictio

def get_elements(start, enumeration):
    elements = []
    enumeration = convert(enumeration)
    for index, i in enumerate(list(start.items())):
        country = i[1]
        print(str(index) + " " + country, enumeration[country], sep=" ")
        elements.append( (  int(enumeration[country]),   ))
    return elements 
    
element_results = get_elements(titles, enumeration)
element_results.pop(0)
element_results.pop(0)

mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="maps")
cur = mydb.cursor()
formula = "INSERT INTO elements( country_id) VALUES (%s)"
cur.executemany(formula, element_results)
mydb.commit()

"""  
 
f = open("EuropeComponent.tsx", "r")

lines = f.readlines()
f.close()

f = open("FinalResult.tsx", "w")

dataId=1

for counter, i in enumerate(lines):
    if "<path" in i and not "data-id" in i:
        #print(str(counter) + i)
        result = i[0:5] + " data-id= {" +  str(dataId)+ "} " + " data-title={'"+titles[dataId]+"'} "+'''
        fill={`${mallActive ==='''+ f'"{str(dataId)}_{str(dataId)}" ? colors.HOVERED : ""' +" }`} "  +'''
        onMouseOver={handleHover} style={{transition:"1s"}}'''+i[5:]
        dataId+=1
        print(result)
        f.write(result)
    else:
        f.write(i)




f.close()
mystr = "{"

for i in range(0,50):
    mystr += f"{i+1}:'', "


mystr +="}"
 
"""

 
