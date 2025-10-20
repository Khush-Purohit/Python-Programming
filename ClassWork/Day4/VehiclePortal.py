from abc import ABC, abstractmethod
from RentalService import Rental

class Vehicle(ABC):
    def __init__(self, make,model,price):
        self._make = make
        self._model = model
        self._price = price

    @abstractmethod
    def calculate_premiun(self):
        pass


    def __str__(self):
        return f'Vehicle details make: {self._make}, model : {self._model}, price: {self._price}'
    

#super classes are given in brackets
#to make this abstract give name as Car(ABC,Vehicle)
class Car(Vehicle):

    def __init__ (self, make,model,price,segment='standard'):
        super().__init__(make,model,price)
        self._segment = segment

    def calculate_premiun(self):
        if self._segment == 'luxuary':
            return self._price * 0.025
        else:
            return self._price * 0.02
        

    def __str__(self):
        return super().__str__() + f'segment : {self._segment}'
    

 
class Bike(Vehicle):
    def __init__ (self, make,model,price):
        super().__init__(make,model,price)

    def calculate_premiun(self):
        return self._price * 0.015
    


# bike = Bike('abc','bca',100000)

# car = Car('pop', 'ppp', 1000000 )

# print(bike)
# print(car)
# print(bike.calculate_premiun())
# print(car.calculate_premiun())


class Bus(Vehicle,Rental):
    def __init__(self,make,model,price, rental_id):
        Vehicle.__init__(self,make,model,price)
        Rental.__init__(self, rental_id)

    def calculate_rent(self, hrs):
        if(hrs<8):
            return hrs*2000
        else:
            return hrs*2000 + (hrs-8)*1000
        
    def __str__(self):
        return f'Bus: {self._rental_id}, '


class Taxi(Car,Rental):
    def __init__(self, make,model,price,rental_id,segment='standard'):
        Car.__init__(self,make,model,price,segment)
        Rental.__init__(self,rental_id)

    def calculate_rent(self,hrs):
        if hrs<8:
            return hrs*1000
        else:
            return hrs*1000 + (hrs-8)*500
        
taxi = Taxi('tata','Harier', 2000000,12345)
print(taxi)
print(taxi.calculate_rent(10))
print(taxi.calculate_premiun())



bus = Bus('aa','aa',20000,123455)
print(bus)
print(bus.calculate_rent(10))
print(bus.calculate_premiun())