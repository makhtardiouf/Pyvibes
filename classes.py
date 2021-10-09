'''
Demo for Classes, simulating pseudo stock market operations

'''
# import math
import random
import datetime

class Stock:
    availDate = datetime.date.today()

    # Conctructor of the object
    def __init__(self):
        self.type = "BTC"
        self.shares = []

    def add(self, x):
        self.shares.append(x)

    def size(self):
        return len(self.shares)

    def show(self):
        if self.size() <= 0:
            print(f"\nYou did not purchase any {self.type} tokens")
            return

        width = 20
        print(str('-'*width).center(10), str('\t' + '-'*width).center(20))

        for i, s in enumerate(self.shares):
            print("{0:10}".format("\tItem " + str(i)), " | \t{0:20}".format(str(s)))
        #    i += 1
        print(f"\nAvailable since: {self.availDate}\n")

    def __str__(self) -> str:
        return f"Blockchain Stock: {self.size} {self.type} tokens"


class DefiStock(Stock):
    def __init__(self):
        print("OOP magic inherited class from Stock")
        Stock.__init__(self)
        self.type = "ETH"

    def listStock(self):
        Stock.show(self)

    def __str__(self) -> str:
        return f"Blockchain Stock: {self.size} {self.type} tokens"


print("Creating your stock")
btcTokens = Stock()
i = random.randint(3, 15)

while i > 0:
    btcTokens.add(random.randint(1, 200))
    i -= 1

print(f"{btcTokens.size()} {btcTokens.type} tokens minted to your portfolio:")
btcTokens.show()

ethTokens = DefiStock()
print( btcTokens.shares.reverse())
ethTokens.listStock()

print(isinstance(btcTokens, Stock))
print(isinstance(ethTokens, Stock))
