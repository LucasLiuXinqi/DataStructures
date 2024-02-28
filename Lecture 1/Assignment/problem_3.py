class Vehicle:
    # Please write your code here and make any necessary changes to the line above (if any)
    pass
    def __init__(self, power = 0, brand = '', owner = None):
        self._power = power
        self._brand = brand
        self._owner = owner

    def drive(self):
        return 'Driving'

    def sell(self, new_owner):
        self._owner = new_owner

    def __add__(self, other):
        new_power = Vehicle()
        #这里写错了, 应该将new_power的brand, owner!!!!!!!!!!!!!!!!!!!!
        new_power._power = self._power + other._power
        return new_power


    def __iadd__(self, other):
        self._power += other._power
        return self

    def __str__(self):
        return f"Brand: {self._brand}, Power: {self._power}, Owner: {self._owner.__repr__()}"



class Person:
    # Please write your code here and make any necessary changes to the line above (if any)
    pass
    def __init__(self, firstname = '', lastname = ''):
        self._firstname = firstname
        self._lastname = lastname


    def change_name(self, first, last):
        self._firstname = first
        self._lastname = last

    def sell_vehic(self, v, new_owner):
        if self._firstname == v._owner._firstname and self._lastname == v._owner._lastname:
            v._owner = new_owner


    def __repr__(self):
        return f"Person({self._firstname}, {self._lastname})"



class Truck(Vehicle):
    # Please write your code here and make any necessary changes to the line above (if any)
    pass
    def __init__(self, power = 0, brand = '', owner = None, max_cargo = 0):
        super().__init__(power, brand, owner)
        self._max_cargo = max_cargo

    def __add__(self, other):
        new_max_cargo = Truck()
        #这里也是同样的错误!!!!!!!!!!!!!!!!!!!!
        new_max_cargo._max_cargo = self._max_cargo + other._max_cargo
        return new_max_cargo

    def __iadd__(self, other):
        self._max_cargo += other._max_cargo
        return self

    def __sub__(self, other):
        new_max_cargo = Truck()
        new_max_cargo._max_cargo = self._max_cargo - other._max_cargo
        return new_max_cargo

    def __isub__(self, other):
        self._max_cargo -= other._max_cargo
        return self

    def __str__(self):
        return f'Brand: {self._brand}, Power: {self._power}, Owner: {self._owner.__repr__()}, c: {self._max_cargo}'

class Car(Vehicle):
    # Please write your code here and make any necessary changes to the line above (if any)
    pass
    def __init__(self, power, brand, owner):
        super().__init__(power, brand, owner)

    def __repr__(self):
        return f'Car({self._brand}, {self._power}, {self._owner._firstname}, {self._owner._lastname})'


def main():
    # Create a Person
    person1 = Person("John", "Doe")

    # Create Vehicles
    car1 = Car(200, "Toyota", person1)
    truck1 = Truck(300, "Ford", person1, 1000)
    car2 = Car(150, "Honda", person1)
    truck2 = Truck(250, "Chevrolet", person1, 800)
    car2._power = 20

    # Display initial vehicle details
    print("Initial Vehicle Details:")
    print(car1)  # should print Brand: Toyota, Power: 200, Owner: Person(John, Doe)
    print(truck1)  # should print Brand: Ford, Power: 300, Owner: Person(John, Doe), c: 1000
    print(car2)  # should print Brand: Honda, Power: 150, Owner: Person(John, Doe)
    print(truck2)  # should print Brand: Chevrolet, Power: 250, Owner: Person(John, Doe), c: 800

    print("\nRepresentation Details:")
    print(car2.__repr__())  # should print Car(Honda, 150, John, Doe)
    print(person1.__repr__())  # should print Person(John, Doe)

    # Change the name of the person
    person1.change_name("Jane", "Smith")

    # Sell vehicles to a new owner
    person2 = Person("Peter", "Moldan")
    person1.sell_vehic(car1, person2)
    person2.sell_vehic(truck2, person1)

    # Perform vehicle addition and subtraction
    print("\nVehicle Addition and Subtraction:")
    result_add = car1 + car2
    result_sub = truck1 - truck2
    print("Result of car1 + car2:", result_add._power)  # should print 350
    print("Result of truck1 - truck2:", result_sub._max_cargo)  # should print 200

    # Display updated vehicle details
    print("\nUpdated Vehicle Details:")
    print(car1)  # should print Brand: Toyota, Power: 200, Owner: Person(Peter, Moldan)
    print(truck1)  # should print Brand: Ford, Power: 300, Owner: Person(Jane, Smith), c: 1000
    print(car2)  # should print Brand: Honda, Power: 150, Owner: Person(Jane, Smith)
    print(truck2)  # should print Brand: Chevrolet, Power: 250, Owner: Person(Jane, Smith), c: 800



if __name__ == '__main__':
    main()
