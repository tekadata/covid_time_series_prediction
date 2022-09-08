import pandas as pd
import numpy as np
from data import country_data



class Indicator:
    '''
    DataFrames containing all indicators as index,
    and various sub-indicators as columns
    '''
    def __init__(self):
        # Assign an attribute ".data" to all new instances of Order
        self.data = Indicator().get_country_data()

    def get_country_data(self, country_name='France') -> pd.DataFrame:
        country_index, country_indicator = country_data.country_output(country_name=country_name)
        return country_index, country_indicator
    
    def get_database(self) -> dict:
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities

        root_dir = os.path.dirname(os.path.dirname(__file__))
        csv_path = os.path.join(root_dir, "raw_data")

        # list of file names
        file_names = [f for f in os.listdir(csv_path) if f.endswith(".csv")]

        # list of key names
        key_names = [key_name.replace(".csv", "") for key_name in file_names]

        # Create the dictionary of file names
        return {k: pd.read_csv(os.path.join(csv_path, f)) for k, f in zip(key_names, file_names)}



    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")