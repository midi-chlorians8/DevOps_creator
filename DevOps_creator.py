from folder_add import *
import PySimpleGUI as sg

sg.theme('DarkGrey13')   # Keep things interesting for your users

background_layout = [[sg.Image(r'pic_front.png')]]

layout = [
    [sg.Text("Название проекта:"), sg.Input(k='expr')],
    [sg.Text("        Выбор папки:"), sg.In(enable_events=True, key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Button('Create', size=(55, 1))],
    [sg.Text("Выбор папок под ваш проект:")],
    [sg.Checkbox('Creds', default=True, key="-CREDS-"),
     sg.Checkbox('DataBases', default=True, key="-DATABASES-"),
     sg.Checkbox('Terraform', default=False, key="-TERRAFORM-"),
     sg.Checkbox('Ansible', default=False, key="-ANSIBLE-"),
     sg.Checkbox('K8s', default=False, key="-K8S-"),
     sg.Checkbox('Monitorings', default=True, key="-MONITORINGS-"),
     sg.Checkbox('Repository', default=True, key="-REPOSITORY-"),
     sg.Checkbox('Description', default=False, key="-DESCRIPTION-"),
     sg.Checkbox('Video_rec', default=False, key="-VIDEOS-"),
     sg.Checkbox('Notes', default=True, key="-NOTES-"),
    ],
]

layout = background_layout + layout

window = sg.Window("DevOps create project", layout, finalize=True)
window['expr'].bind("<Return>", "_Enter")

while True:
    event, values = window.read()
    print(event, values)

    if event == 'Create' or event == "expr_Enter":
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
