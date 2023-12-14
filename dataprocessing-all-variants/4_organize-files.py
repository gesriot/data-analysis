import os
import shutil

def organize_files(dir_path):
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

    for file_name in files:
        base_name = os.path.splitext(file_name)[0]

        new_dir_path = os.path.join(dir_path, base_name)

        os.makedirs(new_dir_path, exist_ok=True)

        shutil.move(os.path.join(dir_path, file_name), os.path.join(new_dir_path, file_name))

organize_files("смещено на 0.1 влево для ScaleID=4")
