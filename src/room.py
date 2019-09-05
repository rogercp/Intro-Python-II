# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items_stored=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items_stored = items_stored

    def __str__(self):
        return f'------- At "{self.name}" , "{self.description}"'

    def current_items(self):
        if len(self.items_stored) < 1:
            return f'----- room:[empty]'
        else:
            return ', '.join(str(i) for i in self.items_stored)

    def placed_item(self, item):
        self.items_stored.append(item)

    def remove_item(self, item):
        print(self.current_items())
        self.items_stored.remove(item)
