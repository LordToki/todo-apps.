import func
import PySimpleGUI as sg

label = sg.Text("Type in to do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button1 = sg.Button("add")
add_button2 = sg.Button("close")
window = sg.Window("My todo APP",
                   layout=[[label],
                           [add_button2],
                           [input_box, add_button1]],
                   font=("helvetica",))

while True:
    event, values = window.read()
    print(event)
    print(values)

    if "add" in event:
        todos = func.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        func.write_todos(todos)
    elif "close" in event:
        break

window.close