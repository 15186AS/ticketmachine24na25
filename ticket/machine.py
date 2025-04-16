from cart import Cart
from payment import Payment_method
from ticket import Ticket
import json

class TicketMachine:
    def __init__(self, prices_file):
        with open(prices_file, "r", encoding="UTF-8") as file:
            self.menu = json.load(file)
        self.cart = Cart()

    def run(self):
        print("Witamy w automacie biletowym.")
        self._add_tickets()
        total = self.cart.total_price()
        Payment_method(total).process()
        input("Drukowanie biletów. Proszę czekać...")
        self.cart.display()
        print("Dziękujemy za skorzystanie z automatu biletowego!")

    def _add_tickets(self):
        add_more = "t"
        while add_more.lower() == "t":
            name, price = self._choose_ticket(self.menu)
            self.cart.add_ticket(Ticket(name, price))
            add_more = input("Czy chcesz dodać kolejny bilet (t/n)? ")

    def _choose_ticket(self, menu):
        print("Jaką opcję biletu chcesz kupić?")
        options = list(menu.keys())
        for i, option in enumerate(options):
            print(f"{i} - {option}")
        try:
            choice = int(input("Wybór: "))
        except ValueError:
            print("Niepoprawna wartość.")
            return self._choose_ticket(menu)
        if choice < 0 or choice >= len(options):
            print("Niepoprawny numer.")
            return self._choose_ticket(menu)
        selected = menu[options[choice]]
        if isinstance(selected, dict):
            return self._choose_ticket(selected)
        return options[choice], selected
