todos = []

while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter to do: ")
            todos.append(todo.capitalize())
        case 'show' | 'display':
            for items in todos:
                print(items)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")

print("Buy!")