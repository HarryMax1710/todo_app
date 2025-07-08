#Creating a Desktop GUI
import functions
import FreeSimpleGUI as sg

label = sg.Text("Type a todo")
input_box = sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label], [input_box, button]])  # layout must be a list of lists
window.read()
window.close()
