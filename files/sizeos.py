import os

path = "."
files = os.listdir(path)

print("Report of files")

report = open("file.txt",'w')
report.write("Report")

for file in files:
    if os.path.isfile(file):
        size = os.path.getsize(file)

        kb = size / 1024
        mb = size / (1024 * 1024)
        report.write(f"{file} -> {size} | {kb:.2f} kb | {mb:.4f} mb\n")

print("updated")