#os provides function to work with files and directeries
import os
#current directory
path = "."
files = os.listdir(path)

report = open("report.txt","w")
report.write("File size Report")

for file in files:
    #check if it is file and not directory
    if os.path.isfile(file):
        #size in bytes
        size = os.path.getsize(file)

        kb = size / 1024
        mb = size / (1024 * 1024)

        report.write(f"{file}->{size}bytes | {kb:.2f} kb | {mb:.4f} mb\n")

report.close()

print("data collected in report.txt")