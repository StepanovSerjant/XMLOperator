import os
import sys
import time

import services
from utils.logger import Logger
from utils.xml_operations import XmlOperator


def main():
    log = Logger()

    # получение путей к файлам для трансформации
    paths_dict = dict()
    extensions = ['xml', 'xsd', 'xsl']
    for extension in extensions:
        step = f'Валидация пути к {extension.upper()} файлу.\n'
        log.info_message(step)
        
        path_valid = False
        while path_valid is False:
            path = input(f'Введите абсолютный путь к {extension.upper()} файлу: ')
            if path == 'exit':
                sys.exit()
            elif services.path_validation(path, extension)['status']:
                paths_dict[extension] = path
                path_valid = True
            else:
                error_message = services.path_validation(path, extension)['error_msg']
                print(error_message)
                log.error_message(error_message)
                
    # Основная логика скрипта
    operator = XmlOperator(log)
    print('Валидация XML файла по XSD схеме')
    if operator.validate_xml(paths_dict['xml'], paths_dict['xsd']):
        print('Валидация XML файла по XSD схеме успешно завершена.\n')
        print('Трансформация файла по XSLT.')
        if operator.transform_by_xslt(paths_dict['xsl']):
            print('Трансформация файла по XSLT успешно завершена.')
            file_dir = os.path.join(os.getcwd(), 'results')
            filename = operator.get_xml_filename(file_dir)
            result_path = operator.save_result(filename)
            
            print('Новый файл успешно сохранен!')
            print(f'Его путь  --  {result_path}')
            print('Сессия завершена.\n')
            return services.restart()
        else:
            print('Трансформация по XSLT не осуществилась из-за ошибки или иной причины.')
    else:
        print('Валидация XML файла по XSD схеме не осуществилась из-за ошибки или иной причины.')
    print(f'Смотрите лог-файл {log.file_path}')
    
    time.sleep(3)
    sys.exit()


if __name__ == '__main__':
    main()
