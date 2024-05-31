#Class
    #attributes
    #methods


class Account:
    def __init__(self, owner, amount=0):
        self.__owner = owner
        self.__amount = amount

    def deposit(self, amount):
        if amount > 0:
            self.__amount += amount
            print("Added", amount, "to the account")

    def get_balnce(self):
        return self.__amount


acc = Account("Boat")
acc.deposit(100)
print(acc.get_balnce())




