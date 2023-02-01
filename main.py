from random import choice
import os
import stages

ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

with open('dict.txt', encoding='utf8') as f:
    content = f.read()

list_content = content.split(sep='\n')
filtered_content = [word for word in list_content if (word.find(' ') == -1 and 9 > len(word) > 5)]


class LettersInWord:
    """
    Нахождение букв в загаданном слове
    """

    def __init__(self, hidden_word: str):
        self.__hidden_word = hidden_word
        self.__word_in_progress = '_' * len(self.__hidden_word)
        self.__status = 'progress'  # / input error / wrong / ok / repeated
        self.__trys = 0

    @property
    def trys(self):
        return self.__trys

    @property
    def hidden_word(self):
        return self.__hidden_word

    @property
    def word_in_progress(self):
        return self.__word_in_progress

    @property
    def status(self):
        return self.__status

    # проверяет букву, изменяет статус, отсчитывает попытки
    def letter_check(self, letter_to_check):
        letter_to_check = letter_to_check.lower()

        if len(letter_to_check) != 1 or letter_to_check not in ALPHABET:
            self.__status = 'НЕВЕРНЫЙ ВВОД'

        elif letter_to_check in self.__hidden_word:
            tmp_list = [letter if letter == letter_to_check else '_' for letter in self.__hidden_word]

            self.__word_in_progress = self.__add_letter(tmp_list)

            if self.__word_in_progress == self.__hidden_word:
                self.__status = 'ПОБЕДА'

        else:
            self.__status = 'НЕТ ТАКОЙ БУКВЫ'
            self.__trys += 1

    # добавляет правильную букву в частично угаданное слово
    def __add_letter(self, another_try) -> str:
        tmp_list = list(self.__word_in_progress)

        for x in range(len(self.__word_in_progress)):
            if self.__word_in_progress[x] == '_' and another_try[x] != '_':
                tmp_list[x] = another_try[x]
                self.__status = 'ЕСТЬ ТАКАЯ БУКВА'
            elif self.__word_in_progress[x] == another_try[x] and self.__word_in_progress[x] != '_':
                self.__status = 'УЖЕ ВЫБИРАЛИ ЭТУ БУКВУ'

        self.__word_in_progress = ''.join(tmp_list)

        return self.__word_in_progress


def render(word_in_progress, trys, status):
    print(stages.return_gallows(trys, status))

    print('Загаданное слово: ', let.word_in_progress, f' ({len(word_in_progress)} букв)')
    print('Угадай букву: ', end='')


again = True

while again:
    print('1 - Начать игру', '\n2 - Выход')
    string = input()
    if string == '2':
        again = False
        break
    elif string == '1':

        let = LettersInWord(choice(filtered_content))

        while True:
            os.system('cls')
            if let.status == 'ПОБЕДА':
                print(stages.return_gallows(let.trys, let.status))
                break
            if let.trys >= 6:
                print(stages.return_gallows(6, f'Слово: {let.hidden_word.upper()} не отгадано'))
                break
            render(let.word_in_progress, let.trys, let.status)
            letter = input()
            if letter == 'exit':
                break
            let.letter_check(letter)
