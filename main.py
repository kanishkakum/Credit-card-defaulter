from CreditCard.logger import logging
from CreditCard.exception import  CCException
import sys,os 
from CreditCard.entity.config_entity import DataIngestionConfig
from CreditCard.entity import config_entity
from CreditCard.component.DataIngestion import DataIngestion

def test_logger():
     try:
          pass
     except Exception as e:
          raise CCException(e, sys)    

if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config= DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
          print(e)