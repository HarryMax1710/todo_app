names = ["tom", "ben", "john"]
names.sort() #Ascending Order
for i, j in enumerate(names):
    print(f"{i + 1}.{j.capitalize()}")

Subjects = ["Maths", "Physics", "Chemistry"]
Subjects.sort(reverse=True) #Descending Order
print(Subjects)