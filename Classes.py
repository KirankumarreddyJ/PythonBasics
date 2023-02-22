# Note: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
class Car:
    # Class variable (Property)
    wheels = 4
    doors = 4

    # Note: constructor(__init__(self)) is called automatically every time once object created
    # default constructor
    def __init__(self):
        pass

    # Constructor
    def __init__(self, colour, speed):
        # Instance variables
        self.color = colour
        self.maxspeed = speed

        # Local variable
        topdoor = 'Yes'

        print(f"Your car is ready with {colour} colour and maximum speed is {speed} ")

    # Method or Funciton (Bhehaviour)
    def start(self, key):
        print("Car started with " + key)

    # Destructor: It will be called automatically while obj getting deleted
    def __del__(self):
        print(f"Your car with color {self.color} is getting deleted")

#Obj creation
p1 = Car('Black', 200)

#Access class variable
print("No. of weels", p1.wheels)
print("No. of weels", Car.wheels)
# update class property
Car.wheels = 5
print("After update wheels, car value", Car.wheels)
print("After update wheels, car value", p1.wheels)
p1.wheels = 5

#Access instance variable
print("color of car", p1.color)
# print("color of car", Car.color)  #Error

# update instance property
# Car.color = 5 # Error
p1.color = "updated to Green"

# print("After update color, color value", Car.color) #Error
print("After update color, color value", p1.color)
p1.wheels = 5


#Call class method
p1.start("my Key")  # technically => start(p1, "my key")

p2 = Car('Blue', 100)
print("After update wheels, car value", p2.wheels)
print("After update color, color value", p2.color)

# delete instance property
print("Before delete maxspeed: ", p1.maxspeed)
del p1.maxspeed
# print("After delete maxspeed: ", p1.maxspeed)  #Error

# delete p1 object
print("Before delete p1 obj: ", p1)
del p1
# print("After delete p1 obj: ", p1)  #Error

