#import ABC
#from abc import ABCMeta, abstractmethod
import abc

# ABCMeta = Abstract Class
class Shape(object):
    @abc.abstractmethod #defines an abstractmethod
    def area(self):
        return 0

class Square(Shape):
        def __init__(self, side):
            self.side =side

        ## overload of +
        def __add__(squareOne, squareTwo):
            return 4*squareOne.side + 4*squareTwo.side

        def area(self):
            print ("Square area: ", self.side * self.side)

class Rectangle(Shape):
    def __init__(self, pLength, pWidth):
        self.width = pWidth
        self.length = pLength

    def area(self):
        print("Area of rectangle ", self.width * self.length)

squareOne = Square(5)
squareTwo = Square(10)
print("The sum of the perimeters is ", squareOne+squareTwo)


rectangle = Rectangle(10,5)
square = Square(3)
square.area()
rectangle.area()