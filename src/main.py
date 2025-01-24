from textnode import *
from os import path, listdir, mkdir
from shutil import copy, rmtree

STATIC_PATH: str = "./static/"
PUBLIC_PATH: str = "./public/"

def move_contents_folder_to_folder(source_path: str, target_path: str):
    if not path.exists(source_path):
        raise ValueError("Source path not valid")
    if not path.exists(target_path):
        raise ValueError("Target path not valid")
    delete_folder_contents(target_path)
    files = list_all_files_recursive(source_path)
    for file in files:
        file_srtucture = file.replace(source_path,"").split("/")
        target = target_path if target_path[-1] == "/" else target_path + "/"
        for item in file_srtucture:
            if "." in item:
                copy(file,target)
            else:
                target += item + "/"
                if not path.exists(target):
                    mkdir(target)

    
def list_all_files_recursive(folder_path: str) -> list[str]:
    if not path.exists(folder_path):
        raise ValueError("Path not valid")
    if folder_path[-1] != "/":
        folder_path += "/"
    file_paths = []
    for item in listdir(folder_path):
        if "." in item:
            file_paths.append(folder_path + item)
        else:
            file_paths.extend(list_all_files_recursive(folder_path + item + "/"))
    return file_paths

def delete_folder_contents(folder_path: str):
    if not path.exists(folder_path):
        raise ValueError("Path not valid")
    rmtree(folder_path)
    mkdir(folder_path)

def main():
    move_contents_folder_to_folder(STATIC_PATH, PUBLIC_PATH)
    
if __name__ == "__main__":
    main()