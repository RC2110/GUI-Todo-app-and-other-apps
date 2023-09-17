import PySimpleGUI as psg
import functions
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
         pass

# psg.theme_previewer()
ctime=psg.Text(key="tm")
label = psg.Text("Enter a Todo")
userip=psg.InputText(tooltip="Enter todo", key="user_ip")
button=psg.Button(image_source='neww.png',key='Add', image_size=(20,20), mouseover_colors='DarkGreen')
e_list=psg.Listbox(values=functions.get_todos(), size=[45,10],
                   enable_events=True, key="ex_list")
button2=psg.Button("Edit")
button3=psg.Button("Complete")
button4 = psg.Button("Exit")
# Dynamic way of defining layouts
# button=["add","edit", "close"]
# layout=[]
# for i in button:
#     layout.append(psg.Button([i]))
psg.theme('DarkTeal3')
# psg.theme('Green Mono')
window=psg.Window("Your Todo app", layout=[[ctime],
                                           [label],
                                           [userip, button],
                                           [e_list,button2, button3],
                                           [button4]])
while True:
    data=window.read(timeout=100)
    window['tm'].update(value=time.strftime("%A %b %d %Y, %I:%M:%S %p"))
    event, inp = data
    print(event)
    print(inp)
    match event:
        case "Add":
            if inp['user_ip']=='':
                psg.popup("Enter a todo")
            else:
                todos=functions.get_todos()
                ntodo= inp['user_ip']+'\n'
                todos.append(ntodo)
                functions.write_todos(todos)
                window['ex_list'].update(values=todos)
        case "Edit":
            try:
                ntodo=inp['user_ip'] +'\n'
                todo2edit=inp['ex_list'][0]
                todos=functions.get_todos()
                index=todos.index(todo2edit)
                todos[index]=ntodo
                functions.write_todos(todos)
                window['ex_list'].update(todos)

            except IndexError:
                psg.popup("Select a Todo.")
        case "Complete":
            try:
                comp_todo = inp['ex_list'][0]
                todos = functions.get_todos()
                todos.remove(comp_todo)
                window['ex_list'].update(values=todos)
                functions.write_todos(todos)
                window['user_ip'].update(value='')
            except IndexError:
                psg.popup("Select a Todo.")
        case "ex_list":
            try:
                todos = functions.get_todos()
                window['user_ip'].update(value=inp['ex_list'][0][0:-1])
            except IndexError:
                psg.popup("Enter a Todo.")
        case "Exit":
            break
        case psg.WIN_CLOSED:
            break

window.close()

