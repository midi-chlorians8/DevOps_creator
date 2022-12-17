#################################################### STEP 1
# Add for linux - in file (folder_add.py)
#!/usr/bin/python3 

# Add section for link on DB creds - in file (folder_add.py)
#
#elif platform.system() == "Linux":
#        # create link on db
#        print('Linux platform - create link to DB creds')
#        os.system('ln -s {0} {1}'.format(os.path.join(os.getcwd(), main_folder_name, "DataBases",  main_folder_name + "_" + "DataBaseCreds.txt"),os.path.join( os.getcwd(), main_folder_name,"Creds", "DataBases_Creds")))
#    else:
#        pass

#################################################### STEP 2
# Для сборки в venv окружении (https://docs.python.org/3/library/venv.html) 
#sudo apt update -y && sudo apt install -y --reinstall python3-venv

#################################################### STEP 3
# Create python venv and activate
python3 -m venv venv && source venv/bin/activate

# requiremente.txt
pip install -r requirements.txt && pip freeze

# create bin
PATH_folder_add="../DevOps_creator.py"
PATH_icon="../icon.ico"
pyinstaller --onefile --windowed --icon $PATH_icon $PATH_folder_add 

# bin
mv ./dist/DevOps_creator ../DevOps_creator.bin

# clear
rm -rf build/ DevOps_creator.spec dist/ 

# diactivate and delete venv
PATH_env="./venv"
deactivate && rm -rf $PATH_env