# import the python module time (to use Time() functions etc. and libraries that will be needed
# Import numpy (foundamental package for scientific computing) and pandas (BSD-licensed library
# providing high-performance,  easy-to-use data structures and data analysis tools for the Python
# programming language)

import time
import numpy as np
import pandas as pd


# import the data files (.csv format) of the three cities Chicago, New York and store them
# in a dictionary, a data structure that stores pairs of elements, keys (elements names)
# and values


CITY_DATA={ 'chicago': './chicago.csv',
            'new york city': './new_york_city.csv',
            'washington': './washington.csv' }

# define a list to contain the three cities'names

cities = ['chicago','new york city','washington']

# define a list to contain the months'names

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

# define a list to contain the weekdays'names

days = ['monday', 'tuesday', 'wednsday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

# define a function to get some user defined/ selected filters for the analysis

def get_filters():

# Asks user to specify a city, month, and day to analyze.
# Returns:
# (str) city - name of the city to analyze
# (str) month - name of the month to filter by, or "all" to apply no month filter
# (str) day - name of the day of week to filter by, or "all" to apply no day filter

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # Print a line to separate results
    # I Get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    # - I create a while True loop to get the user's string input for the city choice,
    # - Since "raw_input" function appears to be deprecated I use the function "input"
    # - I use str() function to define the data type of the inputs
    # - I use the .lower() method to prevent case sensitive errors on the user side
    # - I use \n to create a line break
    # - I use "while True" function to create a while loop that iterate indefinitely until
    # a condition is met

    while True:
        city = str(input('\n Please enter a filter for the city you would like to explore. Enter: New York City, Chicago or Washington?\n')).lower()
        if city not in cities:
            print('{} is not a valid option, please input your choice again'.format(city))
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    # I Get user input for months (from january until june and I provide the option 'all').
    # HINT: Use a while loop to handle invalid inputs
    # - I create a while True loop to get the user's string input for the month's choice,
    # - Since "raw_input" function appears to be deprecated I use the function "input"
    # - I use str() function to define the data type of the inputs
    # - I use the .lower() method to prevent case sensitive errors on the user side
    # - I use \n to create a line break
    # - I use "while True" function to create a while loop that iterate indefinitely until
    # a condition is met

    while True:
        month = str(input('\n Please enter a filter for the month you would like to explore. Enter a month between january and june or simply type \"All\"  \n')).lower()
        if month not in months:
            print('{} is not a valid option, please input your choice again'.format(month))
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    # I Get user input for weekdays (I provide the option 'all').
    # HINT: Use a while loop to handle invalid inputs
    # - I create a while True loop to get the user's string input for the day's choice,
    # - Since "raw_input" function appears to be deprecated I use the function "input"
    # - I use str() function to define the data type of the inputs
    # - I use the .lower() method to prevent case sensitive errors on the user side
    # - I use \n to create a line break
    # - I use "while True" function to create a while loop that iterate indefinitely until
    # a condition is met

    while True:
        day = str(input('\n Please enter a filter for the weekday you would like to explore or simply type \"All\"  \n')).lower()
        if day not in days:
            print('{} is not a valid option, please input your choice again'.format(day))
            continue
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

# Loads data for the specified city and filters by month and day if applicable.

#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day

    # load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
#------------------------------------

# I define a function to ask the user if he/she wants to see the first 5 rows of the raw data
def get_rawdata(df):

# I create a list of possible answers to the question. The list can be used only in this function

    answers = ['y','n']

# I use a while loop to ask the user if he/she wants to see some row data

    while True:
        answer = str(input('\n would you like to see 5 sample rows from a raw data file? Please type "y" for yes and "n" for no.\n')).lower()
        if answer not in answers:
            print('{} is not a valid option, please input your choice again')
            continue
        if answer == 'y':
        # I create a panda's dataframe and I provide a sample .csv file (as it is a sample to see how data look I provide no choice on the city)
            #df = pd.read_csv(CITY_DATA[city]).sample(5)
        # I use the function .sample() to provide the view of 5 random rows
        # (instead of using .head() or .tail() to provide respectively the first 5 rows or the last five rows )
            df = df.sample(5)
            print (df)
            continue
        else:
            break

        print('-'*40)

#------------------------------------

def time_stats(df):
# Displays statistics on the most frequent times of travel

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The month bikeshare is used the most is :", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most chosen day of week is :", most_common_day_of_week)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular start hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
# Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    origin_destination = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common origin-destination is: {}"\
            .format(origin_destination[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
# Displays statistics on the total and average trip duration

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time is:", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("the mean travel time is:", mean_travel)

    # display max travel time
    max_travel = df['Trip Duration'].max()
    print("Max travel time :", max_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:

            # Display counts of gender
            gender = df['Gender'].value_counts()
            print(gender)

            # Display earliest, most recent, and most common year of birth
            older_user = df ['Birth Year'].min()
            younger_user = df ['Birth Year'].max()
            average_year = df ['Birth Year'].mode()[0]
            print("The oldest user was born in year:", older_user)
            print("The youngest user was born in year:", younger_user)
            print("The most common user was born in the year:", average_year)

            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        get_rawdata(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

# def main():
#     while True:
#         city, month, day = get_filters()
#         df = load_data(city, month, day)
#
#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)
#         table_stats(df, city)
#
#         display_data(df)
#
#         restart = input('\nWould you like to restart? Enter yes or no.\n')
#         if restart.lower() != 'yes':
#             break
#
#
# if __name__ == "__main__":
# 	main()


# def main():
#     while True:
#         city, month, day = get_filters()
#         df = load_data(city, month, day)
#
#         time_stats(df)
#         station_stats(df)
#         trip_duration_stats(df)
#         user_stats(df)
#
#         restart = input('\nWould you like to restart? Enter yes or no.\n')
#         if restart.lower() != 'yes':
#             break
#
#
# if __name__ == "__main__":
# 	main()
