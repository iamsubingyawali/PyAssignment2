class Customer:
    def __init__(self, name, address, contact, email, citizenship_no, balance):
        self.name = name
        self.address = address
        self.contact = contact
        self.email = email
        self.citizenship_no = citizenship_no
        self.balance = balance

    def credit(self, added_money):
        self.balance = float(self.balance) + float(added_money)

    def debit(self, withdrawn_money):
        self.balance = float(self.balance) - float(withdrawn_money)


my_ac = Customer('Subin', 'Kathmandu', '0', 'subin@gmail', '1234', 0)
print(my_ac.balance)
my_ac.credit(25000)
print(my_ac.balance)
my_ac.debit(10000)
print(my_ac.balance)
