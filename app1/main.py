todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter to do: ")
            todos.append(todo.capitalize())
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("number of the to doto edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            existing_todo = todos[number]
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")