import os
import pandas as pd
from datetime import datetime, timedelta
import configparser
import glob

config = configparser.ConfigParser()

def to_csv(data):
    
    pathlink = "./"
    
    if not os.path.isdir(pathlink):
        os.mkdir(pathlink)
        
    present_date= str(datetime.utcnow() + timedelta(hours = 9))[:10]
    
    if len(glob.glob(pathlink + "/" + present_date + ".csv")) ==1:
        cnt= len(pd.read_csv(pathlink + "/" + present_date + ".csv", index_col=0).index)
        time_pd = pd.DataFrame(data, index=[cnt])
        time_pd.to_csv(pathlink + "/" + present_date + ".csv", mode='a', header= False, encoding='utf-8-sig')
    
    else:
        cnt= 0
        time_pd = pd.DataFrame(data,index=[cnt])
        time_pd.to_csv(pathlink + "/" + present_date + ".csv", mode='a', encoding='utf-8-sig')
