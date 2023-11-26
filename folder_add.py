from recurs_copy import *

import os, sys
import platform
import datetime
if platform.system() == "Windows":
    import winshell


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

    today = datetime.date.today()
    formatted_date = today.strftime("%d-%m-%Y")

    root_path = main_folder_name + '/'

    if values['-CREDS-'] == True:
        create_dir(root_path + "Creds")
        f = open(root_path + "Creds/"+main_folder_name+"_"+"AWS_Creds.txt", "x")
        f.write("My AWS account in project\n\n")

        f.write("Account ID: \n")
        f.write("IAM user: \n")
        f.write("password: \n\n\n")

        f.write("export AWS_ACCESS_KEY_ID=\n")
        f.write("export AWS_SECRET_ACCESS_KEY=\n")
        f.write("export AWS_DEFAULT_REGION=\n")
        f.close()

        f = open(root_path + "Creds/" + main_folder_name + "_" + "System_Control_Version_Creds.txt", "x")
        f.write("Url:\n\n")
        f.write("Login:\n")
        f.write("Password:\n")

        f = open(root_path + "Creds/" + main_folder_name + "_" + "Creds_Monitorings.txt", "x")
        f.write("My Monitorings in project :\n\n")
        f.write("Creds Grafana:\n")

        f.write("Dev\n")
        f.write("URL:\n")
        f.write("Login:\n")
        f.write("Password:\n\n")

        f.write("Qa\n")
        f.write("URL:\n")
        f.write("Login:\n")
        f.write("Password:\n\n")

        f.write("Prod\n")
        f.write("URL:\n")
        f.write("Login:\n")
        f.write("Password:\n\n")

        f.close()

        create_dir(root_path + "Creds/instance_keys")



    if values["-VIDEOS-"] == True:
        create_dir(root_path + "Video_records")


    if values["-K8S-"] == True:
        create_dir(root_path + "K8s")

        source_directory = './Files/K8s/'
        destination_directory = root_path + "K8s/"
        add_project_files(source_directory, destination_directory)

    if values["-TERRAFORM-"] == True:
        create_dir(root_path + "Terraform")

        source_directory = './Files/Terraform/'
        destination_directory = root_path + "Terraform/"
        add_project_files(source_directory, destination_directory)

    if values["-ANSIBLE-"] == True:
        create_dir(root_path + "Ansible")

        source_directory = './Files/Ansible/'
        destination_directory = root_path + "Ansible/"
        add_project_files(source_directory, destination_directory)

    if values["-MONITORINGS-"] == True:
        create_dir(root_path + "Monitorings")
        f = open(root_path + "Monitorings/"+main_folder_name+"_"+"Description_Monitorings.txt", "x")
        f.write(f"Created date: {formatted_date}\n")
        f.write("My Monitorings in project :\n\n")
        f.close()

        f = open(root_path + "Monitorings/"+main_folder_name+"_"+"Alarms_list.txt", "x")
        f.write(f"Created date: {formatted_date}\n")
        f.write("Alarms_list:\n")
        f.write(" ===== Dev ===== \n")
        f.write(" 1) Db-dev CPU alarm \n")
        f.write(" 2) K8s can not autoscale \n")
        f.write(" ===== Dev ===== \n\n")
        f.write(" ===== Qa ===== \n")
        f.write(" ===== Qa ===== \n\n")
        f.write(" ===== Stage ===== \n")
        f.write(" ===== Stage ===== \n\n")
        f.write(" ===== Prod ===== \n")
        f.write(" ===== Prod ===== \n\n")
        f.close()


    if values["-REPOSITORY-"] == True:
        create_dir(root_path + "Repositories")
       

    if values["-DESCRIPTION-"] == True:
        create_dir(root_path + "Description")
        f = open(root_path + "Description/"+main_folder_name+"_"+"Proposal(TZ).txt", "x")
        f.write("Proposal(TZ):\n")
        f.close()

        f = open(root_path + "Description/"+main_folder_name+"_"+"ToDoList.txt", "x")
        f.write("1) \n")
        f.write("2) \n")
        f.write("3) \n")
        f.close()

        f = open(root_path + "Description/" + main_folder_name + "_" + "Description_proj.txt", "x")
        f.write("Description:\n")
        f.close()

    if values["-DATABASES-"] == True:
        create_dir(root_path + "DataBases")
        f = open(root_path + "DataBases/"+main_folder_name+"_"+"DataBaseCreds.txt", "x")
        f.write("DataBase type: Postgres 13.4\n\n\n")
        f.write("Creds DB Dev:\n\n")
        f.write("DB_HOST:\n")
        f.write("DB_NAME:\n")
        f.write("DB_PASSWORD:\n")
        f.write("DB_PORT:\n")
        f.write("DB_USERNAME:\n")
        f.write("Is_public_access?:\n\n\n")


        f.write("Creds DB Qa:\n\n")
        f.write("DB_HOST:\n")
        f.write("DB_NAME:\n")
        f.write("DB_PASSWORD:\n")
        f.write("DB_PORT:\n")
        f.write("DB_USERNAME:\n")
        f.write("Is_public_access?:\n\n\n")

        f.write("Creds DB Prod:\n\n")
        f.write("DB_HOST:\n")
        f.write("DB_NAME:\n")
        f.write("DB_PASSWORD:\n")
        f.write("DB_PORT:\n")
        f.write("DB_USERNAME:\n")
        f.write("Is_public_access?:\n")
        f.close()

        create_dir(root_path + "DataBases/Backups")

        f = open(root_path + "DataBases/"+main_folder_name+"_"+"Description_backups.txt", "x")
        f.write(f"Created date: {formatted_date}\n\n")
        f.write("Description our backups:\n\n")
        f.write(" ===== Dev ===== \n\n")
        f.write(" 1) Db-dev in AWS \n")
        f.write(" 2) Pg dumps on bastion dev (check that) \n")
        f.write(" \n===== Dev ===== \n\n")
        f.write(" ===== Qa ===== \n")
        f.write(" ===== Qa ===== \n\n")
        f.write(" ===== Stage ===== \n")
        f.write(" ===== Stage ===== \n\n")
        f.write(" ===== Prod ===== \n")
        f.write(" ===== Prod ===== \n\n")
        f.close()

        f = open(root_path + "Log_process.txt", "x")
        f.write("Description what I do every day:\n\n")
        f.write(f"{formatted_date}\n")
        f.close()

    if values["-NOTES-"] == True:
        create_dir(root_path + "NOTES")
        f = open(root_path + "Notes.txt", "x")
        f.write("My notes:\n\n")
        f.write(f"{formatted_date}\n")
        f.close()

    if platform.system() == "Windows":
        winshell.CreateShortcut(
        Path= os.path.join( os.getcwd(), main_folder_name,"Creds", "DataBases_Creds.lnk"),  #os.path.join(    os.path.dirname(os.path.realpath(__file__))    , "c1", "Creds", "DataBases_Creds.lnk"),
        Target=os.path.join(os.getcwd(), main_folder_name, "DataBases",  main_folder_name + "_" + "DataBaseCreds.txt"),
        #Icon=(r"c:\python\python.exe", 0),
        Description="Python Interpreter"
        )
    #"""
    elif platform.system() == "Linux":
        # create link on db
        print('Linux platform - create link to DB creds')
        os.system('ln -s {0} {1}'.format(os.path.join(os.getcwd(), main_folder_name, "DataBases",  main_folder_name + "_" + "DataBaseCreds.txt"),os.path.join( \
            os.getcwd(), main_folder_name,"Creds", "DataBases_Creds")))
    else:
        pass
