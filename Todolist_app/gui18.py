#Creating a Desktop GUI

import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")

td = sg.Text('', key='clock')
label = sg.Text("Type a todo")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
button = sg.Button("Add", size=10)
list_box = sg.Listbox(values = functions.read_todos(), key = 'todos',
                      enable_events = True, size = [45, 10])
edit_box = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-do App',
                   layout=[[td],
                           [label],
                           [input_box, button],
                           [list_box, edit_box, complete_button],
                           [exit_button]],
                   font = ('Helvetica', 20))  # layout must be a list of lists

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.read_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo = values['todos'][0]
                new_todo = values['todo']

                todos = functions.read_todos()
                index = todos.index(todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                  sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                tod = values['todos'][0]
                todos = functions.read_todos()
                todos.remove(tod)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
