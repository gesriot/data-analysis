import os
import time

def split_circles(file_path):
    """
    Разбивает csv-файл на несколько файлов circles*.txt по кругам
    """
    with open(file_path, "r") as file:
        lines = file.readlines()
    files = {}
    last_value = 0.0
    circle = 1

    for line in lines:
        parts = line.split(",")
        try:
            value = float(parts[5])
            if value < last_value - 0.2:
                for circle, lines in files.items():
                    with open(f"circle{circle}.txt", "w") as file:
                        file.write("\n".join(lines))
                files.clear()
                circle += 1

            last_value = value
            if circle not in files:
                files[circle] = []
            files[circle].append(line.strip())
        except ValueError:
            print(f"Could not parse '{parts[5]} as float'")

    for circle, lines in files.items():
        with open(f"circle{circle}.txt", "w") as file:
            file.write("\n".join(lines))

def split_circles_in_dirs(parent_dir):
    """
    Запуск circles для нескольких csv-файлов в разных папках,
    и удаление двух из них (которые неполные)
    """
    dirs = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]

    original_dir = os.getcwd()

    for dir_name in dirs:
        dir_path = os.path.join(parent_dir, dir_name)
        os.chdir(dir_path)

        csv_files = [f for f in os.listdir() if f.endswith(".csv")]

        for csv_file in csv_files:
            split_circles(csv_file)
        time.sleep(2)

        for file_name in ("circle1.txt", "circle7.txt"):
            try:
                os.remove(file_name)
            except FileNotFoundError:
                print(f"File {file_name} not found")

        os.chdir(original_dir)

split_circles_in_dirs("смещено на 0.1 влево для ScaleID=4")
