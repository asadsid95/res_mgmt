class Resident:
    def __init__(self, name:str, email:str, lease_start_date, lease_end_date = None):
        self.name = name
        self.email = email
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date 
        self.parcels = []

    def __repr__(self):
        return f'{__class__.__name__}({self.name}, {self.email}, {self.lease_start_date}, {self.lease_end_date})'

    def has_parcel(self):


        pass