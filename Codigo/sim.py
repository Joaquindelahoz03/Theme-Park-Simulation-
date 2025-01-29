import simpy
import random
import os
import csv
from parks import Parks_class

class Simpy: 
    """Class representing the simulation of a theme park using SimPy."""
    
    def __init__(self, parks_instance):
        """Initialize the Simpy class with a Parks_class instance."""
        self.env = parks_instance.env
        self.list_of_attractions = parks_instance.list_of_attractions  
        self.list_of_names = parks_instance.list_of_names  
        self.simulation_time = parks_instance.simulation_time
        self.visitor_data = []  # List to store visitor data

    def visitor(self, person):
        """Defines the behavior of a visitor."""
        while True:
            attraction = random.choice(self.list_of_attractions)  
            yield self.env.timeout(random.randint(2,6))
            visit_time = self.env.now  # Time when visitor starts enjoying the attraction
            print(f"{person} is going to {attraction.name} at time {visit_time}")
            with attraction.capacity.request() as req:
                yield req  
                start_time = self.env.now  # Time when visitor starts enjoying the attraction after waiting in line
                print(f"{person} starts enjoying {attraction.name} at time {start_time}")
                yield self.env.timeout(attraction.duration)  
                end_time = self.env.now  # Time when visitor finishes enjoying the attraction
                print(f"{person} finishes enjoying {attraction.name} at time {end_time}")
                # Store visitor data in the list
                self.visitor_data.append([person, attraction.name, visit_time, start_time, end_time])

    def save_to_csv(self, filename='visitor_data.csv'):
        """Saves visitor data to a CSV file."""
        folder_path = os.path.join(os.path.dirname(__file__), 'CSV_Folder')
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Visitor', 'Attraction', 'Visit Time', 'Start Time', 'End Time'])  # Write headers
            writer.writerows(self.visitor_data)  # Write visitor data

    def run_simulation(self):
        """Runs the simulation."""
        for person in self.list_of_names:
            self.env.process(self.visitor(person))  

        self.env.run(until=self.simulation_time)

        self.save_to_csv()  # Save data to CSV

if __name__ == '__main__':
    parks_instance = Parks_class()  # Create an instance of Parks_class
    parks_instance.park_generator()  # Generate instances of attractions
    parks_instance.visitor_generator()  # Generate visitor names
    
    simpy = Simpy(parks_instance)  # Create an instance of Simpy with the Parks_class instance
    simpy.run_simulation()  # Run the simulation