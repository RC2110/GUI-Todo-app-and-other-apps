# # # # # # # # prin = "Enter your ideas:"
# # # # # # # # todo= input(prin)
# # # # # # # # todo2= input(prin)
# # # # # # # # todo3= input(prin)
# # # # # # # #
# # # # # # # # action = [todo, todo2, todo3, "lion", 123]
# # # # # # # # print((action[1:2]))
# # # # # # # #
# # # # # # # # # animals = ["lion", "tiger", 'ziraffe', 'Elephant', 'Horse']
# # # # # # # # #
# # # # # # # # # print(animals[-1])
# # # # # # #
# # # # # # # text = "Enter the title:"
# # # # # # # value = input(text)
# # # # # # #
# # # # # # # print(value)
# # # # # # #
# # # # # # # print("The length of the title is",len(value))
# # # # # #
# # # # # # # answers = ['Yes', 'No', 'Yes', 'No', 'No']
# # # # # # my_answer = input("What is your answer?")
# # # # # # answers = ['Yes', 'No', 'Yes' ,'No' , my_answer]
# # # # # # print
# # # # #
# # # # # my_answer = input('What is your answer?')
# # # # # answers = ['Yes', 'No', 'Yes', 'No', my_answer]
# # # # # print(answers)
# # #
# # # # my_answer = input("What is your answer?")
# # # # answers = ['Yes', 'No', 'Yes', 'No', my_answer]
# # # # print("You are looking at the reverse of your answer", answers[::-1])
# # #
# # # state = "Are you a human? (yes:1, no=0)"
# # # value=int(input(state))
# # # Names=[]
# # # if (value==1):
# # #      name= "Enter your name:"
# # #      username= input(name)
# # #      print("that's a Wonderful Name, {0}!" .format(username[:3]))
# # #      Names.append(username.capitalize())
# # #      print(" that's a Wonderful Name!", username[:3])
# # #      print(Names)
# # #
# # # else:
# # #     print("Welcome peculiar Alien! Let's roll!")
# #
# # # option = "Enter your choice:"
# # # vars = []
# # #
# # # while True:
# # #     var = input(option)
# # #     if var == str(0):
# # #         break
# # #     else:
# # #         vars.append(var)
# # #
# # # print(vars)
# #
# # # option = "Enter your choice:"
# # # vars = []
# # #
# # # while True:
# # #     var = input(option)
# # #     var1=var.capitalize()
# # #     vars.append(var1)
# # #     if var == str(0):
# # #         break
# # #
# # # print(vars)
# #
# #
# # a={'a':123, 'cf':"fh123", 'f2':{'ab':['wewe', 1234, 10e+02, [1, 2, 4, 5], {'1':'df', '2':(1, 2, 4), 'f':{1, 'r', 'daytime'}}]}}
# #
# # import pickle
# # wt = open('123.pkly', 'wb')
# # pickle.dump(a, wt)
# # wt.close()
# #
# # import pickle
# # g=open('123.pkly', 'rb')
# # q=pickle.load(g)
# # print(q)
# # g.close()
#
# import pickle
# file= open('decor.pkl', 'rb')
# q=pickle.load(file)
# print(q)
# fruits=["orange", "banana", "guava"]
#
# for items in fruits:
#     print(items.upper())
#

# from functions import get_todos, write_todos
import functions
import time

# print(help(get_todos))
while True:
    print(time.strftime("%A %b %d %Y, %I:%M %p"))
    user_prompt = input("Type add, show, edit, complete or exit:")
    user_prompt = user_prompt.strip()
    if user_prompt.startswith("add"):

            todos= functions.get_todos()
            # try:
            if bool(user_prompt[4:]):

                tdo = user_prompt[4:] + '\n'
                print("Done")
                todos.append(tdo)
                functions.write_todos(todos)

            else:

                tdo = input("Enter a Todo:") + '\n'
                todos.append(tdo)
                functions.write_todos(todos)
            # except NameError:
            #     print("This is going to be a test")


    elif user_prompt.startswith("show"):

            todos= functions.get_todos()

            if len(todos) == 0 :
                print("No todos yet! Add a todo first")
            else:
                # new_todos= []
                # for item in todos:
                #     item=item.strip('\n')
                #     new_todos.append(item)

                 # new_todos= [item.strip('\n') for item in todos]

                 for something, x in enumerate(todos):
                     x=x.strip('\n')
                     x=x.capitalize()
                     print(f"{something+1}.{x}")

    elif user_prompt.startswith("edit"):
            try:
                todos= functions.get_todos()

                if len(todos) == 0:
                    print("No todos added yet. Add a todo first")

                elif bool(user_prompt[5:]):

                    number = int(user_prompt[5:])

                    if number > len(todos):
                        print("The entered todo doesn't exit")
                    else:
                        todos[number - 1] = input("Enter the new todo:") + '\n'
                        print("done")
                        functions.write_todos(todos)
                else:
                          number = int(input("Enter the number of todo:"))
                          newtodo=input("Enter the new todo:")
                          todos[number - 1]=newtodo
                          functions.write_todos(todos)

            except ValueError:
                print("Enter a valid command")
                continue

    elif user_prompt.startswith("complete"):
            try:

                todos = functions.get_todos()

                if len(todos) == 0:
                    print("No todos added yet. Add a todo first")

                else:
                    todos = functions.get_todos()

                    if bool(user_prompt[9:]):

                        comp = int(user_prompt[9:])
                        removed=todos[int(comp)-1]
                        removed=removed.strip('\n')
                        todos.pop(int(comp)-1)

                        functions.write_todos(todos)

                        print("The completed todo '{0}' is successfully removed." .format(removed) )

                    else:

                       comp1 = int(input("Enter the completed todo:"))
                       if comp1 > len(todos):
                          print("The entered todo doesn't exit")
                       else:
                          todos = functions.get_todos()
                          removed=todos[comp1-1]
                          removed=removed.strip('\n')
                          todos.pop(comp1-1)

                          functions.write_todos(todos)
                          print("The completed todo '{0}' is successfully removed." .format(removed) )

            except ValueError:
                       print("Enter a valid command")
                       continue
            except IndexError:
                       print("The entered todo doesn't exist")
                       continue

    elif user_prompt.startswith("exit"):
            break
    else:
            print("You have not entered a command")

print("Bye")