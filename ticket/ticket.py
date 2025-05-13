class Ticket:
    def __init__(self, category:str="", group:str="", name:str="", price:float=0):
        self.category = category
        self.group = group
        self.name = name
        self.price = price
    def __str__(self):
        return f"Bilet {self.category} {self.group} {self.name}"
    def get_price(self) -> float:
        return self.price
    def set_category(self, category:str):
        self.category = category
    def set_group(self, group:str):
        self.group = group
    def set_name(self, name:str):
        self.name = name