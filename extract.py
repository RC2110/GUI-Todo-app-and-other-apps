import PySimpleGUI as psg
from functions import extract
import zipfile

label1 = psg.Text("Select file to extract:")
input1 = psg.Input()
useraction1 = psg.FileBrowse("Choose",key='file')


label2 = psg.Text("Select a destination:")
input2 = psg.Input()
useraction2 = psg.FolderBrowse("Choose",key='folder')

switch = psg.Button("Extract")
label3 = psg.Text(key='out')
bt2 = psg.Button("Exit")

label4 = psg.Text("Enter a name:")
inp4 = psg.InputText(key='nme', size=(15,1))

# label4 = psg.Text("Give zipped file a name:")
# input3 = psg.InputText(key="filename")


window = psg.Window("Extractor", layout=[[label1,input1,useraction1], [label2,input2,useraction2],[label4,inp4],[switch,label3],[bt2]])

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
    fle=inp['file']
    dest=inp['folder']
    Name1=inp['nme']
    extract(fle,dest,Name1)
    window['out'].update(value="Extraction Complete!")

window.close()
