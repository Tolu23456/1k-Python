class Phone:
    def __init__(self, brand):
        self.brand = brand

    def call(self):
        print(self.brand, "is making a call")

p1 = Phone("iPhone")
p2 = Phone("Samsung")

p1.call()
p2.call()