import os
import sys

from lxml import etree
from lxml.etree import XMLSyntaxError



class XmlOperator:

    def __init__(self, log):
        self.logger = log

    def validate_xml(self, xml, xsd):

        try:
            self.logger.info_message('Валидация XML файла.')
            schema_root = etree.parse(xsd)
            schema = etree.XMLSchema(schema_root)
            load_xml = etree.parse(xml)
            result = schema.validate(load_xml)
            self.xml = xml
            self.logger.info_message('Валидация XML файла успешно завершена.')

            return True

        except XMLSyntaxError as err:
            self.logger.error_message('Валидация XML файла по XSD схеме не осуществилась.')
            self.logger.error_message('Произошла синтаксическая ошибка. Проверьте файлы и повторите снова.')
            self.logger.error_message('Ошибка: {}'.format(err))

        except:
            err = sys.exc_info()
            self.logger.error_message('Валидация XML файла по XSD схеме не осуществилась.')
            self.logger.error_message('Произошла ошибка. Проверьте файлы и повторите снова.')
            self.logger.error_message('Ошибка: {}'.format(err))

    def transform_by_xslt(self, xsl):

        try:
            self.logger.info_message('Трансформация файла по XSLT')
            load_xml = etree.parse(self.xml)
            load_xsl = etree.parse(xsl)
            transform = etree.XSLT(load_xsl)
            new_xml = transform(load_xml)
            self.new_xml = new_xml
            self.logger.info_message('Трансформация файла по XSLT успешно завершена.')

            return True

        except XMLSyntaxError as err:
            self.logger.error_message('Трансформация файла по XSLT не осуществилась.')
            self.logger.error_message('Произошла синтаксическая ошибка. Проверьте файлы и повторите снова.')
            self.logger.error_message('Ошибка: {}'.format(err))

        except:
            err = sys.exc_info()
            self.logger.error_message('Трансформация файла по XSLT не осуществилась.')
            self.logger.error_message('Произошла ошибка. Проверьте файлы и повторите снова.')
            self.logger.error_message('Ошибка: {}'.format(err))

    def result_file(self, files):
        valid_name = False
        while valid_name is False:
            name_xml = input('Введите название преобразованного файла XML: ')
            if name_xml + '.xml' in files:
                print('Файл с таким именем существует.')
            else:
                valid_name = True

        return name_xml

    def save_result(self, name_xml):
        infile = etree.tostring(self.new_xml, pretty_print=True)
        new_file = r'results\{}.xml'.format(name_xml)
        outfile = open(new_file, 'a')
        outfile.write(str(infile))

        self.logger.info_message('Новый файл успешно сохранен!')
        self.logger.info_message('Его путь  --  {}'.format(os.path.abspath(new_file)))
        self.logger.info_message('Сессия завершена.')

        return os.path.abspath(new_file)
