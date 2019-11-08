id = 0
class Item:
    def __init__(self, name, desc):
        global id
        self.name = name
        self.desc = desc
        self.id = id
        id += 1
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Item({repr(self.name)}, {repr(self.desc)}, {repr(self.id)})"