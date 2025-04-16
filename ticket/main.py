from machine import TicketMachine
if __name__ == "__main__":
    ticket_machine = TicketMachine("prices.json")
    ticket_machine.run()