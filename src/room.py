# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self,nameOfRoom ,description):
        self.nameOfRoom = nameOfRoom
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None



    def __str__(self):
        str = f"\n------------------------------"
        str += f"\n{self.nameOfRoom}"
        str += f"\n {self.description}"
        return str