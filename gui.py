import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w"):
        pass

sg.theme("Reddit")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button(size=2, mouseover_colors="LightBlue2", tooltip="Add Todo",
                       key="add",
                       image_source="/Users/nikitalutsai/PycharmProjects/"
                                    "pythonProject1/pythonbasics/udemyCourse/"
                                    "GUI-programm/todoGUI/add.png")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10), highlight_background_color="LightBlue4")
edit_button = sg.Button("Edit")
complete_button = sg.Button(size=2, tooltip="Complete", key="complete",
                            image_source="/Users/nikitalutsai/PycharmProjects/pythonProject1/"
                                         "pythonbasics/udemyCourse/GUI-programm/todoGUI/complete.png")
exit_button = sg.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
# Title window
# Each row in GUI has to have its own list
# layout=([[item],[item1]]) "widgets"
window = sg.Window("My To-Do App", layout=layout, font=("Helvetica", 20))

# Display elements (program)
while True:
    # event e.g. String and values dictionary
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b, %d, %Y %H:%M:%S"))
    print(values)

    # Compare event()
    match event:
        case "add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update("")

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update("")
            except IndexError:
                sg.popup("You should select an item to Complete.", font=("Helveica", 20))

        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update("")
            except IndexError:
                sg.popup("You should select an item to Complete.", font=("Helveica", 20))

        case "Exit":
            break

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

# Close
window.close()
