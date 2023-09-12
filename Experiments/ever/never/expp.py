import PySimpleGUI as pg
import functions
label1 = pg.Text("Enter Feet:")
user_input1 = pg.InputText(key="feet")
label2 = pg.Text("Enter Inch:")
user_input2 = pg.InputText(key="inch")
switch = pg.Button("Convert")
reslt=pg.Text(key="result")

window = pg.Window("Convertor", layout=[[label1,user_input1],[label2, user_input2],[switch,reslt]])
while True:
    event=window.read()
    print(event)
    action, data = event
    print(action)
    print(data)
    feet=float(data['feet'])
    inch=float(data['inch'])
    metr=functions.convert(feet,inch)
    window['result'].update(value=f"{metr}")


