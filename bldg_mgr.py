from unit import Unit

class Building:
    address='123 address st'
    management='Mgmt Co.'
    max_capacity_resident = 3
    
    def __init__(self,unit = {}):
        self.units = unit
        self.units_counter = 1

    def add_unit(self,number):

        current_occupied_units =list(self.units.keys())
        
        assert number not in current_occupied_units, f'Unit {number} is already occupied'
        assert len(current_occupied_units) < Building.max_capacity_resident, f"Building capacity is {Building.max_capacity_resident}, {self} being the {self.units_counter}th exceed this"

        new = Unit(number)
        self.units[new.number] = self.units_counter
        self.units_counter += 1

    def remove_unit(self,number):
        current_occupied_units =list(self.units.keys())
        assert number in current_occupied_units, f'Unit {number} is not occupied'
        
        del self.units[number]

# buildingA = Building()

# buildingA.add_unit(100)
# buildingA.add_unit(200)
# buildingA.add_unit(300)
# print(buildingA.units)

# buildingA.remove_unit(100)
# buildingA.remove_unit(200)
# print(buildingA.units)

    