#Task 1
class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
        
        def update_owner(self, new_owner):
            self.owner = new_owner
            print(f"Vehicle: {self.type}, Owner: {self.owner}, Registration Number: {self.registration_number}")

vehicle1 = Vehicle("r123", "truck", "John")
vehicle2 = Vehicle("r456", "sedan", "Jane")

vehicle1.update_owner("Larry")
vehicle2.update_owner("Sam")

