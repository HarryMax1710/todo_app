fi = input("Enter feet and inches:")

def parse(feet_inches):
    parts = fi.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    cms = feet * 30.48 + inches * 2.54
    return cms #f"{feet} feet and {inches} inches is equal to {cms} cms."

f, i = parse(fi)
print("fi", f, i)
height = convert(f, i)

if height < 90:
    print("Kid is too short")
else:
    print("Kid can use the slide.")