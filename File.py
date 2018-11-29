import os

# def addAge(age):
#     new_age = age + 50
#     return new_age

# def askagain(a):
#     print(addAge(a))

# cin = True
# while cin:
#     ask =int(input('What will your age + 50 be?'))
#     if ask < 150:
#         askagain(ask)
#         print('Done')

#     elif ask >150:
#         print('That is not real, type an age less than 150')


# ppl = ['her', 'him', 'bod', 'cat', 'slim', 'emo', 'eki']

# kod = str(input('What is you name'))

# for item in ppl:
#     if kod in item:
#         print(item)
#     else:
#         print('Out')


# def calc_currency(rate, currency):
#     dollar = currency * rate
#     return dollar

# rr = input('What is the current rate?')
# cc = input('What is your amount')

# amount = calc_currency(float(rr), float(cc)) + int(cc)

# print(amount)

# password = ' '

'''
while password != 'Pyhto':
    password = input('Whats password')
    if password == 'Pyhto':
        print('Welcome')
    else:
        print('GTFOH')
'''

'''
password = ' '

while password != 'Pyhto':
     password = input('Whats password')
     if password == 'Pyhto':
         continue

print(password)

'''
'''
nes = ['polr','kev','james','bio']

last =['hen','polo','ak']

for i,j in zip(nes, last):
    print(i,j)
if len(nes) > len(last):
        print(nes[-1])
'''


#Create a file
'''
filename = "sample.txt"

def create_file():
    with open(filename,"w") as file:
        file.write("Welcome to Python")

#call function to create file when executed
create_file()
'''



#Create a file and naming it date & time
'''
import datetime

filename = datetime.datetime.now()

def create_file():
    #check http://strftime.org/ for more info.
    with open(filename.strftime("%Y-%m-%d")+".txt","w") as file:
        file.write("logged on at " + filename.strftime("%Y-%m-%d"))

#call function to create file when executed
create_file()
'''
'''
import time
import datetime

iso = []
for i in range(10):
    iso.append(datetime.datetime.now())
    #time.sleep(3)

def callss():
    for i in iso:
        time.sleep(3)
        print(i)

callss()
'''
######################################################
"""import difflib
this is a library used to to compare 2 words
from difflib import get_close_matches :
this is helps match 2 letters;
eg:  get_close_matches("rain", ["pain","rainn","ain"])
>>>['rainn', 'ain', 'pain'] #it also arranges it by best matched"""
#####################################################
'''
import json
import difflib
from difflib import get_close_matches

info = json.load(open("data.json", 'r'))


conp = True

while conp:
        ask = input("Please Enter a word-:").lower()

        def translate(word):
                if word in info:
                        return info[word]
                elif  len(get_close_matches(word, info.keys())) > 0:
                        wed = input("Did you mean %s instead? Press Y to accept & N to Decline?" %get_close_matches(word, info.keys())[0])

                        if wed.lower() == "y":
                                return info[get_close_matches(word, info.keys())[0]]

                        elif wed.lower() =="n":
                                wod = input("'"+word+"'"+ " doesnt exist. Press 'a' to search for another word-:")
                                return wod

                        elif wed.lower() =="a":
                                pass

        output = (translate(ask))

        if type(output) == str:
                print(output)
        else:
                for  item in output:
                        print(item)
'''

'''
#####################################################
Using Pandas
#####################################################
In [1]: import pandas

In [2]: table = pandas.DataFrame([[2,3,6,8,4],[9,8,5,7,3]])

In [3]: table
Out[3]:
   0  1  2  3  4
0  2  3  6  8  4
1  9  8  5  7  3

In [4]: table =pandas.DataFrame([[2,3,6,8,4],[9,8,5,7,3]], columns = ["Mon", "Tue", "Wed", "Thu", "Fri"], index = [1,2])

In [5]: table
Out[6]:
   Mon  Tue  Wed  Thu  Fri
1    2    3    6    8    4
2    9    8    5    7    3


Working with Jupyter notebook
1. Navigate to the foler in terminal sn execute: jypyter Notebook

2. To work with file on the OS, use following commands:
import os
import pandas

2a. Read/display data:
data= pandas.read_json("address.json")
data= pandas.read_excel("address.xlxs", sheetname=0)

3. Use to list file in directory for:
os.listdir()

4. Set ID as index:
data.set_index('ID')

5.to find help in pandas use:
pandas.read_***?
eg. pandas.read_csv?

6. To open txt files or files sereated by a ';':
data= pandas.read_csv("address_semi-colons.txt", sep=";")

7.Set a column as an index:
data1 = data1.set_index("Address")

8.Select a field:
data1.loc["332 Hill St":"551 Alvarado St","Name":"Employees"]

9. Position based selection, use iloc:
data1.iloc[0:2,0:3]
data1.iloc[1,0:3]

10. Select a cell by mixing a string and integer, can use only ix:
data1.ix[1, "Name"] - Works tho but is deprecated

11.To drop/Delete column or row:
Column = data.drop("Address", 1)
row = data.drop("332 Hill St", 0)
###To drop a group of rows/columns
data.drop([0:3], 1 or 0)

12. Adding a column:
data['Continents']=data.shape[0]*['North Americas']
[data.shape] will list the amount of rows and columns

13. Adding an existing columns data to another column
data['Continents']=data["Country"]+","+"North Americas"

14. To add a new row:
i. Convert row ID to columns by adding '.T':
dataT = data.T

ii. Add following sections
dataT['144 Gill'] = ['United Kingdom','30','7','Lexo','Westland','UK,Europe']

iii. Convert columns back to index by adding [.T]:
 data = dataT.T

15. Using geopy for locations:
a.
i. from geopy.geocoders import Nominatim
ii. nom = Nominatim(scheme = "http")
iii. nom.geocode("3995 23rd St, San Francisco, CA 94114")
>>>Location(3995, 23rd Street, Noe Valley, SF, California, 94114, USA, (37.7529648, -122.4317141, 0.0))

16. Converting address string to Logitude and latitude values
i. n = nom.geocode("3995 23rd St, San Francisco, CA 94114")

n.latitude
>>>37.7529648
n.Longitude
>>>-122.4317141

17. Converting a a full address  into latitude and Longitude
i. First import Nominatim
from geopy.geocoders import Nominatim

ii. Add the full addresses together:
df['Address'] = df['Address']+','+df['City']+','+df['State']+','+df['Country']

ii.Put the  Nominatim fetch command  into a variable:
nom = Nominatim() or nom = Nominatim(scheme = "http")

iii. Creat a new colomn and apply the geocode:
df['Cordinates']=df['Address'].apply(nom.geocode)

...Use 'df.Cordinates[0]' to see each full output:
>>>Location(3666, 21st Street, Noe Valley, SF, California, 94114, USA, (37.756488877551, -122.429343346939, 0.0))

... or df.Cordinates[0].latitude
>>>37.756488877551


18. Creating a new column with only longitude & latitude values:
i. df['latitude']= df['Cordinates'].apply(lambda x: x.latitude)

ii.df['longitude']= df['Cordinates'].apply(lambda y: y.longitude)

NOTE: if the is an error in any of the addresses, it will return an error/NaN:
So you use a python tenary operator:
eg: df['latitude']= df['Cordinates'].apply(lambda x: x.latitude if x !=None else None)
"which means apply ... if its note equal to none, else insect 'None'."

Numpy:
1. import numpy
n = numpy.arange(27)
n
>>>array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24])

2. n.reshape(3,3,3):
>>>array([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],

       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],

       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])

3. Converting an array to numpylist:
m=numpy.asarray()[[12,132,345,23,21,, [],[]]]

4. Image processing with openCV:
i. import cv2

ii. img = cv2.imread("smallgray.png",0)
Note: 0 is to view image in gray/black&white and 1 is to view the image in RGB.colored

iii. img
>>>array([[187, 158, 104, 121, 143],
       [198, 125, 255, 255, 147],
       [209, 134, 255,  97, 182]], dtype=uint8)

5. To convert a numpy array to an image:
cv2.imwrite("newpic.png",img)
>>>True
(This will create a new picture in the folder)

6. Indexing, slicing & iterating:
i. for i in img:
    print(i)
>>>[187 158 104 121 143]
        [198 125 255 255 147]
        [209 134 255  97 182]

ii. for searching through columns:
...Convert it to a tabular form by switching sides:
for i in img.T:
    print(i)
    >>>[187 198 209]
        [158 125 134]
        [104 255 255]
        [121 255  97]
        [143 147 182]

iii. using flat:
for i in img.flat:
    print(i)
>>>187
158
104
121
143
198
125
255
255
147
209
134
255
97
182

7. Horizontal Stack
ims= numpy.hstack((img,img)) (i.e use a tuple)
ims
>>>array([[*187, 158, 104, 121, 143, *187, 158, 104, 121, 143],
                [*198, 125, 255, 255, 147, *198,125, 255, 255, 147],
                [*209, 134, 255,  97, 182, *209, 134, 255,  97, 182]], dtype=uint8)

8. Vertical Stack:
imv = numpy.vstack((img,img))
imv
>>>array([[*187, 158, 104, 121, 143],
                [198, 125, 255, 255, 147],
                [209, 134, 255,  97, 182],
                [*187, 158, 104, 121, 143],
                 [198, 125, 255, 255, 147],
                [209, 134, 255,  97, 182]], dtype=uint8)


9. Spliting an array vertically
lsi = numpy.vsplit(imv,3)
lsi
>>>[array([[187, 158, 104, 121, 143],
        [198, 125, 255, 255, 147]], dtype=uint8),
        array([[209, 134, 255,  97, 182],
        [187, 158, 104, 121, 143]], dtype=uint8),
        array([[198, 125, 255, 255, 147],
        [209, 134, 255,  97, 182]], dtype=uint8)]

ii. Spliting an array horizontally:
lsi = numpy.hsplit(imv,3)


Working with Folium mapsself.

1. Create/Find a point on a map
Import folium
map = folium.Map(location = [57.23, -81.97])

i. Save the map file as an HTML
map.save("Map1.html")

**Use Help(folium.Map) to find more examples ot apply

ii. map = folium.Map(location = [57.23, -81.97], zoom_start = 10, tile = "Mapbox bright")

2. Adding a marker on the map:
map.add_child(folium.Marker(location=[53.34,-75.33], popup ="Hi, I am here", icon = folium.Icon("red")))

2a. OR, Use a Feature group to make code more organized:
fg = folium.FeatureGroup(name = "My Map")
fg.add_child(folium.Marker(location=[53.34,-75.33], popup ="Hi, I am here", icon = folium.Icon("red")))

3. iterating through a list of cordinates:
fg = folium.FeatureGroup(name = "My Map")

for cordinates in [[53.34,-75.33], [53.14,-65.33]]:
        fg.add_child(folium.Marker(location=cordinates, popup ="Hi, I am here", icon = folium.Icon("red")))

'''
import pandas
import folium

data = pandas.read_csv('Volcanoes_USA.txt')

#data.columns
#data["LAT"]

lat = data['LAT']
lon_g = data['LON']
desc = data['ELEV']

map = folium.Map(location=[38.321015, -111.139220], zoom_start=5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name = "My Map")
#folium.Marker only accepts strings so rap any other value in the 'str()'
for i,j,d  in zip(lat,lon_g, desc):
        fg.add_child(folium.Marker(location=[i,j], popup =str(d), icon = folium.Icon("red")))


map.add_child(fg)

map.save("new.html")