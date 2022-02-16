import re
from abc import ABC


class Params(ABC):
    """
    Класс. Описывает установку и проверку параметров пользователя
     (язык, валюта)
    """

    @staticmethod
    def check_lang(data, text):
        """Проверка флага на установленный пользователем язык"""
        if data['lang_flag'] is False:
            return Params.set_lang(text)

    @staticmethod
    def check_cur(data, text):
        """Проверка флага на установленную пользователем валюту"""
        if data['cur_flag'] is False:
            return Params.set_cur(text)

    @staticmethod
    def set_lang(text):
        """Определение языка"""
        if bool(re.search(r'[А-Яа-я]', text)):
            return 'ru_RU'
        return 'ru_RU'

    @staticmethod
    def set_cur(text):
        """Определение валюты"""
        if bool(re.search(r'[А-Яа-я]', text)):
            return 'RUB'
        return 'USD'