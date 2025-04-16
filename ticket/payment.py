import re

class Payment_method:
    def __init__(self, amount):
        self.amount = amount

    def process(self):
        print(f"Kwota do zapłaty - {self.amount} zł")
        method = input("Wybierz metodę płatności: \nb - BLIK\nk - karta\ng - gotówka\n")

        if method == "b":
            self._blik()
        elif method == "k":
            self._card()
        elif method == "g":
            self._cash()
        else:
            retry = input("Niepoprawna opcja. Spróbować ponownie (t/n)? ")
            if retry.lower() == "t":
                self.process()
            else:
                exit()

    def _blik(self):
        code = input("Podaj kod BLIK: ")
        if re.fullmatch(r"\d{6}", code):
            print("Transakcja się powiodła.")
        else:
            retry = input("Niepoprawny kod. Spróbować ponownie (t/n)? ")
            if retry.lower() == "t":
                self._blik()
            else:
                exit()

    def _card(self):
        print("Proszę zbliżyć kartę...")
        input("Potwierdź transakcję: ")
        print("Transakcja się powiodła.")

    def _cash(self):
        paid = 0
        while paid < self.amount:
            try:
                paid += float(input("Wprowadź gotówkę: "))
            except ValueError:
                print("Niepoprawna kwota.")
                continue

            if paid < self.amount:
                retry = input("Za mało gotówki. Dopłacić? (t/n) ")
                if retry.lower() != "t":
                    exit()

        if paid > self.amount:
            print(f"Reszta: {round(paid - self.amount, 2)} zł")
        print("Transakcja się powiodła.")
