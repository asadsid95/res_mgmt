from suite import Suite
from DBcm import UseDatabase

class Building:
    '''
    When initialized, the object will represent a residential building consisting of suites.

    Table also gets created upon initialization
    '''
    building_name = 'Some building'
    max_capacity_suites = 10

    def __init__(self):
        self.units = {}
        self.units_counter = 1
        
        with UseDatabase() as self.cursor:
            create_building_table = '''CREATE TABLE IF NOT EXISTS buildings(
                building_id INTEGER PRIMARY KEY,
                total_suites INTEGER
            ) '''
            
            self.cursor.execute(create_building_table)

    def add_suites(self, number_of_suites):
        '''
        Upon receiving arg, it should create a dict of suites if arg is <= max_capacitity_suites
        '''
        assert number_of_suites <= Building.max_capacity_suites, f'Capacity is {Building.max_capacity_suites} but {number_of_suites} was provided.'

        for number in range(1,number_of_suites+1):
            self.units[Suite(number)] = self.units_counter
            self.units_counter += 1

        with UseDatabase() as self.cursor:
            insert_number_of_suites = f'''INSERT INTO buildings 
            (total_suites) VALUES ({number_of_suites}) 
            '''
            self.cursor.execute(insert_number_of_suites)

        print(self.units)

oBuilding1 = Building()
oBuilding1.add_suites(10)