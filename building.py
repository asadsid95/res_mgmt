from DBcm import UseDatabase

class Resident:
    '''
    When initialized, the object will represent a resident living in a suite.
    '''
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        pass

class Suite:
    '''
    When initialized, the object will represent a suite in the building.
    '''
    all_suites = []
    def __init__(self, suite_number, is_vacant = True):
        self.suite_number = suite_number
        self.is_vacant = is_vacant
        self.suite_history = {}
        self.suite_counter = 0

        Suite.all_suites.append(self)
 
    def __repr__(self):
        return f'{__class__.__name__}({self.suite_number})'

    def moving_in(self,resident_name,email):
        '''
        Upon moving in of a Resident, this should add resident's details as history to maintain record of current and past residents.
        It will also change unit's vacancy to False
        '''
        #check if unit is vacant
        assert self.is_vacant == True, f'Suite {self.suite_number} is not vacant!'

        self.is_vacant = False
        # self.res = Resident(resident_name, email)
        self.res = resident_name

        self.suite_history[self.suite_number, self.res, self.is_vacant] = self.suite_counter
        self.suite_counter += 1

        print(self.suite_history)
        # print(Unit.all_units)

    def moving_out(self, resident_name):
        '''
        Upon moving out, vacancy should be set to free for unit & this should also reflect in the suite_history
        '''
        listt = list(self.suite_history.keys())
        for resident in listt:
            print(resident)
            print(type(resident))
            if resident_name in resident[1]:
                
                
                print('correct name')
            else: 
                print('incorrect name')
        pass


# unnit=Suite(100)
# unnit.moving_in('xyz','a@s.ad')
# unnit.moving_out('xyzz')
# # unnit1=Suite(101)
# # unnit1.moving_in('xy11z','a@s.ad')

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