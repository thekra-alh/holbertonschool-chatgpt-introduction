class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def get_amount(prompt):
    """
    Repeatedly prompts the user until a valid numeric amount is entered.

    Parameters:
        prompt (str): The message shown to the user when asking for input.

    Returns:
        float: A valid numeric amount entered by the user.
    """
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        action = action.lower()

        if action == 'exit':
            break

        elif action == 'deposit':
            amount = get_amount("Enter the amount to deposit: $")
            cb.deposit(amount)

        elif action == 'withdraw':
            amount = get_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
