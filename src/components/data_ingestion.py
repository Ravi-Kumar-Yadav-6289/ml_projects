from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
import os
import sys


@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join("datastore","train.csv")
    test_data_path : str=os.path.join("datastore",'test.csv')
    raw_data_path : str=os.path.join("datastore","raw.csv")


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    def initiateIngestion(self):
        logging.info("Entering DataIngestion method.")

        try:
            df =  pd.read_csv(r"D:\ML_Projects\analysis_notebooks\data\StudentsPerformance.csv")
            logging.info("Reading raw data from path to a dataframe complete.")

            #making the datastore folder here
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path)

            logging.info("initiating train test split")

            train_data, test_data = train_test_split(df,test_size=0.2,random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path)
            test_data.to_csv(self.ingestion_config.test_data_path)

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        



if __name__=='__main__':
    load_data = DataIngestion()
    load_data.initiateIngestion()
    
    