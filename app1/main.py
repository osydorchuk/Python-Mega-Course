while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter to do: ") + "\n"

            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

            todos.append(todo.capitalize())

            # file = open('files/todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.strip('\n')}"
                print(row)
        case 'edit':
            number = int(input("number of the todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("number of the todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")
