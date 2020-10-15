import numpy as np
import pandas as pd

class PriceRevision():

    def load_master(self,filepath):
        self.__master_df=pd.read_csv(filepath_or_buffer=filepath,encoding='CP932',low_memory=False,header=0)


    def create_maker_list(self):
        self.__makers=self.__master_df['メーカー名称'].unique()

    def query_by_maker(self,maker):
        queried_df=self.__master_df[self.__master_df['メーカー名称']==maker]
        print(queried_df)