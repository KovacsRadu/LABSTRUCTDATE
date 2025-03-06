from seminarul_1.domain.car_entity import Masina
from seminarul_1.repository.list_entity import CarOperations
def run(ServiceOperations):
    while True:
        print("1. Add a car")
        print("2. Display all cars")
        print("3. Bubble Sort cars by purchase price")
        print("X. Exit")
        option = input("Enter your option: ")
        if option == "1":
            ServiceOperations.add_car()
        elif option == "2":
             ServiceOperations.display_cars()
        elif option == "3":
            ServiceOperations.bubblesort()
        elif option == "x" or option=="X":
            break
        else:
            print("Invalid option")