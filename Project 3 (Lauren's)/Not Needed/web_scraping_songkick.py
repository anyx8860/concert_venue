import requests
from bs4 import BeautifulSoup
import json
import csv
#import pandas as pd

# Output File (CSV)
e_File = open('events.txt','w')
p_File = open('performance.txt','w')
a_File = open('artist.txt','w')

aids = [17879,65557,82547,85795,95022,115003,127006,139648,149066,181875,182968,186049,197928,209003,213449,217815,
234311,235779,273530,278737,297319,316828,365382,366307,378080,440797,451661,456767,462022,491256,519159,527224,
537914,551106,552177,553938,556955,568431,718506,807990,930524,941964,974908,976211,1055942,1059348,1134363,1168415,
1435335,1646455,2083334,2274326,2322629,2332047,2506696,2596951,2867816,3015056,3277856,3376301,3732956,4363463,
4774213,4971683,5200703,5318433,5352228,5427893,5642214,6012829,6393799,6715369,7561184,8008073,8067338,8310783,
8324968,8504398,8568579]


for i in aids:
try:
  id = str(i)
  url = "https://api.songkick.com/api/3.0/artists/" + id + "/calendar.json?apikey=WewWUhkws9IU4phb"
#print(url)##
  response = requests.get(url)
  data = json.loads(response.text)
  data_main = data['resultsPage']['results']
  events = data_main["event"]

  event_data = []
except KeyError:
 continue


for a in events:
   e_id = a['id']
   e_name = a['displayName']
   e_type = a['type']
   e_popularity = a['popularity']
   e_date = a['start']['date']
   event_data.append(e_id)
   event_data.append(e_name)
   event_data.append(e_type)
   event_data.append(e_popularity)
   event_data.append(e_date)


a=[]
k = 0
for i in event_data:
       if k<len(event_data):
       #a = str(event_data[k]) ,";", str(event_data[k+1]) ,";", str(event_data[k+2]) ,";", str(event_data[k+3]),";",
          a = str(event_data[k]) + ";" + str(event_data[k + 1])+ ";" + str(event_data[k + 2])+ ";" + str(event_data[k + 3])+ ";" + str(event_data[k + 4] + "\n")
          k=k+5
          e_File.write(a)



################################
#### Performance & Artist ##

data_performances = data['resultsPage']['results']['event']
# print(type(data_performances))
for p in data_performances:
    p_data = p['performance']

for a in p_data:
    a_data = a['artist']

performance_data = []
for p in p_data:
   p_id = p['id']
   p_name = p['displayName']
   performance_data.append(p_id)
   performance_data.append(p_name)

a=[]
k = 0
for i in performance_data:
    if k < len(performance_data):
       #print(performance_data[k])
       a = str(performance_data[k]) + ";" + str(performance_data[k + 1]) + "\n"
       k = k + 2
       #print(a)
       p_File.write(a)

artist_data = []
for a in a_data:
   a_id = a_data['id']
   a_name = a_data['displayName']
   artist_data.append(a_id)
   artist_data.append(a_name)

a=[]
k = 0
for i in artist_data:
    if k < len(artist_data):
       #print(performance_data[k])
       a = str(artist_data[k]) + ";" + str(artist_data[k + 1]) + "\n"
       k = k + 2
       #print(a)
       a_File.write(a)


#########LOCATION and Venue #############

## Locations ##
location_data = []
for l in events:
   loc = l['location']
   location_data.append(loc)

a = []
k = 0
for i in location_data:
    if k < len(location_data):
        # print(performance_data[k])
        a = str(location_data[k])
        k = k +

last line is k = k+1