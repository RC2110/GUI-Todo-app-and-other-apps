import PySimpleGUI
import PySimpleGUI as pg
from functions import convert

label1 = pg.Text("Enter Feet:")
user_input1 = pg.InputText(key='feet')
label2 = pg.Text("Enter Inch:")
user_input2 = pg.InputText(key='inch')

switch = pg.Button("Convert")
buttn = pg.Button("Exit")
op=pg.Text('', key='out')

window = pg.Window("Convertor", layout=[[label1,user_input1],[label2, user_input2],[switch, op],[buttn]])
while True:
    data = window.read()
    event, inp = data
    if event == 'Exit':
        exit()
    if pg.WIN_CLOSED:
        break

    ft=inp['feet']
    inc=inp['inch']
    metre = convert(ft,inc)
    window['out'].update(value=f"{metre}")

window.close()