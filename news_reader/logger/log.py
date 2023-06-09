import logging
import os
from datetime import datetime
from news_reader.config import config_data

class Log:
    def __init__(self,name):
        self.name = name

    def get_log_file_path(self):
        log_file = ""
        try:
            current_dir = os.getcwd()
            log_folder = os.path.join(current_dir, config_data["log_folder_name"]) 
            current_year = datetime.now().year
            current_month = datetime.now().month
            current_date = datetime.now().day
            folder_name = log_folder+"/"+str(current_year)+"/"+str(current_month)+"/"+str(current_date)
            folder_path = os.path.join(os.getcwd(), folder_name)  
            log_file = folder_path+"/"+"error.log"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except Exception as e:
            print(str(e)) 
        return log_file

    
    def write(self,ex):
        log_file = self.get_log_file_path()
        logging.basicConfig(filename = log_file, level = logging.ERROR)
        try:            
            logging.error(str(ex), exc_info = True) 
        except Exception as e:
            print(str(e))                