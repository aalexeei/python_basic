class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_num_doors(self):
        return self.num_doors


class Truck(Vehicle):
    def __init__(self, make, model, year, payload_capacity):
        super().__init__(make, model, year)
        self.payload_capacity = payload_capacity

    def get_payload_capacity(self):
        return self.payload_capacity


class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def get_species(self):
        return self.species

    def get_name(self):
        return self.name

    def say(self):
        pass  # to be implemented in subclasses


class Dog(Animal):
    def __init__(self, name):
        super().__init__('dog', name)

    def say(self):
        return 'Woof!'


class Cat(Animal):
    def __init__(self, name):
        super().__init__('cat', name)

    def say(self):
        return 'Meow!'

class SportsCar(Car):
    def __init__(self, make, model, year, num_doors, top_speed):
        super().__init__(make, model, year, num_doors)
        self.top_speed = top_speed

    def get_top_speed(self):
        return self.top_speed


class PickupTruck(Truck):
    def __init__(self, make, model, year, payload_capacity, tow_capacity):
        super().__init__(make, model, year, payload_capacity)
        self.tow_capacity = tow_capacity

    def get_tow_capacity(self):
        return self.tow_capacity


class Bird(Animal):
    def __init__(self, species, name):
        super().__init__(species, name)

    def fly(self):
        pass  # to be implemented in subclasses


class Parrot(Bird):
    def __init__(self, name):
        super().__init__('parrot', name)

    def fly(self):
        return 'Flying!'


class Penguin(Bird):
    def __init__(self, name):
        super().__init__('penguin', name)

    def fly(self):
        return 'Sorry, I can\'t fly!'


# create a vehicle object
vehicle = Vehicle('Tesla', 'Model 3', 2021)
print(vehicle.get_make())
print(vehicle.get_model())
print(vehicle.get_year())

# create a car object
car = Car('Toyota', 'Corolla', 2022, 4)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car.get_num_doors())

# create a truck object
truck = Truck('Ford', 'F-150', 2023, 2000)
print(truck.get_make())
print(truck.get_model())
print(truck.get_year())
print(truck.get_payload_capacity())

# create a dog object
dog = Dog('Fido')
print(dog.get_species())
print(dog.get_name())
print(dog.say())

# create a cat object
cat = Cat('Fluffy')
print(cat.get_species())
print(cat.get_name())
print(cat.say())

# create a sports car object
sports_car = SportsCar('Porsche', '911', 2023, 2, 200)
print(sports_car.get_make())
print(sports_car.get_model())
print(sports_car.get_year())
print(sports_car.get_num_doors())
print(sports_car.get_top_speed())

# create a pickup truck object
pickup_truck = PickupTruck('Chevrolet', 'Silverado', 2022, 3000, 5000)
print(pickup_truck.get_make())
print(pickup_truck.get_model())
print(pickup_truck.get_year())
print(pickup_truck.get_payload_capacity())
print(pickup_truck.get_tow_capacity())

# create a parrot object
parrot = Parrot('Polly')
print(parrot.get_species())
print(parrot.get_name())
print(parrot.fly())

# create a penguin object
penguin = Penguin('Tux')
print(penguin.get_species())
print(penguin.get_name())
print(penguin.fly())
