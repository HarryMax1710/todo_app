#Creating a Desktop GUI
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a todo")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
button = sg.Button("Add")

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, button]],
                   font = ('Helvetica', 20))  # layout must be a list of lists

event, values = window.read()
print(event)
print(values)
window.close()
