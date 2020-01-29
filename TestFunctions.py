import random
from CreateDic import create_dic

def get_book(book):
    if book == 0:
        source = "NewSucc_INT.txt"
    elif book == 1:
        source = "NewSucc_UPP.txt"

    return create_dic(source)


def check_word(correct, user):
    correct_list = [correct]
    correct_list.append(correct[:correct.find("(")])
    correct_list.append(correct.lower())
    
    if "/" in correct:
        correct_list.append(correct[:correct.find("/")])
        correct_list.append(correct[correct.find("/"):])

    if "’" in correct:
        correct_list.append(correct.replace("’", "'"))
        correct_list.append(correct.replace("’", "´"))

    if "sth" in correct:
        correct_list.append(correct.replace("sth", "something"))
        
    for word in correct_list:
        if user == word:
            return True

    return False


def test(test_type, questions, unit_list):
    def classic():
        for i in range(questions):
            wordE = random.choice(list(unit_list.keys()))
            wordS = unit_list[wordE]
            user_word = input(wordS + ": ")
            unit_list.pop(wordE)

            if check_word(wordE, user_word):
                print("Good job!")
            else:
                print("Wrong! The correct word is: " + wordE)

    def intelligent():
        pass
    
    if test_type == 0:
        classic()
    elif test_type == 1:
        classic()
        
if __name__ == "__main__":
    vocab = get_book(0)
    test(0, 10, vocab[9])
