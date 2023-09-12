def get_todos(filepath='../../todos.txt'):
    """ open the file from the file path and fetch the list of
    todos."""
    with open(filepath) as file_local:
        todos = file_local.readlines()
    return todos

def write_todos(todos_arg, filepath='todos.txt'):
    """ write the list with appended new todo in the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def convert(feet_local, inches_local):
    metres= feet_local* 0.3048 + inches_local * 0.0254
    print(f"{feet_local}feet and {inches_local}inches is {metres}metres")
    return metres

# print(__name__)

if __name__ == "__main__":
    print("Hi, I'm here!")

gvh= 87

