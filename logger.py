# логирование
from datetime import datetime as dt

def log_one_argument(text): # запись если введен один аргумент (слово)
    path = 'log_calc.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {text}\n')
    f.close()


def log_two_argument(text1, text2): # запись если введено два аргумента
    path = 'log_calc.csv'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a', encoding="utf-8")
    f.write(f'{time_sign}--> {text1} - {text2}\n')
    f.close()