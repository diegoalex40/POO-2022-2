from pprint import pprint
from account import Account
from accountDriver import Driver
from accountUser import User
from car import Car
from payment import Payment
from paymentCard import PaymentCard
from paymentCash import PaymentCash
from paymentTransfer import PaymentTransfer
from route import Route
from trip import Trip
from uberXL import UberXL
from uberConfort import UberConfort
from uberX import UberX

if __name__ == "__main__":
    """usuario1 = User(1, "Diego Yanez", "Masculino", 99999999, 29)
    print(vars(usuario1))
    
    usuario2 = User(2, "Diego Yanez", "Masculino", 99999999, 39)
    print(vars(usuario2))
    
    driver1 = Driver(3, "Alexander Flores", "Masculino", 9999999, 29, "Licencia111")
    print(vars(driver1))
    """
    
    carro1 = Car("PBC-555555", "Chevrolet Corsa", "Gris", 2015, Driver(3, "Alexander Flores", "Masculino", 9999999, 29, "Licencia111"))
    print(vars(carro1))
    print(vars(carro1.driver))
    
    
    #uberX1   = UberX("XLX-5599", "Chevrolet Corsa", "Gris", 2015, driver1)
    #print(vars(uberX1))