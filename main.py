from datetime import timedelta
import Functions
from Hashtable import HashTable
from Package import Package
from Truck import Truck

package_data = Functions.read_package_csv('package.csv')
address_data = Functions.read_address_csv('addresses.csv')
distance_data = Functions.read_distance_csv('distances.csv')

# NOTE: These times you timedelta so they can be easily manipulated and analyzed
truck1_depart_time = Functions.time_converter('8:00')
truck1 = Truck(16, 18, [15, 19, 14, 13, 16, 20, 17, 1, 29, 30, 31, 34, 37, 40, 24, 26],
               0.0, '4001 South 700 East', truck1_depart_time)

truck2_depart_time = Functions.time_converter('9:05')
truck2 = Truck(16, 18, [3, 6, 18, 25, 28, 32, 36, 38, 2, 4, 5, 7, 8, 21, 22, 23],
               0.0, '4001 South 700 East', truck2_depart_time)

truck3_depart_time = Functions.time_converter('10:20')
# Package 9 address updated at 10:20 am
truck3 = Truck(16, 18, [9, 10, 11, 12, 27, 33, 35, 39], 0.0,
               '4001 South 700 East', truck3_depart_time)

package_hash_table = HashTable()


# This method takes a hash table and package information as input and loops through the package information array to
# create package objects and insert them into the hash table
def load_package_data(hash_table, package_info):
    # O(n) time complexity due to the for loop
    for p in package_info:
        p_id = int(p[0])
        p_address = p[1]
        p_deadline = p[2]
        p_city = p[3]
        p_zip = p[4]
        p_weight = p[5]
        p_status = p[6]
        p_special_notes = p[7]

        package = Package(p_id, p_address, p_deadline, p_city, p_zip, p_weight, p_status, p_special_notes)

        hash_table.insert(p_id, package)


# This method returns the index of an address in the array input as address_info
def find_address_index(address, address_info):
    # O(n) time complexity due to the for loop
    for item in address_info:
        if item[2] == address:
            return item[0]


# The following methods will be the actual implementation of the nearest neighbor algorithm

# This method finds the distance between two given addresses
def distance_between(address1, address2, distance_info):
    # Get the index of each address in the address_data array
    address1_index = int(find_address_index(address1, address_data))
    address2_index = int(find_address_index(address2, address_data))

    # The indices from address_data correspond to the indices in distance_data, so simply plug in those indices to
    # find the distance between the two addresses
    distance = distance_info[address1_index][address2_index]
    distance = float(distance)
    return distance


# This method takes in an address and compares it with the delivery address of each package in the list of
# undelivered packages on the truck. It then returns the address of the package with the nearest delivery address to
# the current address (from_address). truck_not_delivered will be truck.not_delivered, so it will be a list of package
# IDs which correspond to package objects stored in the hash table.
def min_distance_from(from_address, truck_not_delivered, hash_table):
    # min_distance set to 1000.0 to ensure that the first address compared will always be closer
    min_distance = 1000.0
    nearest_package_address = None
    package_id_to_remove = None

    # Loop through the truck inventory and find the distance between each package address and the from_address.
    # Compare that distance with the current min_distance to find the nearest neighbor.
    # Return the delivery address of that nearest neighbor package
    # O(n) time complexity due to for loop
    for package_id in truck_not_delivered:
        # Finds the package object stored in the hash table corresponding to package ID in the truck inventory
        package = hash_table.lookup(package_id)
        # Updates min_distance if a package is found to have a closer delivery address to from_address
        if distance_between(from_address, package.address, distance_data) < min_distance:
            package_id_to_remove = package_id
            nearest_package_address = package.address
            min_distance = distance_between(from_address, package.address, distance_data)

    return nearest_package_address, package_id_to_remove


def deliver_packages(truck, hash_table, distance_info):
    while len(truck.not_delivered) > 0:
        delivery_address, package_delivered_id = min_distance_from(truck.current_address, truck.not_delivered,
                                                                   hash_table)
        package_delivered_id = int(package_delivered_id)
        package = hash_table.lookup(package_delivered_id)
        distance = distance_between(truck.current_address, delivery_address, distance_info)
        # Increment the distance travelled by the truck
        truck.distance_travelled += distance
        # Remove the delivered package from the truck.not_delivered list
        truck.not_delivered.remove(package_delivered_id)
        # Change the truck current address to the address of the most recently delivered package
        truck.current_address = delivery_address
        # Increment the current time of the truck
        truck.current_time += timedelta(hours=distance / truck.speed)
        # Update the delivered package departure and delivery times
        package.depart_time = truck.departure_time
        package.delivery_time = truck.current_time

        # print(f'Package {package_delivered_id} departed at {package.depart_time}'
 #             f' and was delivered at {truck.current_time}!')

    distance_to_hub = distance_between(truck.current_address, '4001 South 700 East', distance_info)
    truck.distance_travelled += distance_to_hub
    truck.current_address = '4001 South 700 East'
    truck.current_time += timedelta(hours=distance_to_hub / truck.speed)
    #print(
#        f'The truck travelled: {round(truck.distance_travelled, 0)} miles and arrived back at the hub at: {truck.current_time}')


load_package_data(package_hash_table, package_data)

deliver_packages(truck1, package_hash_table, distance_data)
deliver_packages(truck2, package_hash_table, distance_data)
# Truck 3 departs at 10:20 am, it will be driven by the truck 1 driver after he arrives back at the hub. It contains
# package 9 which had the wrong address initially listed and was not updated until 10:20 am. Thus, the truck cannot
# leave until that package address is updated.
deliver_packages(truck3, package_hash_table, distance_data)


# NOTE: For the interface, if they enter a time before 10:20, return the old package 9 address, if the enter 10:20 or
# later, return the updated address

# User command line interface
class Main:
    # Gets input from user
    user_time = input("Please enter a time (24-hour clock) at which to check package information - (Ex. 22:00): ")
    user_input = input("If you would like to view a single package, please enter the package ID number. Type 'All' to "
                       "view all packages: ")

    # Converts user_time into a timedelta object
    user_time = Functions.time_converter(user_time)

    # If statement to check if the user requested all packages or a single package
    if user_input in ('All', 'ALL', 'all'):
        for i in range(1, 41):
            package = package_hash_table.lookup(i)
            package.package_status(user_time)

            # If user_time is before 10:20 am then set the address and zip code to the address and zip before it was
            # updated at 10:20 am
            if user_time < timedelta(hours=10, minutes=20) and package.id == 9:
                package.address = '300 State St'
                package.zip = '84103'

            # Print package info
            print(f"ID: {package.id} | Delivery Address: {package.address} | City: {package.city} | Zip Code: "
                  f"{package.zip} | Deadline: {package.deadline} | Departure Time: {package.depart_time} | "
                  f"Delivery Time: {package.delivery_time} | Weight(kg): {package.weight} | Package Status: "
                  f"{package.status} | Special Notes: {package.special_notes}")

    elif 1 <= int(user_input) <= 40:
        package = package_hash_table.lookup(int(user_input))
        package.package_status(user_time)

        # If user_time is before 10:20 am then set the address and zip code to the address and zip before it was
        # updated at 10:20 am
        if user_time < timedelta(hours=10, minutes=20) and package.id == 9:
            package.address = '300 State St'
            package.zip = '84103'

        # Print package info
        print(f"ID: {package.id} | Delivery Address: {package.address} | City: {package.city} | Zip Code: "
              f"{package.zip} | Deadline: {package.deadline} | Departure Time: {package.depart_time} | "
              f"Delivery Time: {package.delivery_time} | Weight(kg): {package.weight} | Package Status: "
              f"{package.status} | Special Notes: {package.special_notes}")


# NOTE: When updating package departure and delivery times, remember to store them with timedelta*
