import os
import shutil

def add_project_files(src_directory, dst_directory):
    """
    Copies all files and folders from src_directory to dst_directory.

    :param src_directory: The path to the directory with files and folders of the project.
    :param dst_directory: The path to the directory where the files and folders should be copied.
    """
    # Checking for the existence of the source and destination directories
    if not os.path.exists(src_directory):
        print("The source directory does not exist:", src_directory)
        return
    if not os.path.exists(dst_directory):
        os.makedirs(dst_directory)

    # Copy all subdirs and files
    for item in os.listdir(src_directory):
        src_path = os.path.join(src_directory, item)
        dst_path = os.path.join(dst_directory, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)  #  Python 3.8 +
        else:
            shutil.copy2(src_path, dst_path)
