import datetime
import os
import pathlib
import sys
import time

from modules import logger
from modules import xml_operations



def main():
    extensions = ['xml', 'xsd', 'xsl']
    paths_dict = {}

    log = logger.Logger()

    for extension in extensions:
        path_valid = False
        step = 'Валидация пути к {} файлу.\n'.format(extension.upper())
        log.info_message(step)
        path = input('Введите абсолютный путь к {} файлу: '.format(extension.upper()))

        while path_valid is False:
            if path == 'exit':
                sys.exit()
            if os.path.isfile(path):
                if pathlib.Path(path).suffix == '.{}'.format(extension):
                    paths_dict[extension] = path
                    path_valid = True
                    log.info_message('Валидация пути {} файла успешно выполнена.\n'.format(extension))
                    print('Валидация пути {} файла успешно выполнена.\n'.format(extension))
                else:
                    error = 'Файл неверного формата! Нужен файл с расширением .{0}!'.format(extension)
                    print(error)
                    log.error_message(error)
                    path = input('Введите абсолютный путь к {} файлу: '.format(extension.upper()))
            else:
                error = 'В адресе вашего пути нет файла или такого файла не существует!\n'
                print(error)
                log.error_message(error)
                path = input('Введите абсолютный путь к {} файлу: '.format(extension.upper()))

    operator = xml_operations.XmlOperator(log)

    print('Валидация XML файла по XSD схеме')
    if operator.validate_xml(paths_dict['xml'], paths_dict['xsd']):
        print('Валидация XML файла по XSD схеме успешно завершена.')
        print()
        print('Трансформация файла по XSLT.')
        if operator.transform_by_xslt(paths_dict['xsl']):
            print('Трансформация файла по XSLT успешно завершена.')
            files = os.listdir(os.getcwd() + r'\results')
            result = operator.result_file(files)
            path = operator.save_result(result)
            print('Новый файл успешно сохранен!')
            print('Его путь  --  {}'.format(path))
            print('Сессия завершена.')
            print()
            answer = input('Повторить операцию с другими файлами? [ДА,НЕТ]\n')
            if answer.upper() == 'ДА':
                print()
                main()
            else:
                print('Всего доброго!')
                time.sleep(2)
                sys.exit()
        else:
            print('Трансформация по XSLT не осуществилась из-за ошибки или иной причины.')
            print('Смотрите лог-файл {}'.format(log.file))
            print('Его путь  --  {}'.format(log.file_path))
    else:
        print('Ваш XML файл не прошел валидацию.')
        print('Смотрите лог-файл {}'.format(log.file))
        print('Его путь  --  {}'.format(log.file_path))

    time.sleep(3)
    sys.exit()


if __name__ == '__main__':
    main()
