from parcel import Parcel

class Resident:
    def __init__(self, name:str, email:str, lease_start_date, is_active=True, lease_end_date = None):
        self.name = name
        self.email = email
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date 
        self.is_active = is_active
        self.parcels = []

    def __repr__(self):
        return f'{__class__.__name__}({self.name}, {self.email}, {self.lease_start_date}, {self.lease_end_date})'

    def parcel_received(self, courier, weight):
        parcel = Parcel(courier, weight)
        self.parcels.append(parcel)
    
    def parcel_picked_up(self):

        if len(self.parcels) == 0:
            return f'There are no parcels for {self.name}'
        elif len(self.parcels) >= 1:
            for parcel in self.parcels:
                parcel.picked_up()
                self.parcels.pop(0)

    def reminder_parcel_pickup(self):
        pass

res1 = Resident('random person', 'a@a.com', 0)
# res1.parcel_received('FedEx', 7.4)
# res1.parcel_received('FedEx', 7777.4)
# print(res1.parcels)
print(res1.parcel_picked_up())