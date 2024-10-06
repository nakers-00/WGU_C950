# Create a truck class with the required attributes

class Truck:
    def __init__(self, max_packages, speed, inventory, distance_travelled,
                 current_address, departure_time):
        self.max_packages = max_packages
        self.speed = speed
        self.starting_inventory = inventory
        self.not_delivered = inventory
        self.distance_travelled = distance_travelled
        self.current_address = current_address
        self.departure_time = departure_time
        self.current_time = departure_time
        self.time_distance_list = []

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.max_packages, self.speed, self.starting_inventory, self.not_delivered,
            self.distance_travelled, self.current_address,
            self.departure_time)
