from resident import Resident

class Unit:
    def __init__(self, number: int, resident = None, occupied=False):
        self.unit_number=number
        self.resident = resident
        self.occupied=occupied
    
    def __repr__(self):
        return f"{__class__.__name__}({self.unit_number}, {self.resident.name}, {self.occupied})"

    def add_resident(self, name, email, lease_start_date, lease_end_date):
        assert self.occupied == False, 'Unit is already occupied'
        
        self.resident = Resident(name, email, lease_start_date, lease_end_date)
        self.occupied = True
        # print(self.resident.name)

    def remove_resident(self, name):
        assert self.occupied == True, 'Unit is vacant'
        
        print(f"resident {self.resident.name} is being removed")
        
        self.resident = None
        self.occupied = False


unit1 = Unit(100)
unit1.add_resident('Bob Vance', 'b.v@a.com', 0, 2)
print(unit1)
unit1.remove_resident('Bob Vance')

# unit1.add_resident('some joe', 'b.v@a.com', 0, 3)