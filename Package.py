# Create a package class with the necessary attributes


class Package:
    def __init__(self, package_id, delivery_address, delivery_deadline, delivery_city, delivery_state,
                 delivery_zip_code, package_weight, delivery_status, special_notes):
        self.id = package_id
        self.address = delivery_address
        self.deadline = delivery_deadline
        self.city = delivery_city
        self.state = delivery_state
        self.zip = delivery_zip_code
        self.weight = package_weight
        self.status = delivery_status
        self.special_notes = special_notes
        self.depart_time = None
        self.delivery_time = None

    # Check the status of package at the specified time
    def package_status(self, time):
        if self.delivery_time < time:
            self.status = "Delivered"
        elif self.depart_time < time:
            self.status = "En Route"
        else:
            self.status = "At Hub"

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.deadline,
                                                           self.city, self.state, self.zip, self.weight,
                                                           self.status, self.special_notes, self.delivery_time)
