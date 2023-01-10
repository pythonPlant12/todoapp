import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It's: ", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"
        functions.add_todo(todo)
    elif user_action.startswith('show' or 'display'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_action.startswith('edit'):
        try:

            todos = functions.get_todos()
            number = int(user_action[5:]) - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.capitalize() + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Please, enter a number")
        except IndexError:
            print("There is no this number in to do list.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except ValueError:
            print("Please, enter a number")
        except IndexError:
            print("There is no this number in to do list.")
            continue
    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an unknown command")
print("Bye!")
