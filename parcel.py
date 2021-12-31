from datetime import datetime

class Parcel:
    def __init__(self, courier: str, weight:float, check_in_time = datetime.now(), hasBeenPickedUp = False):
        self.courier = courier
        self.check_in_time = check_in_time
        self.check_out_time = None
        self.weight = weight
        self.hasBeenPickedUp = hasBeenPickedUp

    def __repr__(self):
        return f'{__class__.__name__}({self.courier}, {self.check_in_time}, {self.check_out_time}, {self.weight}, {self.hasBeenPickedUp})'

    def picked_up(self):
        self.hasBeenPickedUp = True
        self.check_out_time = datetime.now()
        pass

# parcel1 = Parcel('fedex', 7.4, 2)
# print(parcel1.hasBeenPickedUp)
# parcel1.picked_up()
# print(parcel1.hasBeenPickedUp)
# print(parcel1.check_out_time)