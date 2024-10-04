import csv
from datetime import timedelta


# This is a simple read csv method, each of the csv files will be read with the same method.

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        return list(reader)


# **In order to make the main.py file more readable, separate method aliases will be used for each csv file**

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

# Basic idea for how to make package objects, need to use a loop and add them to the hash table in real implementation

# packageData = read_package_csv('package.csv')
#
# test_package = Package(packageData[2][0], packageData[2][1], packageData[2][2], packageData[2][3],
#                        packageData[2][4], packageData[2][5], packageData[2][6], packageData[2][7])
# print(test_package)
