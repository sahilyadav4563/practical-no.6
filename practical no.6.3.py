from abc import ABC, abstractmethod


class CarShowroom(ABC):

    @abstractmethod
    def show_car_details(self):
        pass

    @abstractmethod
    def car_price(self):
        pass

class LuxuryCar(CarShowroom):

    def show_car_details(self):
        print("Car Model  : BMW X5")
        print("Color      : Black")
        print("Fuel Type  : Petrol")

    def car_price(self):
        print("Price      : Rs. 75,00,000")

if __name__ == "__main__":
    car = LuxuryCar()
    car.show_car_details()
    car.car_price()
print("F129")
