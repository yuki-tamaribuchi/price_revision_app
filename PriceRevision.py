import numpy as np

class PriceRevision():
    
    def __init__(self):
        pass

    def read_master_csv(self,master_csv):
        master_jan=np.genfromtxt(master_csv,delimiter=',',skip_header=1,usecols=0,encoding='CP932',dtype=str)
