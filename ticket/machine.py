import json
import re

class TicketMachine:
    def __init__(self):
        with open("prices.json", "r", encoding="UTF-8") as jf:
            self.prices = json.load(jf)
        self.cart = []

    def display_menu(self, menu=None):
        if menu is None:
            menu = self.prices

        print("Jaką opcję biletu chcesz kupić? ")
        options = list(menu.keys())
        for index, option in enumerate(options):
            print(f"{index} - {option}")

        try:
            choice = int(input("Wybór: "))
        except ValueError:
            print("Wprowadzono niepoprawny typ wartości.")
            return self.display_menu(menu)

        if choice > len(options) - 1 or choice < 0:
            print("Wprowadzono błędny numer opcji.")
            return self.display_menu(menu)

        option = options[choice]
        submenu = menu[option]

        if isinstance(submenu, dict):
            return self.display_menu(submenu)
        else:
            return (option, submenu)

    def register_payment(self):
        total = sum(price for _, price in self.cart)
        print(f"Kwota do zapłaty: {total} zł")

        payment_method = input("Wybierz metodę płatności: \nb - BLIK \nk - karta\ng - gotówka\n")

        if payment_method.lower() == 'b':
            blik = input("Podaj kod BLIK: ")
            if re.search(r"^[0-9]{6}$", blik):
                print("Transakcja się powiodła")
            else:
                decision = input("Podano niepoprawny kod. Czy chcesz spróbować jeszcze raz (t/n)? ")
                if decision.lower() == 't':
                    self.register_payment()
                else:
                    exit()

        elif payment_method.lower() == 'k':
            print("Proszę zbliżyć kartę do czytnika...")
            input("Potwierdź transakcję: ")
            print("Transakcja się powiodła")

        elif payment_method.lower() == 'g':
            paid = 0
            while paid < total:
                try:
                    paid += float(input("Wprowadź gotówkę: "))
                except ValueError:
                    paid += 0

                if paid < total:
                    decision = input("Wprowadzono za mało gotówki. Czy chcesz dopłacić (t/n)? ")
                    if decision.lower() != 't':
                        exit()
        else:
            decision = input("Wybrano niepoprawną opcję. Czy chcesz spróbować jeszcze raz (t/n)? ")
            if decision.lower() == 't':
                self.register_payment()
            else:
                exit()

    def display_cart(self):
        for ticket, price in self.cart:
            print(f"Bilet: {ticket}\tCena: {price} zł")

    def run(self):
        add_another = "t"
        while add_another.lower() == 't':
            self.cart.append(self.display_menu())
            add_another = input("Czy chcesz dodać kolejny bilet (t/n)? ")

        self.register_payment()
        input("Drukowanie biletów. Proszę czekać...")
        self.display_cart()
        print("Dziękujemy za skorzystanie z automatu biletowego. Zapraszamy ponownie.")

# Uruchomienie programu
if __name__ == "__main__":
    machine = TicketMachine()
    machine.run()