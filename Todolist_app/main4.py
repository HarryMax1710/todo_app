todos = []

while True:
    action = input("Type add, show, edit or exit:")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                #item = item.title()
                print(item)
        case 'edit':
            n = int(input("The todo to be edited:"))
            n = n - 1
            new_todo = input("Enter a new todo: ")
            todos[n] = new_todo
        #case 'delete':
            #n = int(input("The todo to be deleted:"))
            #n = n - 1
            #tod = todos[n]
            #print(tod)
        case 'exit':
            print("Todolist complete")
            break
        #case anonymous_:
            #print("Invalid data")