class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Item(repr{self.name}, repr{self.desc})"