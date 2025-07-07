#prompt = "Enter a todo:"

#while 10>5:
    #todo = input(prompt)
    #print(todo)
    #print("Done..")

#prompt = "Enter a todo:"

#while True:
    #todo = input(prompt)
    #print(todo)
    #print("Done..")

#while False:
    #todo = input(prompt)
    #print(todo)
    #print("Done..")

#prompt = "Enter a todo:"

#while True:
    #todo = input(prompt)
    #todos = [todo]
    #print(todos)

prompt = "Enter a todo:"

todos=[]

while True:
    todo = input(prompt)
    print(todo.capitalize()) # -> Clean the room.
    print(todo.title()) # -> Clean The Room.
    todos.append(todo)
    print(todos)


