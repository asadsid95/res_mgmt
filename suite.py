from resident import Resident
from DBcm import UseDatabase

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

        # with UseDatabase() as self.cursor:
        #     create_suites_table = '''CREATE TABLE IF NOT EXISTS suites(
        #         suite_id INTEGER PRIMARY KEY,
        #         building_id INTEGER,
        #         suite_number INTEGER,
        #         is_vacant INTEGER,
        #         FOREIGN KEY(building_id) REFERENCES buildings(building_id)
        #         ) '''

        #     insert_suites_table = f'''INSERT INTO suites(
        #         suite_number, is_vacant) VALUES (
        #             {self.suite_number}, {self.is_vacant}
        #         )'''

        #     self.cursor.execute(create_suites_table)
        #     self.cursor.execute(insert_suites_table)

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


# Suite(100)
# unnit.moving_in('xyz','a@s.ad')
# unnit.moving_out('xyzz')
# # unnit1=Suite(101)
# # unnit1.moving_in('xy11z','a@s.ad')
