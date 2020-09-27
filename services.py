import os
import pathlib

import main


def path_validation(path, extension):
    """ Валидация пути к файлу с определенным расширением """
    if not os.path.isfile(path):
        msg = 'В адресе вашего пути нет файла или такого файла не существует!\n'
        return {'status': False, 'error_msg': msg}
    elif pathlib.Path(path).suffix == f'.{extension}':
        msg = f'Валидация пути {extension} файла успешно выполнена.\n'
        return {'status': True, 'message': msg}
    else:
        msg = f'Файл неверного формата! Нужен файл с расширением .{extension}!'
        return {'status': False, 'error_msg': msg}


def restart():
    """ Функция для рестарта основного скрипта """
    answer = input('Повторить операцию с другими файлами? [ДА,НЕТ]\n')
    if answer.upper() == 'ДА':
        main.main()
    else:
        print('Всего доброго!')
