class Item:
    def __init__(self,nameOfItem ,description):
        self.nameOfItem = nameOfItem
        self.description = description

    def __str__(self):
        return (f"{self.nameOfItem} : {self.description}")

    def __repr__(self):
        return (f"{self.nameOfItem} : {self.description}")