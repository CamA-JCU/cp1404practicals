"""
CP1404/CP5632 Prac_08 unreliable_car_test.py
Cameron Attard
"""

from prac_08.unreliable_car import UnreliableCar

unreliable_car = UnreliableCar("Kia 1", 100, 40)
print(unreliable_car)
unreliable_car.drive(40)
print(unreliable_car)
unreliable_car.drive(50)
print(unreliable_car)