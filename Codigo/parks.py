from Names.names import Names  # Import the Names class from the Names module
from Attractions import Attractions  # Import the Attractions class

import simpy  # Import the simpy module


class Parks_class:
    """Class representing a theme park."""

    def __init__(self):
        """Initialize the Parks_class."""
        self.env = simpy.Environment()  # Create a SimPy environment
        self.list_of_attractions = []  # List to store attraction instances
        self.list_of_names = []  # List to store visitor names
        self.simulation_time = 20  # Duration of the simulation
        self.visitor_data = []  # List to store visitor data

    def park_generator(self):
        """Generate instances of attractions in the theme park."""
        for _ in range(10):  
            attractions_instance = Attractions(self.env)  # Create an instance of Attractions
            self.list_of_attractions.append(attractions_instance)  # Add the instance to the list of attractions

    def visitor_generator(self):
        """Generate visitor names."""
        for _ in range(2000):  
            name_instance = Names()  # Create an instance of Names
            person_name = name_instance.name  # Get a random name
            self.list_of_names.append(person_name)  # Add the name to the list of names

    