from CreditCard.entity import config_entity,artifact_entity
from CreditCard.logger import logging
from CreditCard.exception import CCException
import os,sys
from scipy.stats import ks_2samp
from typing import Optional
import pandas as pd 
from CreditCard import utils
import numpy as np 


class DataValidation:
    def __init__(self,data_validation_config:config_entity.DataValidationConfig,
    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'**20}")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
            Self.validation_error = dict()
        except Exception as e:
            raise CCException(e, sys)   


 


    def drop_missing_values_columns(self,df:pd.DataFrame) ->Optional[pd.DataFrame]:
        try:
            """
            This function will drop column which contains missing value more than threshold

            df : accepts a panda dataframe
            threshold : percentage criteria to drop columns

            returns pandas dataframe if single column is available after dropping missing column else None
            """ 

            threshold = self.data_validation_config.missing_threshold
            null_report = df.isna().sum()/df.shape[0]
            #selecting column name which contains null
            logging.info(f"selecting column name which contains null above to {threshold}")
            drop_column_names = null_report[null_report>threshold].index

            logging.info(f"Columns to drop: {list(drop_column_names)}")
            self.validation_error[report_key_name]=list(drop_column_names)
            df.drop(list(drop_column_names),axis=1,inplace=True)

            #return None no columns left
            if len(df.columns)==0:
                return None
            return df

        except Exception as e:
            raise CCException(e, sys)        

    def is_required_column_exist(self,base_df:pd.DataFrame,current_df:pd.DataFrame) ->bool:
        try:
            base_df = base_df.columns
            current_df = current_df.columns 
            missing_column= []
            for base_column in base_df:
                if base_column not in current_df:
                    logging.info(f"Column: [{base} is not available.]")
                    missing_column.append(base_column)

            if len(missing_columns)>0:
                self.validation_error[report_key_name]=missing_columns
                return False
            return True        
        except Exception as e:
            raise CCException(e, sys)


    def data_drift(self,base_df:pd.DataFrame, current_df:pd.DataFrame):
        try:
            drift_report=dict()

            base_columns = base_df.columns
            current_columns = current_df.columns

            for base_column in base_columns:
                base_data,current_data = base_df[base_column],current_df[base_column]
                #Null hypothesis is that both column data drawn from same distrubtion
                
                logging.info(f"Hypothesis {base_column}: {base_data.dtype}, {current_data.dtype} ")
                same_distribution =ks_2samp(base_data,current_data)

                if same_distribution.pvalue>0.05:
                    #We are accepting null hypothesis
                    drift_report[base_column]={
                        "pvalues":float(same_distribution.pvalue),
                        "same_distribution": True
                    }
                else:
                    drift_report[base_column]={
                        "pvalues":float(same_distribution.pvalue),
                        "same_distribution":False
                    }
                    #different distribution

            self.validation_error[report_key_name]=drift_report
        except Exception as e:
            raise SensorException(e, sys)

         


    def initiate_data_validation(self)->artifact_entity.DataValidationArtifact:
        try:
            logging.info(f"Reading base dataframe")
            base_df = pd.read_csv(self.data_validation_config.base_file_path)
            base_df.replace({"na":np.NAN},inplace=True)
            logging.info(f"Replace na value in base df")
            #base_df has na as null
            logging.info(f"Drop null values colums from base df")
            base_df=self.drop_missing_values_columns(df=base_df,report_key_name="missing_values_within_base_dataset")

            logging.info(f"Reading train dataframe")
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            logging.info(f"Reading test dataframe")
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            logging.info(f"Is all required columns present in train df")
            train_df_columns_status = self.is_required_columns_exists(base_df=base_df, current_df=train_df,report_key_name="missing_columns_within_train_dataset")
            logging.info(f"Is all required columns present in test df")
            test_df_columns_status = self.is_required_columns_exists(base_df=base_df, current_df=test_df,report_key_name="missing_columns_within_test_dataset")

            if train_df_columns_status:
                logging.info(f"As all column are available in train df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=train_df,report_key_name="data_drift_within_train_dataset")
            if test_df_columns_status:
                logging.info(f"As all column are available in test df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=test_df,report_key_name="data_drift_within_test_dataset")
                
        except Exception as e:
            raise CCException(e, sys)
