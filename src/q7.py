class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    
    def __init__(self, make, model, year):
        """
        Initialize a Car object with make, model, and year attributes
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model name of the car
            year (int): The manufacturing year of the car
        """
        self.make = make    # Store the car's manufacturer
        self.model = model  # Store the car's model name
        self.year = year    # Store the car's manufacturing year

    def describe_car(self):
        """
        Print information about the car in the format "Year Make Model"
        """
        print(f"{self.year} {self.make} {self.model}")


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

# Create a Car instance with the specified attributes
print("Creating a Car instance: Toyota Corolla 2020")
my_car = Car("Toyota", "Corolla", 2020)

# Call the describe_car method to display the car information
print("Calling describe_car() method:")
my_car.describe_car()
print()
