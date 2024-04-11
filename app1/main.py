while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        file = open('files/todos.txt', 'w')
        file.writelines(todos)
        file.close()

        todos.append(todo.capitalize())

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' | 'display' in user_action:

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            row = f"{index + 1}-{item.strip('\n')}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"todo {todo_to_remove} was removed from the list"
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command is mot valid")

print("Bye!")
