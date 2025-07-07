fi = input("Enter feet and inches:")


def convert(fi):
    parts = fi.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    cms = feet * 30.48 + inches * 2.54
    return cms #f"{feet} feet and {inches} inches is equal to {cms} cms."

height = convert(fi)

if height < 90:
    print("Kid is too short")
else:
    print("Kid can use the slide.")