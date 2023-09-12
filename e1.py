# def get_average():
#     with open('test/test/test.txt', 'r') as file_local:
#          degrees = file_local.readlines()
#          degrees = degrees[1:]
#          values=[float(i) for i in degrees]
#          print(values)
#          average= sum(values)/len(values)
#     return average
#
# f=get_average()
# print(f)


# def get_maximum(degrees):
#     # celsius_local = [14, 15.1, 12.3]
#     maximum = max(degrees)
#     return maximum
#
# # celsius = get_maximum([14, 15.1, 12.3])
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

# def greet(message):
#     message=message.capitalize()
#     print("hey hey")
#     return message
#
# mesg= input("What greeting do you want?")
# meeting =  greet(mesg)
# print(meeting)


# from test import fns2
# from Experiments import fns
# from Experiments.test.test2.fns2 import parse
# from Experiments.ever.never.fns import convert
#
# ft_inchs=input("Enter the feet and inches:")
# t = parse(ft_inchs)
# feet1 = t['feet']
# inches = t['inches']
#
# g= convert(feet1, inches)
#
# if g<2:
#     print("The kid is too small, hence not safe for kid")
# else:
#     print("The kid is allowed to slide")
#
# # print(__name__)

# import glob
#
# paths = glob.glob("*.txt")
# print(paths)
#
# for filepaths in paths:
#     with open(filepaths, 'r') as file:
#         content= file.read()
#         print(content)

# import csv
#
# with open('weather.csv', 'r') as file:
#     content = list(csv.reader(file))
#     for i in content:
#        i[0] = i[0].capitalize()
# print(content)
#
# fg=input("Enter a city:")
# fg=fg.capitalize()
#
# for i in content:
#     if i[0]==fg:
#         print(i[1])

# import shutil
#
# shutil.make_archive("output", 'zip', 'Experiments' )

# import webbrowser
#
# var = input("Enter a search string:")
# var = var.replace(' ', '+')
# print(var)
#
# webbrowser.open("https://www.google.com/search?q=" + var)

# import glob
#
# glob.glob("*.txt")
#
# for in list:
#     with open("i", 'r') as file:
#         h= file.read()
#         print(h)
#
# import shutil
# shutil.make_archive('new','zip','teller')
#
# import csv
# with open("xyz.csv", 'r') as file:
#     l=list(csv.reader(file))
#     print(l)
#
# import webbrowser
# # i=input("Enter a keyword:")
# webbrowser.open("https://www.instagram.com")
#
# import json
# import time
#
# print(time.strftime("%A %b %d %Y, %I:%M %p"))
#
# with open("Experiments/quiz.json", 'r') as file:
#     content = file.read()
#
# data = json.loads(content)
# # print(data)
# # print(len(data))
#
# for w, i in enumerate(data):
#     print(f"Question-{w+1}", i['question'])
#     for index, m in enumerate(i['options']):
#         print(f"{index+1}.{m}")
#     user_choice=int(input("Enter your answer:"))
#     i['user choice']= user_choice
#
# sum=0
# for j, k in enumerate(data):
#     if k['user choice'] == k['Correct answer']:
#         sum=sum+1
#         result="Correct Answer"
#     else:
#         result="Correct Answer"
#
#     print(f"question{j+1}- Userinput{k['user choice']},"
#           f"correct answer{k['Correct answer']}")
#
# print("Results:\n", sum, '/', len(data))

# import PySimpleGUI as psg
# from teller.converter.fns import make_archive
#
# label1=psg.Text("Select Files to compress")
# userinp1=psg.InputText()
# label2=psg.Text("Select destination folder")
# userinp2=psg.InputText()
# button1=psg.FilesBrowse(key="Files")
# button2=psg.FolderBrowse(key="Folder")
# outputtext=psg.Text(key='output')
# switch=psg.Button("Convert")
#
# window=psg.Window("File Compressor", layout=[[label1, userinp1,button1], [label2, userinp2, button2],[switch,outputtext]])
# while True:
#     event=window.read()
#     print(1,"event", event)
#     action,data= event
#     print(2,"action", action)
#     print(3,"data",data)
#     filelist=data['Files'].split(';')
#     folder=data['Folder']
#     print(filelist)
#     print(folder)
#     print("string")
#     make_archive(filelist,folder)
#     window['output'].update(value="Conversion Complete!")
#
# window.read()
# window.close()

































