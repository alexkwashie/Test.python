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
Colomn = data.drop("Address", 1)
row = data.drop("332 Hill St", 0)
###To drop a group of rows/colomns
data.drop([0:3], 1 or 0)

12. Adding a colomn:
data['Continents']=data.shape[0]*['North Americas']
[data.shape] will list the amount of rows and colomns

13. Adding an existing columns data to another colomn
data['Continents']=data["Country"]+","+"North Americas"

14. To add a new row:
i. Convert row ID to colomns by adding '.T':
dataT = data.T

ii. Add following sections
dataT['144 Gill'] = ['United Kingdom','30','7','Lexo','Westland','UK,Europe']

iii. Convert colomns back to index by adding [.T]:
 data = dataT.T
