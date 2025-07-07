password = input("Enter a new password:")
passw = {} #Dictionary
if len(password) >= 8:
    passw["length"] = True
else:
    passw["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

passw["digits"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

passw["up"] = uppercase

print(passw)
if all(passw.values()) == True:
    print("Strong Password")
else:
    print("Weak Password")