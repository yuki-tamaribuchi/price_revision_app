import numpy as np
import pandas as pd
import csv

class PriceRevision():
    
    def __init__(self):
        pass

    def read_master_csv(self,master_csv):
        master=np.loadtxt(master_csv,delimiter=',')

        print(master)
