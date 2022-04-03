#Python v3.9
#source myvenv/bin/activate
#python -m pip install pysimplegui
# pyinstaller -F -w -i "C:\DevOps_create_new_project\icon.ico" DevOps_creator.py

#import os
#os.system('rik-i-morti.mp3')


from folder_add import *
"""
import os

# Функция проверяет не создана ли уже папка чтобы не бить ошибки
def create_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
    print("Created Directory : ", dir)
  else:
    print("Directory already existed : ", dir)
  return dir
# Функция проверяет не создана ли уже папка чтобы не бить ошибки

name = 'proj'

def add_folder_in_project(main_folder_name):
    create_dir(main_folder_name)

    root_path =  main_folder_name + '/'

    create_dir(root_path+"Creds")
    f= open(root_path+"Creds/aws.txt","w+")

    create_dir(root_path+"Creds/Db_Creds")
    f= open(root_path+"Creds/Db_Creds/Db_creds.txt","w+")

    create_dir(root_path+"Videos")
    create_dir(root_path+"K8s")
    create_dir(root_path+"Terraform")
    create_dir(root_path+"Proposal")
"""

import PySimpleGUI as sg

layout = [
            [sg.Text("Название проекта:"), sg.Input( k='expr') ],
            [sg.Button('Cоздать', size=(54,1)) ]
         ]

window = sg.Window("DevOps create project", layout)

while True:
    event, values = window.read()
    print(event, values)
    
    if event == 'Cоздать':
        #print(expr.va)
        name_proj = values['expr'] # Извлекли название проекта
        print(name_proj)
        
        add_folder_in_project(name_proj)
        break


    if event == sg.WIN_CLOSED:
        break

window.close()
         