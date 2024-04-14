from src.errors import error_proxy
from enum import Enum

#
# Класс для описания настроек
#

class ReportFormat(Enum):
    CSV = 1
    Markdown = 2
    Json = 3
class settings():
    _name = ""
    _inn = ""
    _first_start = True
    _check = ""
    _corr_check = ""
    _bik = ""
    _type_of_company = ""
    _report_format = ReportFormat.CSV
    
    
    @property
    def inn(self):
        return self._inn
    
    @inn.setter
    def inn(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 12:
            error_proxy.set_error(Exception("Некорректный ИНН!"))

        self._inn = value.strip()
         
    @property     
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value:str):
        if not isinstance(value.strip(), str):
            error_proxy.set_error(Exception("Некорректное наименование!"))

        self._name = value.strip()

    @property    
    def is_first_start(self):

        return self._first_start    
            
    @is_first_start.setter        
    def is_first_start(self, value: bool):
        self._first_start = value

    @property
    def check(self):
        return self.__check

    @check.setter
    def check(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            error_proxy.set_error(Exception("Некорректный счет!"))

        self.__check = value.strip()

    @property
    def corr_check(self):
        return self.__corr_check

    @corr_check.setter
    def corr_check(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 11:
            error_proxy.set_error(Exception("Некорректный корреспондентский счет!"))

        self.__corr_check = value.strip()

    @property
    def bik(self):
        return self._bik

    @bik.setter
    def bik(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 9:
            error_proxy.set_error(Exception("Некорректный БИК!"))

        self._bik = value.strip()
        
    @property
    def report_mode(self):

        return self._mode

    @property
    def type_of_company(self):
        return self.__type_of_company

    @type_of_company.setter
    def type_of_company(self, value: str):
        if not isinstance(value.strip(), str) or len(value.strip()) != 5:
            error_proxy.set_error(Exception("Некорректный вид собственности!"))

        self.__type_of_company = value.strip()

    @property
    def report_format(self):
        return self._report_format

    @report_format.setter
    def report_format(self, value: ReportFormat):
        self._report_format = value
    