#todos = []
while True:
    action = input("Type add, show, edit, complete or exit:")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            file = open("todos.txt", 'r') #File Handling
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open("todos.txt", 'w') #File Handling
            file.writelines(todos)
            file.close()
        
        case 'show' | 'display':
            file = open("todos.txt", 'r') #File Handling
            todos = file.readlines()
            file.close()

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
            new_todo = input("Enter a new todo: ")
            todos[n] = new_todo

        case 'complete':
            num = int(input("The number of todo to complete:"))
            todos.pop(num - 1)
            
        #case 'delete':
            #n = int(input("The todo to be deleted:"))
            #n = n - 1
            #tod = todos[n]
            #print(tod)

        case 'exit':
            break

        #case anonymous_:
            #print("Invalid data")