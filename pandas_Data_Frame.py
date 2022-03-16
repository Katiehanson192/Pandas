import pandas as pd

#value of each key = a list
    #each key becomes columns
        #each value becomes a row
grades_dict = {'Wally': [87,96,70],
'Eva': [100,87,90],
'Sam': [94,77,90],
'Katie': [100, 81,82],
'Bob': [83,65,85]}

#series = ONE dimensional array
#data frame = 2 dimensional (each column in a DF is a Series)

grades = pd.DataFrame(grades_dict)

#changing row indexes to custom indexes
grades.index = ['Test1', 'Test2', 'Test3']

print(grades)

eva = grades["Eva"]
sam = grades.Sam

#using the loc and iloc methods
test2 = grades.loc['Test2']  #loc = location, uses the name of the index to get the row or column?

test1 = grades.iloc[0] #uses the number (integer) of the index to grab all of the row values 

#for consecutive rows (colon)
test1_thru_test3 = grades.loc['Test1':'Test3']
#for non-consecutive rows (comma, needs to be in a list)
test1_and_test3 = grades.loc[['Test1', 'Test3']] #need double [[]]

test1_and_test2 =grades.iloc[0:2] #does NOT include upper index (so 0:1 would only give us test 1, not test 1 and 2)

#printing out only Eva's and Katie's grades for Test1 and Test2
eva_and_katie_test1_and_test2 = grades[['Eva','Katie']].loc['Test1': 'Test2']
eva_and_katie = grades.loc['Test1': 'Test2', ['Eva','Katie']] #both of these ways work. Katie and Eva are non consecutive, test1 and test2 are consecutive
print(eva_and_katie_test1_and_test2)

#view only Sam's THRU Bob's grades for Test1 and Test3
sam_and_bob = grades.loc[['Test1', 'Test3'], 'Sam':'Bob'] #the extra brackets tell Python which ones are the rows and which ones are the columns?
print(sam_and_bob)
#if all desired parts are consecutive, don't need the extra brackets

#wally_ava_Katie_Bob = grades.loc['Test1', 'Test3'], ['Wally', 'Eva', 'Katie','Bob',]

#select everyone with an A grade
grades_A = grades[grades >=90]

#select everyone with a B grade
grades_B = grades[(grades >=90) & (grades < 90)]

#dataframe for everyone with an A or B grade
grades_A_or_B = grades[(grades >=90) | (grades >=80)] #| = pipe symbol for OR condition


#BY STUDENT
#pd.set_option("precision", 2) #need to fix this line
print(grades.describe()) #.describe gives count, mean, std, min, and max for every student!!

#by test
print(grades.T.describe()) 

#avg of all student grades on each test
print(grades.T.mean()) #can call the specific method.   

#sort rows by their indices (test name)
r_sorted_grades_i = grades.sort_index(ascending = False)

#sort columns by their column names (student names)
#axis = 1 indicates to sort by column indices
#axis = 0 indicates to sort by ROW indices

c_sorted_grades_i =grades.sort_index(axis = 1, ascending = False) #sorts based on the header!, ascending = False = descending order
print()