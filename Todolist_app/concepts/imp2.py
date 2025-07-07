#Python Modules

import glob
myfiles = glob.glob("files/*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
#
import csv

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city:")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
#
import shutil

#shutil.make_archive(Name of the file, Type of File, Directory of the file)

shutil.make_archive("output", "zip", "files")
#
import webbrowser

st = input("Enter a search term: ")

webbrowser.open("https://www.google.com/search?q=" + st)

import random

#Random
# Get two numbers from the user and covert them to integers
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# Pick a random int using randint()
rand = random.randint(lower_bound, upper_bound) 

print(rand)