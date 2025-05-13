import re

class Payment_method:
    def __init__(self, amount:float):
        self.amount = amount
    def process_payment(self):
        print(f"Kwota do zapłaty: {self.amount} zł")
        method = input("Wybierz metodę płatności: \nb - BLIK\nk - karta\ng - gotówka\nWybór: ")
        if method.lower()=='b': self._blik()
        elif method.lower()=='k': self._card()
        elif method.lower()=='g': self._cash()
        else: 
            decision = input("Wybrano niepoprawną opcję. Czy chcesz spróbować jeszcze raz (t/n)? ")
            if decision.lower()=='t':
                self.process_payment()
            else: exit()
    def _blik(self):
        blik = input("Podaj kod BLIK: ")
        if re.search(r"^[0-9]{6}$", blik):
            print("Transakcja się powiodła")
        else: 
            decision = input("Podano niepoprawny kod. Czy chcesz spróbować dokonać płatności jeszcze raz (t/n)? ")
            if decision.lower()=='t':
                self.process_payment()
            else: exit()
    def _card(self):
        print("Proszę zbliżyć kartę do czytnika...")
        input("Potwierdź transakcję: ")
        print("Transakcja się powiodła")
    def _cash(self):
        paid = 0
        while paid < self.amount:
            try:
                paid += float(input("Wprowadź gotówkę: "))
            except ValueError:
                paid += 0
            if paid < self.amount:
                decision = input("Wprowadzono za mało gotówki. Czy chcesz dopłacić (t/n)?")
                if decision.lower()=='t':
                    continue
                else: exit()
        if paid > self.amount:
            print(f"Reszta: {paid-self.amount} zł")