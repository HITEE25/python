import matplotlib.pyplot as plt

slices = [4,5,7,6]

activites = ['eat','sleep','work','play']

colors = ['r','g','b','y']

plt.pie(slices,labels=activites,colors=colors,shadow=True,radius=1.2,explode=(0,0,0.1,0),autopct="%1.1f%%")

plt.show()