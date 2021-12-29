from unit import Unit

class Building:
    address='123 address st'
    management='Mgmt Co.'
    max_capacity_resident = 3
    
    def __init__(self):
        self.units = {}
        self.units_counter = 1

    def add_unit(self,number):
        assert number not in list(self.units.keys()), 'Unit is already occupied'
        
        if len(self.units) < Building.max_capacity_resident:
            new = Unit(number)
            self.units[new.number] = self.units_counter
            self.units_counter += 1
        else:
            return "Building is at capacity"

    def remove_unit(self,number):
        assert number in self.units, 'Unit not occupied'

        pass

buildingA = Building()
buildingA.add_unit(100)
print(buildingA.units_counter)
buildingA.add_unit(2)
print(buildingA.units_counter)
buildingA.add_unit(3)
print(buildingA.units_counter)

buildingA.add_unit(4)

    