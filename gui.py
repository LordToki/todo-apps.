import func
import PySimpleGUI as SG

label = SG.Text("Type in to do")
input_box = SG.InputText(tooltip="Enter todo", key="todo")
add_button1 = SG.Button("Add")
add_button2 = SG.Button("Close")
list_box = SG.Listbox(values=func.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = SG.Button("Edit")
window = SG.Window("My todo APP",
                   layout=[[label],
                           [add_button2],
                           [input_box, add_button1], [list_box, edit_button]],
                   font=("helvetica",))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    if "Add" in event:
        todos = func.get_todos()
        new_todo = values["todo"] + "\n"
        todos.append(new_todo)
        func.write_todos(todos)
        window["todos"].update(values=todos)
    if "Edit" in event:
        todo_to_edit = values["todos"][0]
        new_todo = values["todo"]

        todos = func.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo + "\n"
        func.write_todos(todos)
        window["todos"].update(values=todos)
    if "todos" in event:
        window["todo"].update(value=values["todos"][0])
    elif "Close" in event:
        break

window.close