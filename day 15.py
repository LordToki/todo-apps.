import func
import time

now = time.strftime("%d/%m/%Y, %H.%M.%S")
print("It is", now)
while True:
    case = input("Give command(add, show, complete, edit, or exit): ")
    if case.startswith("add"):
        todo = case[4:] + "\n"

        todos = func.get_todos()
        todos.append(todo)
        func.write_todos(todos)

    elif case.startswith("check"):
        todos = func.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif case.startswith("edit"):
        try:
            number = int(case[5:])
            print(number)
            number -= 1
            todos = func.get_todos()

            new_todo = input("new todo to insert: ")
            todos[number] = new_todo + "\n"

            func.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif case.startswith("complete"):
        try:
            number = int(case[9:])

            todos = func.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            func.write_todos(todos)

            message = f"{todo_to_remove} has been removed from your list"
            print(message)
        except IndexError:
            print("Such number is out of range")
            continue
        except ValueError:
            print("Your command is not valid")
            continue
    elif case.startswith("exit"):
        break
    else:
        print("your command is not valid")

print("Bye")
