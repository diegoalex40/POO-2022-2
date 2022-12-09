from car import Car
from accountDriver import Driver
from accountUser import User
from route import Route
from payment import Payment

class Trip(Car, Driver, User, Route, Payment):
    idTrip = int

    def __init__(self, idTrip,  Car, User, Driver, Route, Payment):
        super().__init__(Car, User, Driver, Route, Payment)
        self.idTrip = idTrip