import pandas as pd

class StatisticsCollector:
    def __init__(self):
        """Initialize the StatisticsCollector class."""
        self.data = []

    def add_data(self, person:str, attraction:str, visit_time:int, start_time:int, end_time:int) -> None:
        """Add visit data to the collector.

        Args:
            person (str): Name of the person
            attraction (str): Visited attraction
            visit_time (int): Time of visit to the attraction
            start_time (int): Start time of the visit
            end_time (int): End time of the visit
        """
        dict_data = {
            'Visitor': person, 
            'Attraction': attraction, 
            'Visit Time': visit_time,
            'Start Time': start_time, 
            'End Time': end_time}
        self.data.append(dict_data)

    def to_dataframe(self):
        """Convert collected data to a pandas DataFrame."""
        return pd.DataFrame(self.data)
