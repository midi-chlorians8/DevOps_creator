import os

# Функция проверяет не создана ли уже папка чтобы не бить ошибки
def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print("Created Directory : ", dir)
    else:
        print("Directory already existed : ", dir)
    return dir

#################################################################


def add_folder_in_project(main_folder_name, values):
    create_dir(main_folder_name)

    root_path = main_folder_name + '/'

    if values['-CREDS-'] == True:
        create_dir(root_path + "Creds")
        f = open(root_path + "Creds/AWS.txt", "x")
        f.write("My AWS account in project\n")
        f.close()
        create_dir(root_path + "Creds/Db_Creds")
        f = open(root_path + "Creds/Db_Creds/Db_creds.txt", "x")
        f.write("Creds DB Dev:\n\n\n")
        f.write("Creds DB Qa:\n\n\n")
        f.write("Creds DB Prod:\n\n\n")
        f.close()

    if values["-IMAGES-"] == True:
        create_dir(root_path + "Images")
        create_dir(root_path + "Images/Diagrams")
        create_dir(root_path + "Images/Screens")
        create_dir(root_path + "Images/Other")

    if values["-VIDEOS-"] == True:
        create_dir(root_path + "Videos")
        create_dir(root_path + "Videos/Backend_side")
        create_dir(root_path + "Videos/Front_end_side")
        create_dir(root_path + "Videos/Other")

    if values["-K8S-"] == True:
        create_dir(root_path + "K8s")

    if values["-TERRAFORM-"] == True:
        create_dir(root_path + "Terraform")

    if values["-CDK-"] == True:
        create_dir(root_path + "CDK")

    if values["-PROPOSAL-"] == True:
        create_dir(root_path + "Proposal")
        f = open(root_path + "Proposal/Description.txt", "x")
        f.write("Description:\n")
        f.close()

