### Date created
26/09/2019

### Project Title
Explore_US_Bikeshare_Database

### Description

This project consist in a program (python) that helps the user (through an interactive dialog) to explore data (related to year 2017) of bikeshare services in three american cities: New York; Chicago and Washington. The program asks the users which city the user wants to explore data of. Then the user can specify the month (or all from january to june) and a specific weekday (or all). The analysis includes gender analysis, age of the users but also most common starting station, arrival station origin-destination combinations, together with trip duration, most common day of the week or most common hour of the day the service is being used. Descriptive statistics is used to provide insights to the user. Time, Numpy and Pandas library have been used to develop the program.

### Files used
bikeshare.py

Bikeshare data (provided by https://www.motivateco.com/)
chicago.csv
new_york_city.csv
washington.csv

### Credits
For the section of the code "# display most frequent combination of start station and end station trip" inspiration has been taken from the solution provided at this GitHub link: https://github.com/ozlerhakan/bikeshare/blob/master/bikeshare.py

The code was modified by changing the statements and, mainly, correcting a minor error, related to the duplication of the same message (misuse of .format). 

the original code was therefore changed from:

Name = df[['Start Station', 'End Station']].mode().loc[0]
    print("sentence is: {}, {}"\
            .format(name[0], name[1]))
to:

ChangedName = df[['Start Station', 'End Station']].mode().loc[0]
    print("Changedsentence is: {}"\
            .format(name[0]))

