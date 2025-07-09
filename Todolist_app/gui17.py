#Creating a Desktop GUI
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a todo")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
button = sg.Button("Add")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, button]],
                   font = ('Helvetica', 20))  # layout must be a list of lists

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
