import random
import simpy

class Attractions: 
    """Class representing the attractions in the park.
    
    Args:
        env (simpy.Environment): Simpy simulation environment
        
    Attributes:
        env (simpy.Environment): Simpy simulation environment
        name (str): Name of the attraction park
        capacity (int): Maximum capacity of the attraction park
        duration (int): Duration of the visit to the attraction park
    """

    def __init__(self, env: simpy.Environment):
        """Initialize the Attractions class."""
        self.env = env
        attraction_info = self.read_txt_file('spanish_attraction_parks.txt')
        if attraction_info:
            self.name, capacity_str, duration_str = attraction_info
            self.capacity = int(capacity_str)
            self.duration = int(duration_str)  # Convert duration from string to integer
        self.capacity = simpy.Resource(env, capacity=self.capacity)

    def read_txt_file(self, attraction_info_file):
        """Reads information about the attraction park from a text file.
        
        Args:
            attraction_info_file (str): Path to the text file containing attraction park information
        
        Returns:
            list: Information about the attraction park (name, capacity, duration)
        """
        with open(attraction_info_file, 'r') as file:
            lines = file.readlines()
            attraction_info = [line.strip().split(", ") for line in lines]
        if attraction_info:
            return random.choice(attraction_info)
        else:
            return None