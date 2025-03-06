from seminarul_1.repository.list_entity import CarOperations
from seminarul_1.domain.car_entity import Masina

class ServiceOperations():
    def __init__(self,repository):
        self.__repository = repository

    def bubblesort(self):
        cars = self.__repository.get_cars()  # Store the car list in a variable
        n = len(cars)

        for i in range(n - 1):  # Number of passes
            for j in range(n - 1 - i):  # Compare adjacent cars
                if cars[j].pretAchizitie > cars[j + 1].pretAchizitie:  # Swap if needed
                    cars[j], cars[j + 1] = cars[j + 1], cars[j]  # Swap the objects

        self.__repository.set_cars(cars)
    def display_cars(self):
        cars = self.__repository.get_cars()
        for car in cars:
            print(car)
    # bubble  sort si quicksort