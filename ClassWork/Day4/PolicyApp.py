from VehiclePortal import Car, Bike, Vehicle
from Employees import Employee

class Policy:
    @staticmethod
    #vehicle:Vehicle just for readability
    def display_policy(vehicle:Vehicle): #just specifying what are we expecting, but we can give anu object
        if (year < 5) :
            amount = vehicle.calculate_premiun()
        else:
            amount = vehicle.calculate_premiun() + 1000

        print(f'Total premium due for vehicle: {amount}')




'''This can be written in another module'''

my_car = Car('honda', 'city', 1500000)
my_bike = Bike('suzuki','gixer', 100000)

def show_premium(vehicle:Vehicle):
    year = int(input("Enter how old is the vehicle: "))
    Policy.display_policy(v,year)


show_premium(my_bike)
show_premium(my_car)

# Policy.display_policy(my_car)
# Policy.display_policy(my_bike)
# # Policy.display_policy(self)  ducktypeing


print('--------Admin----------')


Vehicles = [my_car,my_bike]

for v in Vehicles:
    Policy.display_policy(v,year=1)



