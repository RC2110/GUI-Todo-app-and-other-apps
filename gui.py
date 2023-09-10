# import PySimpleGUI as psg
#
# label1 = psg.Text("Select files to compress:")
# input1 = psg.Input()
# useraction1=psg.FilesBrowse("Choose")
#
#
# label2= psg.Text("Select destination folder:")
# input2 = psg.Input()
# useraction2=psg.FolderBrowse("Choose")
#
# switch = psg.Button("Compress")
#
# window = psg.Window("Compress Files", layout=[[label1,input1,useraction1], [label2,input2,useraction2],[switch]])
# window.read()
# window.close()

# import PySimpleGUI as pg
# label1 = pg.Text("Enter Feet:")
# user_input1 = pg.InputText()
# label2 = pg.Text("Enter Inch:")
# user_input2 = pg.InputText()
#
# switch = pg.Button("Convert")
#
# window = pg.Window("Convertor", layout=[[label1,user_input1],[label2, user_input2],[switch]])
# window.read()
# window.close()

# import PySimpleGUI as psg
# label = psg.Text("What are dolphins?")
# userchoice1= psg.Radio("Amphibians", group_id="question1")
# userchoice2= psg.Radio("Reptiles", group_id="question1")
# userchoice3= psg.Radio("Mammals", group_id="question1")
# userchoice4= psg.Radio("Birds", group_id="question1")
# switch = psg.Button("Submit")
#
# window = psg.Window("Questionnaire", layout= [[label],[userchoice1,userchoice2,userchoice3,userchoice4],[switch]])
# window.read()
# window.close()

import PySimpleGUI as psg
import functions

label1= psg.Text("Enter a Todo", font=('Helvetica', 15))
userip=psg.InputText(tooltip="Enter Todo", font=('Helvetica', 15), size=[33,10],
                     key="usr_ip")
e_lst=psg.Listbox(functions.get_todos(), enable_events=True, size=[50, 10], key='elist')
elst_button=psg.Button("Edit")
button=psg.Button("Add")

window = psg.Window("Your Todo app", layout=[[label1],[userip,button],[e_lst,elst_button]])

while True:
    event = window.read()
    action, input = event
    print(1,"event", event)
    print(2,"action",action)
    print(3,"input",input)
    match action:
        case "Add":
            e_todos= functions.get_todos()
            new_todos=input['usr_ip'] + '\n'
            e_todos.append(new_todos)
            functions.write_todos(e_todos)
            window['elist'].update(values=e_todos)
            print(e_todos)
        case "Edit":
            todos=functions.get_todos()
            ntodo=input['usr_ip']
            tdo2edit=input['elist'][0]
            indx=todos.index(tdo2edit)
            todos[indx]=ntodo
            functions.write_todos(todos)
            window['elist'].update(values=todos)
        case "elist":
            window['usr_ip'].update(value=input['elist'][0])
        case psg.WIN_CLOSED:
            break

window.close()


