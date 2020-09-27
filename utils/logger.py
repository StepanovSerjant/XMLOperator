import datetime
import logging
import os
import sys


class Logger:

    def __init__(self):
        Logger.create_log_dir()
        self.filename = Logger.create_logs_filename() 
        self.file_path = os.path.abspath(self.filename)
        self.set_config()
        self.info_message('Начало сессии!')

    def set_config(self):
        logging.basicConfig(
            filename=self.filename,
            filemode="w",
            format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
            level = logging.DEBUG
        )  

    def info_message(self, text):
        return logging.info(text)

    def error_message(self, text):
        return logging.error(text)

    def error_notification(self, text, error):
        self.error_message(text)
        self.error_message('Произошла ошибка. Проверьте файлы и повторите снова.')
        self.error_message(f'Ошибка: {error}')
        self.error_message(sys.exc_info())

    @staticmethod
    def create_log_dir():
        if 'logs' not in os.listdir(os.getcwd()):
            os.mkdir('logs')

    @staticmethod
    def create_logs_filename():
        current_time = datetime.datetime.now().strftime('%d-%m-%Y %H-%M')
        logs_file = f'logs/xml_operations_logs_{current_time}.log'
        return logs_file
