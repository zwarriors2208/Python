from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        print("This method is for starting the vehicle")
    def stop(self):
        print("This method is for stopping the vehicle")

class Bus(Vehicle):
    def start(self):
        print("This method is for starting the bus")
    def stop(self):
        print("This method is for stopping the bus")

class Car(Vehicle):
    def start(self):
        print("This method is for starting the car")
    def stop(self):
        print("This method is for stopping the car")

class Bike(Vehicle):
    def start(self):
        print("This method is for starting the bike")
    def stop(self):
        print("This method is for stopping the bike")

class Garage:
    vehicle_list = []
    # @classmethod
    # def add_vehicle(cls, x):
    #
    #     x = cls
    #     Garage.vehicle_list.append(x)
    @classmethod
    def add_vehicle(self, *args):
        # x = cls()
        Garage.vehicle_list.extend(args)

    def starts(obj):
        obj.start()
    def stops(obj):
        obj.stop()


# tuntuna = Vehicle()

# Garage.add_vehicle(Car, 'alto')

alto = Car()
Garage.add_vehicle(alto)
Garage.starts(alto)
# alto.start()
# alto.stop()
splendor = Bike()
Garage.add_vehicle(splendor)
Garage.starts(splendor)
# splendor.start()
# splendor.stop()
volvo = Bus()
Garage.add_vehicle(volvo)
Garage.starts(volvo)
# volvo.start()
# volvo.stop()
# Garage.add_vehicle(Bike, 'splendor')
print(len(Garage.vehicle_list))
