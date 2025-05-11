class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, Price):
        self.__maxprice = Price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell

# using setter fuction
c.setMaxPrice(1000)
c.sell()