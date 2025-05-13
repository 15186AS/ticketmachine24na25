import ticket

class Cart:
    def __init__(self):
        self.tickets:list[ticket.Ticket] = []
        self.value = 0.0
    def add_ticket(self, item:ticket.Ticket):
        self.tickets.append(item)
        self.value += item.get_price()
    def get_value(self):
        return self.value
    def display(self) -> None:
        print("Zawartość koszyka:")
        for index, ticket in enumerate(self.tickets):
            print(f"{index+1}. {ticket}: \t {ticket.get_price()} zł")
        print(f"Wartość koszyka: \t {self.value} zł")
    def recalculate_value(self):
        self.value = sum(item.get_price() for item in self.tickets)
        return self.value
