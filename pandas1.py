import pandas as pd

grades = pd.Series([87,100,94])

print(grades)  #default index values and elements for each index

a = pd.Series(98.6, range(3)) #array of same numnber repeated several times

print() #blank for python debugger. f5 key. values drop down arrow shows values in an array + max, min

b = grades[0]
c = grades.count()
d = grades.mean()

print(grades.describe()) #gives count, mean, std, min, max

grades = pd.Series([87,100,94], index = ['Wally', 'Eva', 'Sam']) #custom indexing! assigns names of students to each of the grades

#print(grades)

grades_dict = {'Wally': 87, 'Eva':100, 'Sam':94}

grades_ds = pd.Series(grades_dict) #key become indexes in Series and values become values for them

print(grades_ds)

eve = grades['Eva']
wally = grades.Wally #only works with string notation

e = grades.values #array of all values

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])

print()