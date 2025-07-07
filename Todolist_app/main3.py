#todos = []

#while True:
    #action = input("Type add, show or exit :")

    #match action:
        #case 'add':
            #todo = input("Enter a todo:")
            #todos.append(todo)
        #case 'show':
            #print(todos)
        #case 'exit':
            #break

todos = []

while True:
    action = input("Type add, show or exit :")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            print("Todolist complete")
            break
        case anonymous_:
            print("Invalid data")