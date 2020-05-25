# This code should be used for the PyBoss homework for the Rice Bootcamp, May 2020.
# Requires a set of data called employee_data.csv in the same folder.
# The dataset should compose of Emp ID, Name, DOB, SSN, State

#1 Import modules
import os
import csv
import datetime

#2 Create lists to hold the data, plus a dictionary of states.
New_Emp_List = []
New_First_Name_List = []
New_Last_Name_List = []
New_DOB_List = []
New_SSN_List = []
New_State_List = []
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#3 find file path
csvpath = os.path.join('employee_data.csv')

#4 Upload and read the CSV file
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#Skip the header
    csv_header = next(csvreader)
#5 Populate the lists by looping through all the data.
    for row in csvreader:
        New_Emp_List.append(int(row[0]))
        New_First_Name_List.append(row[1].split(" ")[0])
        New_Last_Name_List.append(row[1].split(" ")[1])
        New_DOB_List.append(datetime.datetime.strptime(row[2],'%Y-%m-%d').strftime('%m/%d/%Y'))
        New_SSN_List.append(f'***-**-{row[3][-4:]}')
        New_State_List.append(us_state_abbrev[row[4]])

#6 zip all the lists together into a Tuple
Zipped = zip(New_Emp_List,New_First_Name_List, New_Last_Name_List, New_DOB_List,New_SSN_List, New_State_List)

#7 export to CSV
output_path = os.path.join("employee_data_reformatted.csv")
with open(output_path, 'w', newline = "") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
    for x in Zipped:
        csvwriter.writerow(x)