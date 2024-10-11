# This file is the hash table that will be used to store package info.
# Citations: C950 - Webinar-1 - Let’s Go Hashing - Recording, Lysecky, R., & Vahid, F. (2018, June). C950:
# Data Structures and Algorithms II. zyBooks.
# Create hash table class with chaining. This hash table takes in package ID as the key and package objects as the
# value. Therefore, it holds all necessary data components in the package object and each are easily and efficiently
# accessible.
# This hash table has an average time complexity of O(1) and a worst-case of O(n). The space complexity is O(n).
class HashTable:
    # Constructor with initial length of the table to 40 if not specified
    def __init__(self, initial_cap=40):
        # Hash table is initialized with empty buckets, each bucket is a list
        self.cap = initial_cap
        self.table = []
        for i in range(self.cap):
            self.table.append([])

    # Insert package details (value) into table based on the package ID (key)
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
        return True

    # Search for value given a key
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
    # This is not used in the current program but is added because it is needed for a proper hash table
    def remove(self, key):
        # Find the bucket that the key is in
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Remove the kv pair from the bucket if it is present
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
