p1=10
p2=12
print(f"Price of brinjal yesterday was {p1} and today it is {p2}")

#
for i, j in enumerate("Hiii"):
    print(i, j)
print("Length of hiii is:", len("Hiii"))
#
a = enumerate("Hrushikesh")
print(list(a))

#
#file = open(r"C:\Users\hrush\OneDrive\Desktop\Udemy\Python Course\Todolist_app", 'r')
#
member = input("Enter a new member:")
file = open("members.txt","a")
file.write(member)
file.close()
#
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for filename in filenames:
    file = open(f"{filename}","w")
    file.write("Hello")
    file.close()
#
files = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(filename,'r')
    content=file.read()
    print(content)
#List Comprehension
names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)
#
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)
#
numbers = [10, 20, 30]
numbers = [num * 2 for num in numbers]
print(numbers)
#
user_entries = ['10', '19.1', '20']
user_entries= [float(item) for item in user_entries]
print(sum(user_entries))


