class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self, speed):
        self.speed += speed

    def decelerate(self, speed):
        self.speed -= speed

    def start(self):
        self.speed = 0

    def stop(self):
        self.speed = 0
