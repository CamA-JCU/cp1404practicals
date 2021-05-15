"""
CP1404/CP5632 Prac_08 silver_service_taxi_test.py
Cameron Attard
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


hummer = SilverServiceTaxi("Hummer", 200, 2)
print(hummer)
hummer.drive(18)
print(hummer)
print(hummer.get_fare())
