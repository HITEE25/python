import csv

with open("name.csv","w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["roll","name","marks"])
    writer.writerow([12,"hitee",50])
    writer.writerow([34,"mihu",59])
    writer.writerow([25,"vency",55])

with open("name.csv","r") as file:
    reader = csv.reader(file)
    
    for word in reader:
        print(word)











