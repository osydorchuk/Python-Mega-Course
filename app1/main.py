todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter to do: ")
            todos.append(todo.capitalize())
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
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
            existing_todo = todos[number]
            break
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")