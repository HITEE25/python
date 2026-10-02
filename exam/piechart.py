import matplotlib.pyplot as plt

slices = [5,3,8,5]

activites = ["eat","sleep","work","play"]

colors = ["r","y","g","b"]

plt.pie(slices,labels=activites,colors=colors,startangle=90,explode=(0,0,0.1,0),shadow=2,autopct="%1.1f%%")

plt.legend()
plt.show()

