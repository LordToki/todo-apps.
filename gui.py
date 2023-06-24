import func
import PySimpleGUI as sg
label = sg.Text("Type in to do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("add")

window = sg.Window("My todo APP", layout=[[label], [input_box, add_button]])
window.read()
window.close()
