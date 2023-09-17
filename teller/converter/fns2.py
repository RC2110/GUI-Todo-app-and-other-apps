# def get_todos(filepath='../../todos.txt'):
#     """ open the file from the file path and fetch the list of
#     todos."""
#     with open(filepath) as file_local:
#         todos = file_local.readlines()
#     return todos
#
# def write_todos(todos_arg, filepath='todos.txt'):
#     """ write the list with appended new todo in the file"""
#     with open(filepath, 'w') as file:
#         file.writelines(todos_arg)
#
# def convert(feet_local, inches_local):
#     metres= feet_local* 0.3048 + inches_local * 0.0254
#     print(f"{feet_local}feet and {inches_local}inches is {metres}metres")
#     return metres
#
# # print(__name__)
#
# if __name__ == "__main__":
#     print("Hi, I'm here!")
#
# gvh= 87


def parse(feet_inches):
    ls=feet_inches.split(" ")
    feet_local = float(ls[0])
    inches_local = float(ls[1])
    return {"feet":feet_local, "inches":inches_local}

# def water_state(temp):
#     if temp<=0:
#         return "Solid"
#     elif temp>0 and temp<100:
#         return "Liquid"
#     elif temp>=100:
#         return "Gas"

def water_state(temperature):
        FREEZING_POINT = int(0)
        BOILING_POINT = int(100)
        if temperature <= FREEZING_POINT:
            return "Solid"
        elif FREEZING_POINT < temperature < BOILING_POINT:
            return "Liquid"
        else:
            return "Gas"

if __name__ == "__main__":
    print(water_state(103))
    print(__name__)

fnme="gffyu"

