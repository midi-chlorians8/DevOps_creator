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

        with open("Text_hints_files/Kubernetes_commands.txt", "r") as f:
            content = f.read()

        with open(root_path + "K8s/"  + "Kubernetes_commands.txt", "w") as f:
            f.write(content)

        # f = open(root_path + "K8s/" + main_folder_name + "_" + "Focus_to_K8s_clusters.txt", "x")
        # f.write("export AWS_ACCESS_KEY_ID=\n")
        # f.write("export AWS_SECRET_ACCESS_KEY=\n")
        # f.write("export AWS_DEFAULT_REGION=\n\n")


        # f.write("aws eks --region <region> update-kubeconfig --name <cluster_name>\n")
        # f.write("Dev\n\n")

        # f.write("Qa:\n")
        # f.write("aws eks --region <region> update-kubeconfig --name <cluster_name>\n\n")

        # f.write("Prod:\n")
        # f.write("aws eks --region <region> update-kubeconfig --name <cluster_name>\n\n")

        create_dir(root_path + "K8s/HelmCharts")


    if values["-TERRAFORM-"] == True:
        create_dir(root_path + "Terraform")
        create_dir(root_path + "Terraform/Terraform_Polygon")
        create_dir(root_path + "Terraform/Terraform_Work_Version")
        create_dir(root_path + "Terraform/Terragrunt")

        # f = open(root_path + "Terraform/" + main_folder_name + "_" + "Terraform_commands.txt", "x")
        # f.write("Вот список основных команд Terraform, которые вы можете использовать:\n\n**Основные команды:**\n1. `init` - Подготовьте рабочий каталог для других команд.\n2. `validate` - Проверьте, является ли конфигурация действительной.\n3. `plan` - Показать изменения, требуемые текущей конфигурацией.\n4. `apply` - Создать или обновить инфраструктуру.\n5. `destroy` - Уничтожить ранее созданную инфраструктуру.\n\n**Все остальные команды:**\n1. `console` - Попробуйте выражения Terraform в интерактивном командном интерфейсе.\n2. `fmt` - Отформатируйте вашу конфигурацию в стандартном стиле.\n3. `force-unlock` - Снять застрявшую блокировку на текущем рабочем пространстве.\n4. `get` - Установите или обновите удаленные модули Terraform.\n5. `graph` - Сгенерируйте график Graphviz шагов в операции.\n6. `import` - Свяжите существующую инфраструктуру с ресурсом Terraform.\n7. `login` - Получите и сохраните учетные данные для удаленного хоста.\n8. `logout` - Удалите локально сохраненные учетные данные для удаленного хоста.\n9. `metadata` - Команды, связанные с метаданными.\n10. `output` - Показать значения вывода из вашего корневого модуля.\n11. `providers` - Показать поставщиков, требуемых для этой конфигурации.\n12. `refresh` - Обновите состояние, чтобы соответствовать удаленным системам.\n13. `show` - Показать текущее состояние или сохраненный план.\n14. `state` - Расширенное управление состоянием.\n15. `taint` - Пометьте экземпляр ресурса как не полностью функциональный.\n16. `untaint` - Удалите состояние \"загрязненности\" из экземпляра ресурса.\n17. `version` - Показать текущую версию Terraform.\n18. `workspace` - Управление рабочим пространством.\n\n**Глобальные опции (используйте их перед подкомандой, если таковая имеется):**\n1. `-chdir=DIR` - Переключитесь на другой рабочий каталог перед выполнением данной подкоманды.\n2. `-help` - Показать этот вывод справки или справку для указанной подкоманды.")

        with open("Text_hints_files/Terraform_commands.txt", "r") as f:
            content = f.read()

        with open(root_path + "Terraform/"  + "Terraform_commands.txt", "w") as f:
            f.write(content)

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

    # if values["-CDK-"] == True:
    #     create_dir(root_path + "CDK")
    if values["-REPOSITORY-"] == True:
        create_dir(root_path + "SourceCode/application")

        with open("Text_hints_files/SourceCode/requirements.txt", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/application/"  + "requirements.txt", "w") as f:
            f.write(content)


        with open("Text_hints_files/SourceCode/Dockerfile", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/application/"  + "Dockerfile", "w") as f:
            f.write(content)


        with open("Text_hints_files/SourceCode/.env_example", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/application/"  + ".env_example", "w") as f:
            f.write(content)

        with open("Text_hints_files/SourceCode/main.py", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/"  + "main.py", "w") as f:
            f.write(content)




        with open("Text_hints_files/SourceCode/docker-compose.yaml", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/"  + "docker-compose.yaml", "w") as f:
            f.write(content)



        with open("Text_hints_files/DockerCompose_commands.txt", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/"  + "DockerCompose_commands.txt", "w") as f:
            f.write(content)





        with open("Text_hints_files/SourceCode/README.md", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/"  + "README.md", "w") as f:
            f.write(content)


        with open("Text_hints_files/SourceCode/.gitignore", "r") as f:
            content = f.read()

        with open(root_path + "SourceCode/"  + ".gitignore", "w") as f:
            f.write(content)

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
