class Item:
    def __init__(self, name_of_item , description):
        self.name_of_item = name_of_item
        self.description = description

    def __str__(self):
        return f"{self.name_of_item}"

