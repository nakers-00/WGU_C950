import csv
from datetime import timedelta


# This is a simple read csv method, each of the csv files will be read with the same method.

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        return list(reader)


# In order to make the main.py file more readable, separate method aliases will be used for each csv file

# Reads package information from package.csv file
read_package_csv = read_csv

# Reads address information from address.csv file
read_address_csv = read_csv

# Reads the distance information from distance.csv file into a 2d array to hold the distances between each address
read_distance_csv = read_csv


# This method will be used in main.py to take a user input time and convert it into a form that can be compared more
# easily
# The input must be in 24-hour clock
def time_converter(time):
    (h, m) = time.split(':')

    converted_time = timedelta(hours=int(h), minutes=int(m))
    return converted_time
