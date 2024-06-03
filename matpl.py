import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 

#x = np.arange(1, 11)
#y1 = 2 * x
#y2 = 3 * x

# Plotting the graph
#plt.plot(x, y1)
#plt.plot(x, y2)

#plt.title("Line Plot")
#plt.xlabel("X-lable")
#plt.ylabel("Y-lable")
#plt.plot(x,y2,color='r',linestyle=':',linewidth=3)
#plt.grid(True)
# Displaying the graph

#plt.subplot(1,2,1)
#plt.plot(x,y1,color = 'g',linestyle = ':',linewidth = 2)

#plt.subplot(1,2,2)
#plt.plot(x,y1,color = 'r',linestyle = ':',linewidth = 2 )
#plt.show()

#bargraph
#stu = {'bob':87,'ok':45,'olivia':89,'mat':90}
#names = list(stu.keys())
#values = list(stu.values())
#plt.bar(names,values)
#print(plt.show())

#scattergraph
#x=[10,20,30,40,50,60]
#a=[6,8,4,9,3,2]
#plt.scatter(x,a,marker="*",c="g",s=100)
#print(plt.show())

#histogram
#data = [1,3,3,3,3,4,4,4,6,7,7,7,7,9,0,2,2,2]
#plt.hist(data)
#print(plt.show())

#histogram on data set
#iris = pd.read_csv(r'C:\Users\ASUS\Downloads\dataset.csv')
#print(iris.head())
#plt.hist(iris['Data_value'],bins=30,color='r')
#print(plt.show())

#box plot
#one = [1,2,3,4,5,6,7,8,9]
#two = [1,2,3,4,4,3,5,2,1]
#three = [6,7,8,9,7,5,4,5,7]
#data = list([one,two,three])
#plt.boxplot(data)
#print(plt.show())
#plt.violinplot(data,showmedians=True)
#plt.show()

#pie-charts
#fruit = ['apple', 'banana' , 'mango' , 'guava' , 'sagar']
#quantity = [67,34,100,29,32]
#plt.pie(quantity,labels=fruit)
#print(plt.show())
#plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['yellow','green','pink','red','black'])
#print(plt.show())
#plt.pie(quantity,labels=fruit,radius=2)
#plt.pie([1],colors=['w'],radius=1)
#print(plt.show())