class Unit:
    def __init__(self, suite_number, is_vacant = True):
        self.suite_number = suite_number
        self.is_vacant = is_vacant
        self.unit_history = {}
        self.unit_history = 0

    def __repr__(self):
        return f'{__class__.__name__}({self.suite_number})'

    def moving_in(self,resident_name):
        new_res = resident_name
        self.unit_history[new_res] = self.unit_history
        self.unit_history += 1
        pass


class Building:
    '''
    When initialized, the object will represent a residential building consisting of suites.
    '''
    building_name = 'Some building'
    max_capacity_suites = 10

    def __init__(self):
        self.units = {}
        self.units_counter = 1
    
    def add_suites(self, number_of_suites):
        '''
        Upon receiving arg, it should create a dict of suites if arg is <= max_capacitity_suites
        '''
        assert number_of_suites <= Building.max_capacity_suites, f'Capacity is {Building.max_capacity_suites} but {number_of_suites} was provided.'

        for number in range(1,number_of_suites+1):
            self.units[Unit(number)] = self.units_counter
            self.units_counter += 1

        print(self.units)
        
Building().add_suites(10)