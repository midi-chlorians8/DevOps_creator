#from test import *

import os, sys
import platform
import datetime
if platform.system() == "Windows":
    import winshell


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
        f = open(root_path + "K8s/" + main_folder_name + "_" + "Focus_to_K8s_clusters.txt", "x")
        f.write("export AWS_ACCESS_KEY_ID=\n")
        f.write("export AWS_SECRET_ACCESS_KEY=\n")
        f.write("export AWS_DEFAULT_REGION=\n\n")


        f.write("aws eks --region <region> update-kubeconfig --name <cluster_name>\n")
        f.write("Dev\n\n")

        f.write("Qa:\n")
        f.write("aws eks --region <region> update-kubeconfig --name <cluster_name>\n\n")

        f.write("Prod:\n")
        f.write("aws eks --region <region> update-kubeconfig --name <cluster_name>\n\n")

        create_dir(root_path + "K8s/HelmCharts")


    if values["-TERRAFORM-"] == True:
        create_dir(root_path + "Terraform")
        create_dir(root_path + "Terraform/Terraform_Polygon")
        create_dir(root_path + "Terraform/Terraform_Work_Version")
        create_dir(root_path + "Terraform/Terragrunt")

    if values["-MONITORINGS-"] == True:
        create_dir(root_path + "Monitorings")
        f = open(root_path + "Monitorings/"+main_folder_name+"_"+"Description_Monitorings.txt", "x")
        f.write(f"Created date: {datetime.date.today()}\n")
        f.write("My Monitorings in project :\n\n")
        f.close()

    if values["-CDK-"] == True:
        create_dir(root_path + "CDK")

    if values["-DESCRIPTION-"] == True:
        create_dir(root_path + "Description")
        f = open(root_path + "Description/"+main_folder_name+"_"+"Proposal.txt", "x")
        f.write("Proposal:\n")
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

# Crete link to db creds:
    #print( os.path.join(  os.path.dirname(os.path.realpath(__file__)), "p52", "Creds", "DataBases_Creds.lnk") )
    #"""
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
