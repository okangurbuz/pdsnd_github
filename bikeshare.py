import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_input_raw = input("Which city do you wanto analyze: ")

    city_input = city_input_raw.lower()

    city_name_chk ='2'

    while city_name_chk !='1':
        if city_input in CITY_DATA:
            city = city_input
            city_name_chk ='1'
        else:
            city_name_chk ='0'
            city_input_raw = input("You can choose one of theese city chicago, new york city, washington: ")
            city_input = city_input_raw.lower()


    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['route'] = df['Start Station'] + " - " + df['End Station']

    df['Trip Duration'] = df['Trip Duration'].astype(int)
    df['hour'] = df['Start Time'].astype(str)

    # TO DO: get user input for month (all, january, february, ... , june)

    month_input_raw = input("name of the month to filter by, or ""all"" to apply no month filter: ")

    month_input = month_input_raw.capitalize()

    month_name_chk ='2'

    while month_name_chk !='1':
        if month_input=="All":
            month = month_input
            month_name_chk ='1'
        elif month_input not in ('January','February','March','April','May','June','July','August','September','October','November','December'):
            month_input_raw = input("you should give month name correct, or ""all"" to apply no month filter: ")
            month_input = month_input_raw.capitalize()
            month_name_chk = '0'
        elif month_input not in set(df['month']):
            month_input_raw = input("this month doesnt exist in the sample data. you should try another one or ""all"" to apply no month filter: ")
            month_input = month_input_raw.capitalize()
            month_name_chk =' 0'
        else:
            month= month_input
            month_name_chk = '1'


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day_input_raw = input("name of the day to filter by, or ""all"" to apply no day filter: ")

    day_input = day_input_raw.capitalize()

    day_name_chk ='2'

    while day_name_chk !='1':
        if day_input=="All":
            day = day_input
            day_name_chk ='1'
        elif day_input not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'):
            day_input_raw = input("you should give day name correct, or ""all"" to apply no day filter: ")
            day_input = day_input_raw.capitalize()
            day_name_chk = '0'
        elif day_input not in set(df['day_of_week']):
            day_input_raw = input("this day doesnt exist in the sample data. you should try another one or ""all"" to apply no day filter: ")
            day_input = day_input_raw.capitalize()
            day_name_chk =' 0'
        else:
            day= day_input
            day_name_chk = '1'

    print('-'*40)
    return city, month, day

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    df['route'] = df['Start Station'] + " - " + df['End Station']

    df['Trip Duration'] = df['Trip Duration'].astype(int)
    df['hour'] = df['Start Time'].astype(str)

    if month != "All":
        df = df[df['month'] == month]

    if day != "All":
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    popular_month = df['month'].mode()[0]

    popular_month_count = df['month'].value_counts()[0]

    print("Most common month is " + popular_month + " and this month bikers rent a bike " + str(popular_month_count) + " times." )

    # TO DO: display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    popular_day_count = df['day_of_week'].value_counts()[0]

    print("Most common day of week is " + popular_day + " and this day bikers rent a bike " + str(popular_day_count) + " times." )

    # TO DO: display the most common start hour

    popular_hour = df['hour'].mode()[0]

    popular_hour_count = df['hour'].value_counts()[0]

    print("Most common hour of day is " + str(popular_hour) + " and this hour bikers rent a bike " + str(popular_hour_count) + " times." )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    popular_start = df['Start Station'].mode()[0]

    popular_start_count = df['Start Station'].value_counts()[0]

    print("Most common Start Station is " + popular_start + " and from this station bikers start their trips " + str(popular_start_count) + " times." )

    # TO DO: display most commonly used end station

    popular_end = df['End Station'].mode()[0]

    popular_end_count = df['End Station'].value_counts()[0]

    print("Most common End Station is " + popular_end + " and at this station bikers have ended their trips " + str(popular_end_count) + " times." )

    # TO DO: display most frequent combination of start station and end station trip

    popular_route = df['route'].mode()[0]

    popular_route_count = df['route'].value_counts()[0]

    print("Most common route is " + popular_route + " and this route has used beeen " + str(popular_route_count) + " times." )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print('Total travel time: ' + str(df['Trip Duration'].sum()))

    # TO DO: display mean travel time

    print('Average travel time: ' + str(round(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()

    print("Counts of user types:")
    print(user_types)

    print('\n')

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()

        print("Counts of user Gender types:")
        print(gender)
        print('\n')
    else:
        print("No Gender column for this city.")
        print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:

        min_birth_year = df['Birth Year'].min()

        max_birth_year = df['Birth Year'].max()

        print("Oldest biker's birth year is " + str(min_birth_year) + " and youngest biker's birth year is " + str(max_birth_year) + ".")

        common_birth_year = df['Birth Year'].mode()[0]

        df2 = df[df['Birth Year'] == common_birth_year]

        common_birth_year_count = df2['Birth Year'].count()

        print("Most common Birth Year is " + str(common_birth_year) + " and this year " + str(common_birth_year_count) + " bikers were born." )

    else:
        print("No Birth Year column for this city.")
        print('\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def see_raw():
            show_raw = input('\nWould you like to see raw data sample? Enter yes or no. \n')

            x = 0
            y = 5

            show_raw_chk ='2'

            while show_raw_chk !='1':
                if show_raw.lower() != 'yes':
                    show_raw_chk ='1'
                else:
                    print(df.iloc[x:y,0:5])
                    show_raw = input('\nWould you like to see more? Enter yes or no. \n')
                    show_raw_chk ='0'
                    x = x + 5
                    y = y + 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        see_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
