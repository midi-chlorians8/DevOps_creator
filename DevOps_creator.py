from folder_add import *
import PySimpleGUI as sg

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [
    [sg.Text("Название проекта:"), sg.Input(k='expr')],
    [sg.Text("        Выбор папки:"), sg.In(enable_events=True, key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Button('Cоздать', size=(55, 1))],
    [sg.Text("Выбор папок под ваш проект:")],
    [sg.Checkbox('Creds', default=True, key="-CREDS-"),
     sg.Checkbox('K8s', default=True, key="-K8S-"),
     sg.Checkbox('Terraform', default=True, key="-TERRAFORM-"),
     sg.Checkbox('Monitorings', default=True, key="-MONITORINGS-"),
     sg.Checkbox('Description', default=True, key="-DESCRIPTION-"),
     sg.Checkbox('DataBases', default=True, key="-DATABASES-"),
     sg.Checkbox('Images', default=False, key="-IMAGES-"),
     sg.Checkbox('Videos', default=True, key="-VIDEOS-"),
     sg.Checkbox('CDK', default=False, key="-CDK-"),

     ],
]

window = sg.Window("DevOps create project", layout, finalize=True)
window['expr'].bind("<Return>", "_Enter")

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Cоздать' or event == "expr_Enter":
        name_proj = values['expr']  # Извлекли название проекта
        print(name_proj)
        fld = values['-FOLDER-']  # Получаем информацию с блока выбора папки
        if fld != '':
            os.chdir(fld)  # Меняем директорию для сохранения
        add_folder_in_project(name_proj, values)
        break
    if event == sg.WIN_CLOSED:
        break

window.close()
