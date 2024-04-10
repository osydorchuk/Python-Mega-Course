while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter to do: ") + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo.capitalize())

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

#            new_todos = []
#            for item in todos:
#                new_item = item.strip('\n')
#                new_todos.append(new_item)
#            new_todos = [item.strip('\n') for item in todo]

            for index, item in enumerate(todos):
#                item = item.strip('\n')
                row = f"{index + 1}-{item.strip('\n')}"
                print(row)
#            print(f"Length is {index +1 }")
#            print(len(todos))
        case 'edit':
            number = int(input("number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("number of the todo to complete:: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")