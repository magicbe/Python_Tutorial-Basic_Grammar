class Dog:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    def run(self):
        print("Dog", self.name, "[", self.age, "] Run")

dog1 = Dog("Black", 10)
dog1.run()

dog2 = Dog("White", 5)
dog2.run()