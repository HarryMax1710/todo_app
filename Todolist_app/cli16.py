#The Frontend(main.py) which creates the CLI or GUI is decoupled from the Backend(functions.py).

#todos = []
#from functions import read_todos, write_todos
import functions
import time

CTD = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", CTD)

while True:
    action = input("Type add, show, edit, complete or exit:")
    action = action.strip()

   #Match-case Statement replaced by If-else Statement
    #if 'add' in action: #or 'new' in action
    if action.startswith('add'):
        #todo = input("Enter a todo:") + "\n"
        todo = action[4:] + "\n" #List Slicing

        #file = open("todos.txt", 'r')       #File Handling
        #todos = file.readlines()
        #file.close()
        todos = functions.read_todos() #Function(Arguments) #Global Variable
        # filepath = "todos.txt"
        #No need to close.This is the difference.
        todos.append(todo) 

        #file = open("todos.txt", 'w') #File Handling
        #file.writelines(todos)
        #file.close()
        functions.write_todos(todos) # filepath = "todos.txt" # todos_w = todos
        
    #elif 'show' in action:
    elif action.startswith('show'):
        todos = functions.read_todos()

            #new_todos = [] #Using for-loop
            #for item in todos:
                #new_item = item.strip('\n')
                #new_todos.append(new_item)
            #
            #new_todos = [item.strip('\n')for item in todos] #Using List Comprehension
            #
        for (index, item) in enumerate(todos):
                item = item.strip('\n')
                item = item.capitalize()
                print(index + 1, '-', item)
                #row = f"{index + 1}-{item}"
                #print(row)

    #elif 'edit' in action:
    elif action.startswith('edit'):
            #n = int(input("The todo to be edited:"))
        try:
            number = int(action[5:])
            number = number - 1

            todos = functions.read_todos()
                
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        
        except ValueError:
             print("Invalid command.")
             continue #Starts from the beginning of the loop again.

    #elif 'complete' in action:
    elif action.startswith('complete'):
            #number = int(input("The number of todo to complete:"))
        try:
            number = int(action[9:])

            todos = functions.read_todos()
            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{completed_todo}' was completed successfully."
            print(message)
            
        except IndexError:
            print("Index not in list")       
        #case 'delete':
            #n = int(input("The todo to be deleted:"))
            #n = n - 1
            #tod = todos[n]
            #print(tod)

    #elif 'exit' in action
    elif action.startswith('exit'):
        break

    else: #anonymous
        print("Invalid data")