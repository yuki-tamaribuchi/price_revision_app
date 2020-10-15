import numpy as np
from openpyxl import Workbook,load_workbook
import pandas as pd

class PriceRevision():
    
    def __init__(self):
        pass

    def create_revision_sheet(self):
        wb=Workbook()
        ws=wb.active
        ws.title='改定表貼り付けシート'
        ws['A1']='JAN'
        ws['B1']='品番'
        ws['C1']='商品名'
        ws['D1']='改定価格'
        ws['E1']='備考'

        wb.save('revision.xlsx')


    def read_master_csv(self,master_csv):
        self.__master_jan=np.genfromtxt(master_csv,delimiter=',',skip_header=1,usecols=0,encoding='CP932',dtype=str)

    def read_revision_sheet(self):
        from itertools import islice

        wb=load_workbook('revision.xlsx')
        ws=wb['改定表貼り付けシート']
        data=ws.values
        data=list(data)
        df=pd.DataFrame(data)
        revision_arr=df.to_numpy()
        