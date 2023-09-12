
import PySimpleGUI as psg
import functions

label = psg.Text("Enter a Todo")
userip=psg.InputText(tooltip="Enter todo", key="user_ip")
button=psg.Button("Add")
e_list=psg.Listbox(functions.get_todos(), size=[45,10], enable_events=True, key="ex_list")
button2=psg.Button("Edit")

window=psg.Window("Your Todo app", layout=[[label], [userip, button], [e_list, button2]])
while True:
    data=window.read()
    event, inp = data
    print(event, inp)
    match event:
        case "Add":
            todos=functions.get_todos()
            ntodo= inp['user_ip']+'\n'
            todos.append(ntodo)
            functions.write_todos(todos)
            window['ex_list'].update(values=todos)
        case "Edit":
            ntodo=inp['user_ip'] +'\n'
            todo2edit=inp['ex_list'][0]
            todos=functions.get_todos()
            index=todos.index(todo2edit)
            todos[index]=ntodo
            functions.write_todos(todos)
            window['ex_list'].update(values=todos)
        case "ex_list":
            window['user_ip'].update(value=inp['ex_list'][0])

        case psg.WIN_CLOSED:
            break



window.read()
window.close()
