# IN MAIN, MAKE A PACKAGE OBJECT WITH THE DETAILS AND THEN PASS THAT OBJECT AS THE value VARIABLE IN THIS CLASS

# This file is the hash table that will be used to store package info. It has a resize method that
# triggers when the max chain length is met.
# Citations: C950 - Webinar-1 - Let’s Go Hashing - Recording, Lysecky, R., & Vahid, F. (2018, June). C950:
# Data Structures and Algorithms II. zyBooks.

# Create hash table class with chaining This hash table takes in package ID as the key and package objects as the
# value. Therefore, it holds all necessary data components in the package object and each are easily and efficiently
# accessible.
class HashTable:
    # Constructor with initial length of the table to 40 if not specified
    def __init__(self, initial_cap=40):
        # Hash table is initialized with empty buckets, each bucket is a list
        self.cap = initial_cap
        self.table = []
        # O(n) time complexity due to the for loop
        for i in range(self.cap):
            self.table.append([])

        # Max allowed chain length, table will be resized if this chain length is reached
        self.max_chain_length = 5

    # Insert package details (value) into table based on the package ID (key)
    # O(n) time complexity due to the for loop
    def insert(self, key, value):
        # Determine the bucket that the package ID will be hashed into
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # If the package ID is already in the bucket list, update the package details
        for kv in bucket_list:
            if kv == key:
                kv[1] = value
                return True

        # If the package ID is not in the bucket list, append the package details to the bucket list
        key_value = [key, value]
        bucket_list.append(key_value)

        # Resize the hash table if the max chain length is reached
        if len(bucket_list) == self.max_chain_length:
            self._resize(self.cap * 2)

        return True

    # Search for value given a key
    # O(n) time complexity due to the for loop
    def lookup(self, key):
        # Find the bucket that the key would be in
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search the bucket_list for the package ID, return the details associated with the ID
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]

        # If key is not in the bucket list, return None
        return None

    # Remove a kv pair given a key
    # O(n) time complexity due to the for loop
    # This is not used in the current program but is added because it is needed for a proper hash table
    def remove(self, key):
        # Find the bucket that the key is in
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove the kv pair from the bucket if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Creates resize function that allows for self-adjusting nature of the hash table
    # O(n^2) time complexity due to the nested for loop
    def _resize(self, new_cap):
        original_table = self.table
        self.cap = new_cap
        self.max_chain_length = 5
        # Reset the table with the new capacity
        self.table = [[] for i in range(self.cap)]

        # Insert the data from the original table into the new, resized table
        for bucket in original_table:
            for k, v in bucket:
                self.insert(k, v)

