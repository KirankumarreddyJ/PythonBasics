# Note:
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
class Car:

    # Constructor
    def __init__(self, colour, speed):
        # Instance variables
        self.colour = colour
        self.maxspeed = speed
        # print(f"Your car is ready with {colour} colour and maximum speed is {speed} ")

    # The string representation of an object WITH the __str__() function
    def __str__(self):
        return f"This car is '{self.colour}' colour and maximum speed is '{self.maxspeed}'"


#Obj creation
p1 = Car('Black', 200)
print("p1 object : ", p1)

p2 = Car('Red', 100)
print("p2 object : ", p2)

