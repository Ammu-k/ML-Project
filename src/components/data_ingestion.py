print("File is executing...")
import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:  # Configuration class for data ingestion which contains the path to the train and test data files.
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path to save the training data, artifacts folder is used to store the output of the data ingestion process.
    test_data_path: str = os.path.join('artifacts', 'test.csv')    # Path to save the testing data
    raw_data_path: str = os.path.join('artifacts', 'data.csv')     # Path to save the raw data
    
class DataIngestion:  # Class for data ingestion which contains methods to read, split and save the data.
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()  # Create an instance of the DataIngestionConfig class to access the paths for train, test and raw data.
        
    def initiate_data_ingestion(self):  # Method to read the data, split it into train and test sets and save them to the specified paths.
        print("Data Ingestion Started")
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')  # Read the data from the specified CSV file into a pandas DataFrame.
            
            logging.info("Read the dataset as dataframe")  # logging.info is used to log the information about the data ingestion process.
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)  # Create the directory for the train data path if it does not exist.
            
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header = True)  # Save the raw data to the specified path.
            
            logging.info("Train test split initiated")  # Log the information about the train-test split process.  
            
            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)  # Split the data into train and test sets using an 80-20 split.
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True)  # Save the training data to the specified path.
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True)   # Save the testing data to the specified path.
            
            logging.info("Ingestion of the data is completed")
            
            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)  # Return the paths to the train and test data files.
        
        except Exception as e:
            raise CustomException(e, sys)  # Raise a custom exception if any error occurs during the data ingestion process.
        
if __name__ == "__main__":
    obj = DataIngestion()  # Create an instance of the DataIngestion class.
    obj.initiate_data_ingestion()  # Call the initiate_data_ingestion method to start the data ingestion process.