'''
Using the provided csv file and pandas dataframe, create a dataframe from the file. 
The csv file consists of 20 employees that have listed their preference to work on the given dates.
Their preference range is from 1 - 13 (1 being the most preferred). 
Come up with the optimal solution that meets the staffing needs and employee preference.

Constraints:

Employees should only be scheduled to work two shifts (2 days)
3-4 employees per shift (ideally 3)
'''

#days 11/27/2019 - 12/31/2019 (13 days total), 20 employees
import csv
import pandas as pd
import numpy as np

open_file = open('Holiday Schedule Ranking 2019.csv', 'r')
employee = csv.reader(open_file,delimiter=",")
header_row = next(employee)

df = pd.DataFrame(employee)

df.columns = ['Employee','11/27/2019','11/29/2019','11/30/2019','12/1/2019','12/21/2019','12/22/2019','12/23/2019','12/26/2019','12/27/2019','12/28/2019','12/29/2019','12/30/2019','12/31/2019']
print(df)

#create new df using 1s and 0s based on who's working which shifts?
work_schedule = pd.DataFrame()

#sorted_df = df.sort_values(by=['11/27/2019','11/29/2019','11/30/2019','12/1/2019','12/21/2019','12/22/2019','12/23/2019','12/26/2019','12/27/2019','12/28/2019','12/29/2019','12/30/2019','12/31/2019'])
#print(sorted_df)
