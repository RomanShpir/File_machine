import time
from datetime import datetime
import os
import shutil
from os.path import join, getsize


def get_extensions_list(path=r"E:\Shpir R\photo_test"):
    dictionary = {}
    for root, dirs, files in os.walk(path):
        for folders in dirs:
            # print(folders)
            dictionary[os.path.join(root, folders)] = []
    # print(dictionary)
    return dictionary


def organising_files():
    duplicates_folder = r"E:\Shpir R\Duplicates"
    dictionary = get_extensions_list()
    for folder_path in dictionary:
        print(folder_path)
        photos_list = os.listdir(folder_path)
        # print(photos_list)
        for photos in photos_list:
            # print(photos)
            if photos in [x for v in dictionary.values() for x in v]:
                try:
                    shutil.move(os.path.join(folder_path, photos), duplicates_folder)
                except OSError:
                    pass
            else:
                dictionary[folder_path].append(photos)
    print(dictionary)


while organising_files() is True:
    organising_files()


