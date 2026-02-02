class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount,description=""):
        self.ledger.append({"amount": amount,"description": description})

    def withdraw(self, amount,description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()\

    def transfer(self, amount, person):
        if self.check_funds(amount):
            self.withdraw(amount,f"Transfer to {person.name}")
            person.deposit(amount,f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    # Title
    chart = "Percentage spent by category\n"

    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    percentages = [(int((amount / total_spent) * 100) // 10) * 10 for amount in spent]

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(105.55, "groceries")
food.withdraw(15.89, "restaurant")

entertainment = Category("Entertainment")
entertainment.deposit(1000, "initial deposit")
entertainment.withdraw(33.40, "movies")

business = Category("Business")
business.deposit(1000, "initial deposit")
business.withdraw(10.99, "tax")

print(create_spend_chart([food, entertainment, business]))

