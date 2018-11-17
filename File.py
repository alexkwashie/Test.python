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

import json

info = json.load(open("data.json", 'r'))

ask = input("Please Enter a word-:")

def translate(word):
        return info[word]

print(translate(ask))




