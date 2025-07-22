#The Frontend(main.py) which creates the CLI or GUI is decoupled from the Backend(functions.py).

#FILEPATH = filepath
#read_todos(filepath=FILEPATH)

def read_todos(filepath="todos.txt"): #Function(Parameters)
    """Read a text file and return the list of todo items.""" #Doc Strings 
    with open(filepath, 'r') as file_r: #With
        todo_s = file_r.readlines() #Variable Declaration
    return todo_s #Local Variable


def write_todos(todos_w, filepath="todos.txt"):
    """Write the todo items list in the text file.""" #Description
    with open(filepath, 'w') as file:
        file.writelines(todos_w)

#Maintain 2 lines gap from functions

if __name__ == "__main__":
    print(read_todos())
