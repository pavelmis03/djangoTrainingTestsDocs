"""Модуль, который можно протестировать с помощью Unittest"""
from typing import List, Dict
from collections import Counter

class TextStatistic:
    def __init__(self, text: str):
        self.__text = text
        self.words = self.get_words()
        self.numbers = self.get_numbers()
        self.length = self.get_len()
        self.symbol_rate = self.get_symbol_rate()

    def get_words(self) -> List[str]:
        return self.__text.strip().split()

    def get_numbers(self) -> List[int]:
        res = []
        words = self.get_words()
        for word in words:
            if word.isnumeric():
                res.append(int(word))
        return res

    def get_len(self):
        return len(self.__text)

    def get_symbol_rate(self) -> Dict[str, int]:
        return dict(Counter(self.__text))

    def __iter__(self):
        data = {"Слова": self.words, "Числа": self.numbers, "Длина текста": self.get_len(),
                "Частотная статистика": self.get_symbol_rate()}
        return iter(data.items())
