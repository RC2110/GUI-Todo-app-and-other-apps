import PySimpleGUI as psg
from functions import compress
import zipfile

label1 = psg.Text("Select files to compress:")
input1 = psg.Input()
useraction1 = psg.FilesBrowse("Choose",key='files')


label2= psg.Text("Select destination folder:")
input2 = psg.Input()
useraction2 = psg.FolderBrowse("Choose",key='folder')

switch = psg.Button("Compress")
label3 = psg.Text(key='out')
bt2 = psg.Button("Exit")

label4 = psg.Text("Give a name:")
input3 = psg.InputText(key="filename",size=(15,1))


window = psg.Window("Compress Files", layout=[[label1,input1,useraction1], [label2,input2,useraction2],[label4,input3],[switch,label3],[bt2]])

while True:
    data = window.read()
    event,inp = data
    match event:
        case "Exit":
            break
        case psg.WIN_CLOSED:
            break

    print(event)
    print(inp)
    docs = inp['files'].split(';')
    dest = inp['folder']
    name = inp['filename']
    print(docs)
    print(dest)
    compress(docs,dest,name)
    window['out'].update(value="Compression Complete!")

window.close()
