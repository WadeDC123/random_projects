#just messing around with requests

import requests
import random

first = input("First Name: ")
middle = input("Middle Initial: ")
last = input("Last Name: ")
gender = input("Gender [M/F]: ")
year = input("Birth Year [XXXX]: ")
month = input("Birth Month [1-12]: ")
day = input("Birth Date [1-31]: ")
step = '1'
data = {'first':first,
        'middle': middle,
        'last': last,
        'gender': gender,
        'y': year,
        'm': month,
        'd': day,
        'type':'dl_fl',
        'step': '1'}

r = requests.post("http://www.highprogrammer.com/cgi-bin/uniqueid/dl_fl", data=data)
license_number = r.text[2421:2437] + str(random.randint(0,1))
print(license_number)
