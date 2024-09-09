#Define a class named car
class Car:
    #Attributes of the class
    wheels=4
    make=""
    model=""#Model of the car
    year=""
    number_of_cars=0
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        Car.number_of_cars += 1
    #Method to display info about the car
    def display_info(self):
        print(f"Car Information: \nYear of manufacturing: {self.year} \nMake: {self.make} \nModel: {self.model}")

    @classmethod
    def get_number_of_cars(cls):
        print(f"no of cars : {cls.number_of_cars}")
if __name__=="__main__":
    #Creating Objects(instances) of the Car Class
    # car1=Car()
    # car1.model="Toyota"
    # car1.make="Corolla"
    # car1.year="2020"
    #
    # car2=Car()
    # car2.model="Honda"
    # car2.make="Civic"
    # car2.year="2021"
    #Calling the method of the objects
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Hyundai", "Civic", 2022)

    car1.display_info()
    car2.display_info()


    Car.get_number_of_cars()