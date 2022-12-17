# make bin for linux 

## STEP 1
### need add to scritp ./DevOps_creator/folder_add.py
- add in head file 
    #!/usr/bin/python3  

- add in bottom file (for set link on cred db)
    elif platform.system() == "Linux":
        # create link on db
        print('Linux platform - create link to DB creds')
        os.system('ln -s {0} {1}'.format(os.path.join(os.getcwd(), main_folder_name, "DataBases",  main_folder_name + "_" + "DataBaseCreds.txt"),os.path.join( \
        os.getcwd(), main_folder_name,"Creds", "DataBases_Creds")))
        else:
            pass

## STEP 2
### install pakage for build
- command 
    sudo apt update -y && sudo apt install -y --reinstall python3-venv 
    
- if need --reinstall ( python-pkg-resources build-essential python-dev )

## STEP 3.1
### make_bin_for_linux.sh need
    - requirements.txt (PyInstaller, PySimpleGUI)
    - PATH_folder_add="../DevOps_creator.py"
    - PATH_icon="../icon.ico"
    - PATH_env="./venv"

    !!! for make_bin_for_linux.sh need - put with folder DevOps_creator

## STEP 3.2
### start script for build 
sudo chmod +x make_bin_for_linux.sh && bash make_bin_for_linux.sh