import datetime
import logging
import os



class Logger:

    def __init__(self):

        current_time = datetime.datetime.now()
        if 'logs' not in os.listdir(os.getcwd()):
            os.mkdir('logs')
        if 'results' not in os.listdir(os.getcwd()):
            os.mkdir('results')
        logs_file = r'logs\xml_operations_logs_{0}.log'.format(current_time.strftime('%d-%m-%Y %H-%M'))

        logging.basicConfig(
            filename=logs_file,
            filemode="w",
            format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
            level = logging.DEBUG
        )

        self.file = logs_file
        self.file_path = os.path.abspath(self.file)
        self.info_message('Начало сессии!')

    def info_message(self, text):
        return logging.info(text)

    def error_message(self, text):
        return logging.error(text)
