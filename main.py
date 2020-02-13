import time, os, re, shutil
from datetime import datetime
from os.path import join, getsize


def get_all_folder_path(path=r"E:\Shpir R\photo_test"):
    dictionary = {}
    for root, dirs, files in os.walk(path):
        for folders in dirs:
            # print(folders)
            dictionary[os.path.join(root, folders)] = []
    # print(dictionary)
    return dictionary


def organising_files_moving_duplicates():
    duplicates_folder = r"E:\Shpir R\Duplicates" + "\\"
    original_files_folder = r"E:\Shpir R\TEST" + "\\"
    dictionary = get_all_folder_path()
    # GET ALL SUB FOLDERS
    number_of_runs = 0
    for folder_path in dictionary:
        # print(folder_path)
        # CREATE A LIST OF PHOTOS
        photos_list = os.listdir(folder_path)
        # print(photos_list)
        number_of_runs += 1
        for photos in photos_list:
            if photos in [x for v in dictionary.values() for x in v]:

                try:
                    # MOVE AND RENAME DUPLICATES
                    os.rename(os.path.join(folder_path, photos), duplicates_folder + str(number_of_runs) + " " + str(photos))
                except OSError:
                    pass
            else:
                # ADD FILE NAME TO PATH KEY IN DICTIONARY
                dictionary[folder_path].append(photos)
                for paths in dictionary:
                    # PASS ON SYSTEM FILE
                    if photos == "desktop.ini":
                        pass
                    else:
                        try:
                            # GET CREATION DATE OF FILE
                            file_created = os.path.getctime(paths + "\\" + photos)
                            creation_date = "Date created: " + time.ctime(file_created)
                            creation_year = re.search(r'(\d+){4}', creation_date).group(0)
                            # MOVE FILE TO FOLDER RELATED TO CREATION YEAR OF FILE
                            if photos.endswith(('.jpg', '.png', '.JPG', '.PNG', '.pdn')):
                                # CHECK IF "PHOTO" FOLDER EXISTS
                                if not os.path.exists(original_files_folder + creation_year):
                                    os.mkdir(original_files_folder + creation_year)
                                    # print("Directory ", creation_year, " Created ")
                                else:
                                    pass
                                    # print("Directory ", creation_year, " already exists")
                                shutil.move(paths + "\\" + photos, original_files_folder + creation_year)
                            # SEPARATE VIDEO FILES TO VIDEO FOLDER
                            elif photos.endswith('.mp4'):
                                # CHECK IF "VIDEO" FOLDER EXISTS
                                if not os.path.exists(original_files_folder + "Video" + " " + creation_year):
                                    os.mkdir(original_files_folder + "Video" + " " + creation_year)
                                    # print("Directory ", "Video" + " " + creation_year, " Created ")
                                else:
                                    pass
                                    # print("Directory ", "Video" + " " + creation_year, " already exists")
                                shutil.move(paths + "\\" + photos, original_files_folder + "Video" + " " + creation_year)
                        except:
                            pass


organising_files_moving_duplicates()