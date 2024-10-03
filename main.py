# from datetime import timedelta
import Functions

# from Package import Package

address_data = Functions.read_address_csv('addresses.csv')
distance_data = Functions.read_distance_csv('distances.csv')


# This method returns the index of an address in the address_data array
def find_address_index(address):
    for item in address_data:
        if item[2] == address:
            return item[0]


# The following methods will be the actual implementation of the nearest neighbor algorithm
def distance_between(address1, address2):
    # Get the index of each address in the address_data array
    address1_index = find_address_index(address1)
    address2_index = find_address_index(address2)

    # The indices from address_data correspond to the indices in distance_data, so simply plug in those indices to
    # find the distance between the two addresses
    distance = distance_data[address1_index][address2_index]
    return distance


# This method takes in an address and compares it with the delivery address of each package in the truck inventory.
# It then returns the address of the package with the nearest delivery address to the current address
# truck_inventory will be truck.inventory, so it will be a list of package objects

# NOTE: May have to rethink how I access the package objects to make use of the hash table, maybe just store the
# packageID in the truck inventory and then use that to access the package object stored in the hash table
def min_distance_from(from_address, truck_inventory):
    min_distance = 200.0
    nearest_package_address = None

    # Loop through the truck inventory and find the distance between each package address and the from_address.
    # Compare that distance with the current min_distance to find the nearest neighbor.
    # Return the delivery address of that nearest neighbor package
    # O(n) time complexity due to for loop
    for package in truck_inventory:
        if distance_between(from_address, package.address) < min_distance:
            nearest_package_address = package.address
            min_distance = distance_between(from_address, package.address)

    return nearest_package_address

# Load the trucks manually by creating truck objects and adding the packages that need to be in each truck


# Work in progress on instantiating package objects from the CSV data (dont run yet cause it may make alot of objects*)
# for package in package_data:
#     pID = package[0]
#     pAddress = package[1]
#     pDeadline = package[2]
#     pCity = package[3]
#     pZip = package[4]
#     pWeight = package[5]
#     pStatus = package[6]
#     pSpecial = package[7]
#
#     test_package = Package(pID, pAddress, pDeadline, pCity, pZip, pWeight, pStatus, pSpecial)


# * This is a check for if the distance array is correct*
# for i in range(len(distance_data) - 1):
#     for j in range(len(distance_data) - 1):
#         if distance_data[i][j] == distance_data[j][i]:
#             print('good')
#             continue
#         else:
#             print('bad')
#             break
