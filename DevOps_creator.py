from folder_add import *
import PySimpleGUI as sg

layout = [
            [sg.Text("        Выбор папки:"), sg.In(enable_events=True, key='-FOLDER-'), sg.FolderBrowse()],
            [sg.Text("Название проекта:"), sg.Input(k='expr')],
            [sg.Button('Cоздать', size=(55, 1))],
            [sg.Text("Выбор папок под ваш проект:")],
            [sg.Checkbox('Creds', default=True, key="-CREDS-"),
             sg.Checkbox('Images', default=True, key="-IMAGES-"),
             sg.Checkbox('Videos', default=True, key="-VIDEOS-"),
             sg.Checkbox('K8s', default=True, key="-K8S-"),
             sg.Checkbox('Terraform', default=True, key="-TERRAFORM-"),
             sg.Checkbox('CDK', default=True, key="-CDK-"),
             sg.Checkbox('Proposal', default=True, key="-PROPOSAL-"),
             ],
         ]

window = sg.Window("DevOps create project", layout)
while True:
    event, values = window.read()
    print(event, values)
    
    if event == 'Cоздать':
        name_proj = values['expr'] # Извлекли название проекта
        print(name_proj)
        fld = values['-FOLDER-'] # Получаем информацию с блока выбора папки
        os.chdir(fld) # Меняем директорию для сохранения
        add_folder_in_project(name_proj, values)
        break
    if event == sg.WIN_CLOSED:
        break


window.close()
         