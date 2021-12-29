from resident import Resident

class Unit:
    def __init__(self, number: int, occupied=False):
        self.number=number
        self.occupied=occupied
    
    def __repr__(self):
        return f"{__class__.__name__}({self.number}, {self.occupied})"


    def add_resident(self, name, email, lease_start_date):
        Resident(name, email, lease_start_date)
        self.occupied = True
    pass

# unit1 = Unit(1)
# print(unit1)
# unit1.add_resident('Bob Vance', 'b.v@a.com', 0)
# print(unit1)