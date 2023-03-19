import csv
import re
import os

folder_path = "../csv"

folder_path = "../csv"
list = []
for filename in os.listdir(folder_path):
    list.append(filename.split(".")[0])
with open("./result.txt", "w") as f:
    f.write("\",\"".join(list))
