"""
Модуль, который анализирует статьи и предоставляет статистику по ним
"""
from typing import List, Dict
from collections import Counter

class TextStatistic:
    """
    Построение статистики по статье
    """
    def __init__(self, text: str):
        """
        Конструктор
        :param text: текст статьи
        :type: str
        """
        self.__text = text
        self.words = self.get_words()
        self.numbers = self.get_numbers()
        self.length = self.get_len()
        self.symbol_rate = self.get_symbol_rate()

    def get_words(self) -> List[str]:
        """
        Разделяет полученную статью на слова
        :return: список слов
        :rtype: List[str]
        """
        return self.__text.strip().split()

    def get_numbers(self) -> List[int]:
        """
        выделяет из массива слов те, что являются числами
        :return: массив массив чисел, выделенных в тексте
        :rtype: List[int]
        """
        res = []
        words = self.get_words()
        for word in words:
            if word.isnumeric():
                res.append(int(word))
        return res

    def get_len(self):
        """
        получение длины текста
        :return: длину текста
        :rtype: int
        """
        return len(self.__text)

    def get_symbol_rate(self) -> Dict[str, int]:
        """
        Возвращает частотную статистику
        :return: словарь частотной статистики
        :rtype: Dict
        """
        return dict(Counter(self.__text))

    def __iter__(self):
        """
        Статистика по статье
        :return: словарь со статистикой
        :rtype: iterator
        """
        data = {"Слова": self.words, "Числа": self.numbers, "Длина текста": self.get_len(),
                "Частотная статистика": self.get_symbol_rate()}
        return iter(data.items())
