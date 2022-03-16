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
f = hardware.str.contains("a") #returns True True False b/c hammer and saw contain "a", but wrench doesn't (to see result: debugger, HOVER OVER variable!)
g = hardware.str.upper()


#convert a series object to a python list
hardware_list = hardware.to_list() #there are other options than convert it to something other than a list. .to_...

#compare 2 series
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

g = ds1 == ds2
h = ds1 > ds2
i = ds1 <ds2

#Compare series to a list 
list_of_series = pd.Series([  #series with 3 elements (which are lists)
    ['Red', 'Gree','Wite'],['Red', 'Black'],['Yellow']])

#transform list of series to 1 element?
#list_of_series - list_of_series.apply(pd.Series).stack().reset_index(drop = True)


#sort a series
s = pd.Series(["100", "200", "python", "300.12", "400"]) #this one NEEDS TO BE IN DOUBLE QUOTES!! so all elements are considered a str
#in order to sort, all elements must be SAME data type
sorted_series = s.sort_values() #can sort by index or values

#s = pd.Series(['100', 200, 'python', 300.12, '400']) #this wouldn't work b/c different data types

#adding to a series
s = s.append(pd.Series(['500', 'php'])).reset_index(drop = True) #reset to reformat indexes

#calc frequency counts of each unique value of a given series
#(how much each # or value repeats)
import random
lists1 = [random.randrange(1,10) for i in range(0, 100)]
s = pd.Series(lists1) #convert list into series
result = s.value_counts()

print()