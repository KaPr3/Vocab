import random
from TestFunctions import get_book, test

vocab = get_book(0)

def get_unit():
    unit = 0
    while unit == 0:
        temp_unit = int(input("Ktorá lekcia? "))
        if temp_unit > 0 and temp_unit < 13:
            return temp_unit
        else:
            print("Invalid input.")
            
unit = get_unit()

test_type = -1

test_type = int(input("Typ testu: (0 = normálny, 1 = inteligentný) "))

questions = int(input("Počet otázok? "))

test(test_type, questions, vocab[unit])

