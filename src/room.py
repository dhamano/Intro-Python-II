# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        self.items = items
        self.n_room = None
        self.s_room = None
        self.e_room = None
        self.w_room = None

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Person(repr{self.name}"
    
    def add_item(self, item):
        self.item.append(item)
    
    # def rem_item(self, item):
       
    
    def n_to(room):
        self.n_room = room
    
    def s_to(room):
        self.s_room = room
    
    def e_to(room):
        self.e_room = room
    
    def n_to(room):
        self.n_room = room
