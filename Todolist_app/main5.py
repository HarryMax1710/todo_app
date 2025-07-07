todos = []

while True:
    action = input("Type add, show, edit, complete or exit:")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Enter a todo:")
            todos.append(todo)
        case 'show' | 'display':
            for (index, item) in enumerate(todos):
                item = item.title()
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