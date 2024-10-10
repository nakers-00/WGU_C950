# Course: C950 - Student ID: 011359614
from datetime import timedelta
import Functions
from Hashtable import HashTable
from Package import Package
from Truck import Truck
from builtins import ValueError

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
# O(n^2) time complexity because the for loop calls hash_table.insert(), which is a method of the HashTable class and
# contains a for-loop
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


# The following methods will be involved in the actual implementation of the nearest neighbor algorithm
# This method returns the index of an address in the array input as address_info
# O(n) due to the for-loop
def find_address_index(address, address_info):
    # O(n) time complexity due to the for loop
    for item in address_info:
        if item[2] == address:
            return item[0]


# This method finds the distance between two given addresses. This method has a time complexity of O(n) because it
# calls find_address_index which has a for-loop and is therefore O(n)
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
# It has O(n^2) time complexity due to a for loop which calls the .lookup() method and distance_between() method.
# The .lookup() and distance_between methods both have O(n) time complexity and they are nested at the same level within
# the outer for-loop; therefore, the time complexity is O(n * 2n) which would simply be O(n^2).
def min_distance_from(from_address, truck_not_delivered, hash_table):
    # min_distance set to 1000.0 to ensure that the first address compared will always be closer
    min_distance = 1000.0
    nearest_package_address = None
    package_id_to_remove = None

    # Loop through the truck inventory and find the distance between each package address and the from_address.
    # Compare that distance with the current min_distance to find the nearest neighbor. Return the delivery address
    # of that nearest neighbor package.
    for package_id in truck_not_delivered:
        # Finds the package object stored in the hash table corresponding to package ID in the truck inventory
        package = hash_table.lookup(package_id)
        # Updates min_distance if a package is found to have a closer delivery address to from_address
        distance = distance_between(from_address, package.address, distance_data)
        if distance < min_distance:
            package_id_to_remove = package_id
            nearest_package_address = package.address
            min_distance = distance

    return nearest_package_address, package_id_to_remove


# This method uses the methods and objects defined above to determine an efficient order to deliver the packages.
# The time complexity is O(n^3) due to a while-loop which calls the .lookup() (O(n)), min_distance_from() (O(n^2)), and
# distance_between() (O(n)) methods. Due to the time complexities and organization of these methods, the time complexity
# of deliver_packages() simplifies to O(n^3).
def deliver_packages(truck, hash_table, distance_info):
    # O(n) time complexity from while loop
    while len(truck.not_delivered) > 0:
        # O(n^2) time complexity
        delivery_address, package_delivered_id = min_distance_from(truck.current_address, truck.not_delivered,
                                                                   hash_table)
        package_delivered_id = int(package_delivered_id)
        # O(n) time complexity
        package = hash_table.lookup(package_delivered_id)
        # O(n)
        distance = distance_between(truck.current_address, delivery_address, distance_info)
        # Increment the distance traveled by the truck
        truck.distance_traveled += distance
        # Remove the delivered package from the truck.not_delivered list
        truck.not_delivered.remove(package_delivered_id)
        # Change the truck current address to the address of the most recently delivered package
        truck.current_address = delivery_address
        # Increment the current time of the truck
        truck.current_time += timedelta(hours=distance / truck.speed)
        truck.time_distance_list.append([truck.current_time, truck.distance_traveled])
        # Update the delivered package departure and delivery times
        package.depart_time = truck.departure_time
        package.delivery_time = truck.current_time

    # O(n)
    # The address of the hub is input directly as the hub address. If this program is being used in another city/state,
    # the hub address should be updated here.
    distance_to_hub = distance_between(truck.current_address, '4001 South 700 East', distance_info)
    truck.distance_traveled += distance_to_hub
    truck.distance_traveled = round(truck.distance_traveled, 0)
    truck.current_address = '4001 South 700 East'
    truck.current_time += timedelta(hours=distance_to_hub / truck.speed)
    truck.time_distance_list.append([truck.current_time, truck.distance_traveled])


# Loads the package_hash_table created on line 25 with package objects
load_package_data(package_hash_table, package_data)

# Delivers packages using the method defined on line 96-121
deliver_packages(truck1, package_hash_table, distance_data)
deliver_packages(truck2, package_hash_table, distance_data)
# Truck 3 departs at 10:20 am, it will be driven by the truck 1 driver after he arrives back at the hub. It contains
# package 9 which had the wrong address initially listed and was not updated until 10:20 am. Thus, the truck cannot
# leave until that package address is updated.
deliver_packages(truck3, package_hash_table, distance_data)

total_mileage = truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled

# Creates variables to hold the truck inventory, so they can be more easily referenced later
truck1_inv = [15, 19, 14, 13, 16, 20, 17, 1, 29, 30, 31, 34, 37, 40, 24, 26]
truck2_inv = [3, 6, 18, 25, 28, 32, 36, 38, 2, 4, 5, 7, 8, 21, 22, 23]
truck3_inv = [9, 10, 11, 12, 27, 33, 35, 39]


# User command line interface
# Overall time complexity is O(n^3) due to the while-loop containing nested for-loops. Although there are multiple
# for-loops nested within the while-loop, all their complexities will not multiply duo to their organization.
# Therefore, the simplified time complexity is O(n^3).
class Main:
    # While loop used so that the program will continue to ask for input until the user decides to exit the program.
    while True:
        # This try-except block encompasses the interface code and will close the program if user input causes a
        # Value Error
        try:
            # Gets input from user
            user_time = input("Please enter a time (24-hour clock) at which to check package information (Ex. 22:00) - "
                              "type 'exit' to close program: ")
            # Checks if the user entered 'Exit'. If so, the program is terminated
            if user_time.lower() == 'exit':
                print("Goodbye!")
                exit()

            user_input = input("If you would like to view a single package, please enter the package ID number. Type "
                               "'All' to view all packages - type 'exit to close program: ")
            # Checks if the user entered 'Exit'. If so, the program is terminated
            if user_input.lower() == 'exit':
                print("Goodbye!")
                exit()

            # Converts user_time into a timedelta object
            user_time = Functions.time_converter(user_time)

            # Initializes variables needed to calculate the truck mileage at specific times
            truck1_distance = 0.0
            truck2_distance = 0.0
            truck3_distance = 0.0

            # Determines the distance traveled by truck 1 at the user input time. Loops through the truck
            # time_distance_list, which tracks the distance a truck has traveled at certain time points throughout its
            # journey. Sets the value of truck1_distance to the current distance traveled by that truck. The last value
            # assigned to truck1_distance is the distance traveled at the user input time.
            # Each of these loops is O(n), they are not nested, so they do not multiply.
            for item in truck1.time_distance_list:
                if user_time > item[0]:
                    truck1_distance = item[1]
            # Same as above, but for truck 2
            for item in truck2.time_distance_list:
                if user_time > item[0]:
                    truck2_distance = item[1]
            # Same as above, but for truck 3
            for item in truck3.time_distance_list:
                if user_time > item[0]:
                    truck3_distance = item[1]

            # If statement to check if the user requested all packages or a single package
            if user_input.lower() == 'all':
                print(f"\nTruck 1 - Total Mileage: {round(truck1_distance, 0)}")
                # O(n) time complexity
                for i in truck1_inv:
                    package = package_hash_table.lookup(i)
                    package.package_status(user_time)

                    # This if statement checks if the package has been delivered at the user input time. If it yet to
                    # be delivered, it prints the output with "Upcoming Delivery Time" to indicate the time at which
                    # the package will be delivered.
                    if package.delivery_time > user_time:
                        # Print package info
                        print(
                            f"ID: {package.id} | Delivery Address: {package.address} | Deadline: {package.deadline} | "
                            f"Departure Time: {package.depart_time} | Upcoming Delivery Time: {package.delivery_time} |"
                            f" Package Status: {package.status} | Special Notes: {package.special_notes}")
                    # If the package has been delivered then the output shows "Delivery Time".
                    else:
                        print(
                            f"ID: {package.id} | Delivery Address: {package.address} | Deadline: {package.deadline} | "
                            f"Departure Time: {package.depart_time} | Delivery Time: {package.delivery_time} | Package "
                            f"Status: {package.status} | Special Notes: {package.special_notes}")

                print(f"\nTruck 2 - Total Mileage: {round(truck2_distance, 0)}")
                # O(n) time complexity
                for i in truck2_inv:
                    package = package_hash_table.lookup(i)
                    package.package_status(user_time)

                    # This if statement checks if the package has been delivered at the user input time. If it yet to
                    # be delivered, it prints the output with "Upcoming Delivery Time" to indicate the time at which
                    # the package will be delivered.
                    if package.delivery_time > user_time:
                        # Print package info
                        print(
                            f"ID: {package.id} | Delivery Address: {package.address} | Deadline: {package.deadline} | "
                            f"Departure Time: {package.depart_time} | Upcoming Delivery Time: {package.delivery_time} |"
                            f" Package Status: {package.status} | Special Notes: {package.special_notes}")
                    # If the package has been delivered then the output shows "Delivery Time".
                    else:
                        print(
                            f"ID: {package.id} | Delivery Address: {package.address} | Deadline: {package.deadline} | "
                            f"Departure Time: {package.depart_time} | Delivery Time: {package.delivery_time} | Package "
                            f"Status: {package.status} | Special Notes: {package.special_notes}")

                print(f"\nTruck 3 - Total Mileage: {round(truck3_distance, 0)}")
                # O(n) time complexity
                for i in truck3_inv:
                    package = package_hash_table.lookup(i)
                    package.package_status(user_time)
                    p_address = package.address
                    p_zip = package.zip

                    # If user_time is before 10:20 am then set the address and zip code to the address and zip before
                    # it was updated at 10:20 am
                    # This logic is only needed for Truck 3 because package 9 will always be on Truck 3 because it
                    # departs after the package address is updated.
                    if user_time < timedelta(hours=10, minutes=20) and package.id == 9:
                        p_address = '300 State St'
                        p_zip = '84103'

                    # This if statement checks if the package has been delivered at the user input time. If it yet to
                    # be delivered, it prints the output with "Upcoming Delivery Time" to indicate the time at which
                    # the package will be delivered.
                    if package.delivery_time > user_time:
                        # Print package info
                        print(
                            f"ID: {package.id} | Delivery Address: {p_address} | Deadline: {package.deadline} | "
                            f"Departure Time: {package.depart_time} | Upcoming Delivery Time: {package.delivery_time} |"
                            f" Package Status: {package.status} | Special Notes: {package.special_notes}")
                    # If the package has been delivered then the output shows "Delivery Time".
                    else:
                        print(
                            f"ID: {package.id} | Delivery Address: {p_address} | Deadline: {package.deadline} | "
                            f"Departure Time: {package.depart_time} | Delivery Time: {package.delivery_time} | Package "
                            f"Status: {package.status} | Special Notes: {package.special_notes}")

                print(f"\nTotal Mileage (all trucks): {round(truck1_distance + truck2_distance + truck3_distance, 0)}")

            elif 1 <= int(user_input) <= 40:
                on_truck = None
                # Complexity of O(n) because truck_inv is iterated over, not nested loops, so the complexities don't
                # multiply
                if int(user_input) in truck1_inv:
                    on_truck = 1
                elif int(user_input) in truck2_inv:
                    on_truck = 2
                elif int(user_input) in truck3_inv:
                    on_truck = 3

                print(f"Truck {on_truck}")
                # O(n) time complexity
                package = package_hash_table.lookup(int(user_input))
                package.package_status(user_time)
                p_address = package.address
                p_zip = package.zip

                # If user_time is before 10:20 am then set the address and zip code to the address and zip before it was
                # updated at 10:20 am
                if user_time < timedelta(hours=10, minutes=20) and package.id == 9:
                    p_address = '300 State St'
                    p_zip = '84103'

                    # This if statement checks if the package has been delivered at the user input time. If it yet to
                    # be delivered, it prints the output with "Upcoming Delivery Time" to indicate the time at which
                    # the package will be delivered.
                if package.delivery_time > user_time:
                    # Print package info
                    print(
                        f"ID: {package.id} | Delivery Address: {p_address} | Deadline: {package.deadline} | "
                        f"Departure Time: {package.depart_time} | Upcoming Delivery Time: {package.delivery_time} | "
                        f"Package Status: {package.status} | Special Notes: {package.special_notes}")
                # If the package has been delivered then the output shows "Delivery Time".
                else:
                    print(
                        f"ID: {package.id} | Delivery Address: {p_address} | Deadline: {package.deadline} | "
                        f"Departure Time: {package.depart_time} | Delivery Time: {package.delivery_time} | Package "
                        f"Status: {package.status} | Special Notes: {package.special_notes}")
            else:
                print("Invalid input. Closing Program.")
                exit()
        except ValueError:
            print("Invalid input. Closing Program.")
            exit()
