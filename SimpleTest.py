import random
from CreateDic import create_dic

source = "NewSucc_INT.txt"
vocab = create_dic(source)

unit = 0
def get_unit():
    while unit == 0:
        temp_unit = int(input("Ktorá lekcia? "))
        if temp_unit > 0 and temp_unit < 13:
            unit = temp_unit
        else:
            print("Invalid input.")

unit = 9

def test():
    wordE = random.choice(list(vocab[unit].keys()))
    wordS = vocab[unit][wordE]
    user_word = input(wordS + " ")

    if user_word == wordE:
        print("Good job!")
    else:
        print("Wrong! The correct word is: " + wordE)

while True:
    test()
