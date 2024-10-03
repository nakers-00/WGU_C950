# from datetime import timedelta
import Functions
# from Hashtable import HashTable
from Package import Package

package_data = Functions.read_package_csv('package.csv')
address_data = Functions.read_address_csv('addresses.csv')
distance_data = Functions.read_distance_csv('distances.csv')


# package_hash_table = HashTable()

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
    address1_index = find_address_index(address1, address_data)
    address2_index = find_address_index(address2, address_data)

    # The indices from address_data correspond to the indices in distance_data, so simply plug in those indices to
    # find the distance between the two addresses
    distance = distance_info[address1_index][address2_index]
    return distance


# This method takes in an address and compares it with the delivery address of each package in the truck inventory.
# It then returns the address of the package with the nearest delivery address to the current address (from_address)
# truck_inventory will be truck.inventory, so it will be a list of package IDs which correspond to package objects
# stored in the hash table
def min_distance_from(from_address, truck_inventory, hash_table):
    # min_distance set to 1000.0 to ensure that the first address compared will always be closer
    min_distance = 1000.0
    nearest_package_address = None

    # Loop through the truck inventory and find the distance between each package address and the from_address.
    # Compare that distance with the current min_distance to find the nearest neighbor.
    # Return the delivery address of that nearest neighbor package
    # O(n) time complexity due to for loop
    for package_id in truck_inventory:
        # Finds the package object stored in the hash table corresponding to package ID in the truck inventory
        package = hash_table.lookup(package_id)
        # Updates min_distance if a package is found to have a closer delivery address to from_address
        if distance_between(from_address, package.address, distance_data) < min_distance:
            nearest_package_address = package.address
            min_distance = distance_between(from_address, package.address, distance_data)

    return nearest_package_address

# NOTE: When updating package departure and delivery times, remember to store them with timedelta*

# Load the trucks manually by creating truck objects and adding the packages that need to be in each truck


# * This is a check for if the distance array is correct*
# for i in range(len(distance_data) - 1):
#     for j in range(len(distance_data) - 1):
#         if distance_data[i][j] == distance_data[j][i]:
#             print('good')
#             continue
#         else:
#             print('bad')
#             break
