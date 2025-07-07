#todos = []
while True:
    action = input("Type add, show, edit, complete or exit:")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo:") + "\n"

            #file = open("todos.txt", 'r')       #File Handling
            #todos = file.readlines()
            #file.close()
            with open("todos.txt", 'r') as file: #With
                todos = file.readlines()
            #No need to close.This is the difference.
            todos.append(todo)

            #file = open("todos.txt", 'w') #File Handling
            #file.writelines(todos)
            #file.close()

            with open("todos.txt", 'w') as file: #With
               file.writelines(todos)
        
        case 'show' | 'display':
            with open("todos.txt", 'r') as file: #With
                todos = file.readlines()

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

        case 'edit':
            n = int(input("The todo to be edited:"))
            n = n - 1

            with open("todos.txt", 'r') as file: #With
                todos = file.readlines()
            
            new_todo = input("Enter a new todo: ")
            todos[n] = new_todo + "\n"

            with open("todos.txt", 'w') as file: #With
               file.writelines(todos)

        case 'complete':
            number = int(input("The number of todo to complete:"))

            with open("todos.txt", 'r') as file: #With
                todos = file.readlines()

            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", 'w') as file: #With
               file.writelines(todos)

            message = f"Todo '{completed_todo}' was completed successfully."
            print(message)
            
        #case 'delete':
            #n = int(input("The todo to be deleted:"))
            #n = n - 1
            #tod = todos[n]
            #print(tod)

        case 'exit':
            break

        #case anonymous_:
            #print("Invalid data")