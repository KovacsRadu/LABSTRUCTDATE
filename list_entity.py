from seminarul_1.domain.car_entity import Masina


class CarOperations:
    def __init__(self):
        self.__cars = []
        with open("masini", "r") as file:
            for linie in file:
                parts = linie.strip().split()  # Împărțim linia pe spații și eliminăm eventuale spații suplimentare
                marca, model, token, pretAchizitie, pretVanzare = parts[0], parts[1], parts[2], int(parts[3]), int(
                    parts[4])
                masina = Masina(marca, model, token, pretAchizitie, pretVanzare)
                self.__cars.append(masina)

    def add_car(self):
        marca = input("Introduceți marca: ")
        model = input("Introduceți modelul: ")
        token = input("Introduceți tokenul: ")
        pretAchizitie = int(input("Introduceți prețul de achiziție: "))
        pretVanzare = int(input("Introduceți prețul de vânzare: "))
        car = Masina(marca, model, token, pretAchizitie, pretVanzare)
        self.__cars.append(car)

    def get_cars(self):
        return self.__cars
    def set_cars(self, cars):
        self.__cars = cars


    def get_car(self, index):
        return self.__cars[index]

    def update_car(self, index, car):
        self.__cars[index] = car

    def delete_car(self, index):
        self.__cars.pop(index)

    

