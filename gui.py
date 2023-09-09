# import PySimpleGUI as psg
#
# label = psg.Text("Enter your Todo")
# userip = psg.InputText()
#
# icon = psg.Button("Add")
# window = psg.Window("Your To-Do app", layout=[[label, userip], [icon]])
# window.read()
# window.close

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

import PySimpleGUI as psg
label = psg.Text("What are dolphins?")
userchoice1= psg.Radio("Amphibians", group_id="question1")
userchoice2= psg.Radio("Reptiles", group_id="question1")
userchoice3= psg.Radio("Mammals", group_id="question1")
userchoice4= psg.Radio("Birds", group_id="question1")
switch = psg.Button("Submit")

window = psg.Window("Questionnaire", layout= [[label],[userchoice1,userchoice2,userchoice3,userchoice4],[switch]])
window.read()
window.close()
