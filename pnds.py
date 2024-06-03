import pandas as pd 

iris = pd.read_csv(r'C:\Users\ASUS\Downloads\dataset.csv')
#shows first 5 lines of data (rows,columns)
print(iris.head()) 
#shows last rows and columns
print(iris.tail())
#gives mean , 25% , 50% , 75% means all the related data 
print(iris.describe())
#print only 3 rows and 3 columns from the given dataset
print(iris.iloc[0:3,0:3])
#this is for extracting the data by calling their names or rows names
print(iris.loc[0:3,("Period" , "Magnitude")])
#Dropping columns
print(iris.head())
print(iris.drop("Data_value" , axis = 1))
#mean , median ,min , max
#print(iris.mean())
#print(iris.median())
#print(iris.min())
#print(iris.max())
#function to perform the inbuild actions
def double(s):
    return s*2
print(iris[["Period" , "Data_value"]].apply(double))
#to count the data
print(iris["Series_reference"].value_counts())
#to sort the values
print(iris.sort_values(by = 'Data_value'))