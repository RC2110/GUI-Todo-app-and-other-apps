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
