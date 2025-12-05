# Abstraction Example
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start (self):
           pass

class Car(Vehicle):
      def start(self):
            print("Car engine started: ")

class Bike(Vehicle):
      def start(self):
            print("Bike engine started: ")

car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()
             
    