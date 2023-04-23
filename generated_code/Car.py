class Car:
    # class to represent a car

    def __init__(self, make, model, year):
        # initialize attributes
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        # return a string with a description of the car
        return f"{self.year} {self.make} {self.model}"
