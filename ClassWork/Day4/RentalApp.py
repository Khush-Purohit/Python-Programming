from VehiclePortal import Taxi,Bus
from RentalService import Rental

class RentalApp:
    
    @staticmethod
    def display_rent(rental_Vehicle:Rental):
        print('-----Welcome to my rental app')
        hrs = int(input('Enter the number of hours for which you want to rent:'))
        amount = rental_Vehicle.calculate_rent(hrs)
        print(f'total rent for {rental_Vehicle} : Rs. {amount}')

    
print('----------THE USER -----------')
taxi = Taxi('tata','Harier', 2000000,12345)
print(RentalApp.display_rent(taxi))
# print(taxi)
# print(taxi.calculate_rent(10))
# print(taxi.calculate_premiun())



bus = Bus('aa','aa',20000,123455)
print(RentalApp.display_rent(bus))
# print(bus)
# print(bus.calculate_rent(10))
# print(bus.calculate_premiun())