from parcel import Parcel
from DBcm import UseDatabase

class Resident:
    '''
    When initialized, the object will represent a resident living in a suite.
    '''
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        pass