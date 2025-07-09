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

#
# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

window.read()
window.close()
#
# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()
#
def foo(oz):
    return oz * 29.57353