FILEPATH = "todo_gui.txt"


def get_todos(filename=FILEPATH):
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_local, filename=FILEPATH):
    with open(filename, "w") as file_local:
        file_local.writelines(todos_local)


if __name__ == "__main__":
    print("Hello from function")
    print(get_todos())