#
#with open("../files/tod.txt", 'r') as file:
    #content = file.read()

#print(content)

#Default-Strings-User Input
#Default-r mode-File Handling

#
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for filename in filenames:
    print(filenames[:-4])

#Python Functions
def name():
    message = "hrushikesh"
    msg = message.capitalize()
    return msg

naming = name()
print(naming)
print(len(naming))
#
def greet(message):
    msg = message.capitalize()
    return msg

greeting = greet("Good Morning")
print(greeting)
#
#
def drink(choice):
    dc = choice.capitalize()
    return dc

drunk = input("What drink would you like to have:")
drinking = drink(drunk)
print(drinking)
#
def strength(password):
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password"
    
    upper = False
    digit = False
    
    for char in password:
        if char.isupper():
            upper = True
        if char.isdigit():
            digit = True
        
    if upper and digit:
         return "Strong Password"
    else:
        return "Weak Password"
        
#Multi-line Strings
text = """
Lionel Messi is the GOAT of Football. \n\
Cristiano Ronaldo is the GOAT of Football.
Pele is the GOAT of Football.
Diego Maradona is the GOAT of Football.
Johan Cryuff is the GOAT of Football.
"""

print(text)

#
if __name__ == __main__:
    print("Hello")

#
def water_state(temperature):
    if temperature <= 0:
        return "Solid"
    elif 0 < temperature < 100:
        return "Liquid"
    else:
        return "Gas"
