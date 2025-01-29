from sim import Simpy

class Menu:
    def __init__(self, simpy_instance):
        """Initialize the Menu class.

        Args:
            simpy_instance (Simpy): Instance of the Simpy class.
        """
        self.simpy_instance = simpy_instance

    def run(self):
        """Runs the simulation."""
        print("Running simulation...")
        self.simpy_instance.run_simulation()
        print("Simulation completed.")

if __name__ == "__main__":
    simpy_instance = Simpy()
    menu = Menu(simpy_instance)
    menu.run()