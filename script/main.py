import csv
import re
import os

folder_path = "../csv"

for filename in os.listdir(folder_path):
    if filename.startswith("sh."):
        with open(folder_path+"/"+filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = []
            for row in reader:
                new_row = [re.sub("sh.", "sh", cell) for cell in row]
                rows.append(new_row)

        with open(folder_path+"/"+filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

    if filename.startswith("sz."):
        with open(folder_path+"/"+filename, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = []
            for row in reader:
                new_row = [re.sub("sz.", "sz", cell) for cell in row]
                rows.append(new_row)

        with open(folder_path+"/"+filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

folder_path = "../csv"
for filename in os.listdir(folder_path):
    if filename.startswith("sz."):
        new_filename = filename.replace("sz.", "sz")
        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_filename))
    elif filename.startswith("sh."):
        new_filename = filename.replace("sh.", "sh")
        os.rename(os.path.join(folder_path, filename),
                  os.path.join(folder_path, new_filename))
