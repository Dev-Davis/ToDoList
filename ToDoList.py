# todos = []


while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            # + "\n" adds new line in text file
            todo = input("Enter a task: ") + "\n"

            file = open('todo.txt', 'r')
            todos = file.readlines()

            todos.append(todo)

            # when new todo added it opens the file
            file = open('todo.txt',  'w')
            file.writelines(todos)
        case 'show':
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case 'edit':
            number = int(input('Number of item to edit: '))
            number = number - 1
            new_task = input('Enter new task: ')
            todos[number] = new_task
        case 'complete':
            number = int(input('Number of item to complete: '))
            todos.pop(number - 1)
        case 'exit':
            break

print("Bye!")
