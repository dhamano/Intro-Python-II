# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc="", items=[]):
        self.name = name
        self.desc = desc
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{self.name} {self.n_to} {self.s_to} {self.w_to} {self.e_to}"
    
    def __repr__(self):
        return f"Person({repr(self.name)})"
    
    def add_item(self, item):
        self.items.append(item)
    
    def rem_item(self, item):
        self.items.remove(item);
