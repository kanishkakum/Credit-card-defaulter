from CreditCard.entity import config_entity,artifact_entity
from CreditCard.logger import logging
from CreditCard.exception import CCException
import os,sys
from scipy.stats import ks_2samp


class DataValidation:
    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'**20}")
            self.data_validation_config=data_validation_config
        except Exception as e:
            raise CCException(e, sys)   


    def is_required_column_exist(self) ->bool:
        try:
            pass 
        except Exception as e:
            raise CCException(e, sys)



    def drop_missing_values_columns(self,df:pd.DataFrame,threshold:float=0.3) ->bool:
        try:
            pass 
        except Exception as e:
            raise CCException(e, sys)        


    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        try:
