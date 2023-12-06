
# Refer "AbstractDemo.py" file for Executing
# should define common functions for all vehicles inside this class
# It is known as ABSTRACT CLASS.
# Just an imagination. Not exists in real time



from abc import abstractmethod, ABC      # abc module for abstract class | ABC - Abstract Class
                                         # creating Abs class to avoid object instantiation for the class
                                         # can't create object for this class "Vehicle"

                                        
class Vehicle(ABC):         # Abstract class
                            # intha class ku obj create panna vidama panrom by using absclass
                            # v = Vehicle() - Can't instantiate abstract class Vehicle with abstract method start
    @abstractmethod         # '@'- Decorator       
    def start(self):    
        pass            
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("You are riding a bike..")

class Car(Vehicle):
    def start(self):
        print("You are riding a car..")