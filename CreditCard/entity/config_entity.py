import os,sys
from datetime import datetime
from CreditCard.logger import logging
from CreditCard.exception import CCException



FILE_NAME="CreditCard.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"
class TrainingPipelineConfig:
    try:
        def __init__(self):
            self.artifact_dir=os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%y_%h%m%s')}")
    except Exception as e:
        raise CCException(e,sys)      

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
            try:
                self.database_name="Credit_Card"
                self.collection_name="CC_Defaulter"
                self.data_ingestion_dir=os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
                self.feature_store_file_path=os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
                self.train_file_path=os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
                self.test_file_path=os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
                self.test_size=0.2
            except Exception as e:
                raise CCException(e,sys)

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
                raise CCException(e,sys)    
                            

        
      


class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...