import os

from lxml import etree
from lxml.etree import XMLSyntaxError


class XmlOperator:

    def __init__(self, log):
        self.logger = log

    def validate_xml(self, xml, xsd):
        """ Валидация XML файла """
        self.logger.info_message('Валидация XML файла.')
        try:
            schema_root = etree.parse(xsd)
            schema = etree.XMLSchema(schema_root)
            load_xml = etree.parse(xml)
            is_valid = schema.validate(load_xml)
        except Exception as err:
            self.logger.error_notification(
                'При валидации XML файла произошла ошибка.', err
            )
        else:
            if is_valid:
                self.xml = xml
                self.logger.info_message('Валидация XML файла успешно завершена.')
                return True
            self.logger.error_message('Файл не прошел валидацию.')
            return False

    def transform_by_xslt(self, xsl):
        """ Трансформация файла по XSLT """
        self.logger.info_message('Трансформация файла по XSLT')
        try:
            load_xml = etree.parse(self.xml)
            load_xsl = etree.parse(xsl)
            transform = etree.XSLT(load_xsl)
            new_xml = transform(load_xml)
        except Exception as err:
            self.logger.error_notification(
                err, 'При трансформации файла по XSLT произошла ошибка.'
            )
            return False
        else:
            self.new_xml = new_xml
            self.logger.info_message('Трансформация файла по XSLT успешно завершена.')
            return True

    def get_xml_filename(self, files):
        """ Метод получения имени результирующего файла """
        valid_name = False
        while valid_name is False:
            name_xml = input('Введите название преобразованного файла XML: ')
            if f'{name_xml}.xml' in files:
                print('Файл с таким именем существует.')
            else:
                valid_name = True

        return name_xml

    def save_result(self, name_xml):
        """ Метод сохраняющий файл с результатом и возвращающий путь до него """
        # infile = etree.tostring(self.new_xml, pretty_print=True)
        if 'results' not in os.listdir(os.getcwd()):
            os.mkdir('results')
        with open(f'results/{name_xml}.xml', 'a') as xml_file:
            xml_file.write(str(self.new_xml))
        
        result_filepath = os.path.abspath(f'results/{name_xml}.xml')
        self.logger.info_message('Новый файл успешно сохранен!')
        self.logger.info_message(f'Его путь  --  {result_filepath}')
        self.logger.info_message('Сессия завершена.')

        return result_filepath
