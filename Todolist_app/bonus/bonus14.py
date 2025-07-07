from fconvert14 import convert
from fparse14 import parse


feet_inches = input("Enter feet and inches:")

f, i = parse(feet_inches)
height = convert(f, i)
print(f"{f} feet and {i} inches is equal to {height} cm.")

if height < 90:
    print("Kid is too short")
else:
    print("Kid can use the slide.")