#Creating a Desktop GUI
from cgitb import enable

import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a todo")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
button = sg.Button("Add")
list_box = sg.Listbox(values = functions.read_todos(), key = 'todos',
                      enable_events = True, size = [45, 10])
edit = sg.Button("Edit")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, button],[list_box, edit]],
                   font = ('Helvetica', 20))  # layout must be a list of lists

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.read_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values =  todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
