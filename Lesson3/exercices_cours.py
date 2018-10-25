
import requests
from bs4 import BeautifulSoup
import pandas as pd

Villes = []
Points = []
Trash = []
dist = []
Distance = []
Result = []

Villes50 = 'http://www.linternaute.com/ville/classement/villes/population' #50 plus grandes villes de 2015
req = requests.get(Villes50)
soup = BeautifulSoup(req.text, "lxml")

for sub_head in soup.find_all('a'):
    Villes.append(sub_head.text) 

Villes = Villes[179:179+50]

for i in range(0,50):
   Trash.append(Villes[i].split()) 
   Points.append(Trash[i][0])
   
for i in range (0, len(Points)):
    for j in range (0, len(Points)):
        a = Points[i]
        b = Points[j]
        Url = f'https://fr.distance.to/{a}/{b}' #50 plus grandes villes de 2015
        requ = requests.get(Url)
        soupe = BeautifulSoup(requ.text, "lxml")
        
        for b in soupe.find_all('span'):
            dist.append(b.text)
         
print(str(a)+' '+str(b)+' '+dist[27])