def get_todos(filepath='files/todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='files/todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo.capitalize() + '\n')

        write_todos(filepath='files/todos.txt', todos_arg=todos)

    elif user_action.startswith('show') | user_action.startswith('display'):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos, 'files/todos.txt')

            message = f"todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with this number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is mot valid")

print("Bye!")
