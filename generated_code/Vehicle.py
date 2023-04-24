class Vehicle:
    def __init__(self, make, model, year, color, speed):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed

    def accelerate(self, speed):
        self.speed += speed

    def decelerate(self, speed):
        self.speed -= speed

    def start(self):
        self.speed = 0

    def stop(self):
        self.speed = 0


# Test

import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle("Honda", "Accord", 2020, "Black", 0)

    def test_accelerate(self):
        self.vehicle.accelerate(5)
        self.assertEqual(5, self.vehicle.speed)

    def test_decelerate(self):
        self.vehicle.decelerate(5)
        self.assertEqual(-5, self.vehicle.speed)

    def test_start(self):
        self.vehicle.start()
        self.assertEqual(0, self.vehicle.speed)

    def test_stop(self):
        self.vehicle.stop()
        self.assertEqual(0, self.vehicle.speed)


if __name__ == "__main__":
    unittest.main()
