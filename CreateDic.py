"""
NewSucc
Loads vocabulary from NewSucces, creates a Dictionary for each UNIT,
puts all the units in a tuple
"""

source = "NewSucc_INT.txt"

def create_dic(file):
    dic = {} #dictionary, one for each unit
    vocab = [] #list for all units
    doc = open(file, "r") #opens file
    prev_word = 0
    #dot = 44
    was_unit = False #was the previous line was the name of the unit
    prev_line = None #the whole previous line
    wordS = "" #the slovak word
    wordE = "" #the english word
    loading_slovak = False #should program load slovak word
    ignore_letter = False #should program ignore the current letter
    ignore_lines = 0 #how many lines should the program ignore
    
    def save_wordS(wordSk, wordEn, cut):
        """
        wordSk- slovak word
        wordEn- translation of the slovak words
        cut- the word that is supposed to be be cut from the end of wordSk
        """
        wordS = wordSk[2:]
        wordS = wordS[:wordS.find(cut)]
        wordS = wordS.strip()
        wordE = wordEn.strip()
        for i in range(2):
            if "\n" in wordS:
                wordS = wordS.replace("\n", " ")
        if "." in wordS:
            wordS = wordS[wordS.find(".")+3:]
        return wordE, wordS
                            
    for line in doc: #loops through each line
        if "NEW SUCCESS – INTERMEDIATE" in line:
            ignore_lines = 2
        elif ignore_lines > 0:
            ignore_lines += -1
        elif line[0].isalpha():
            if "UNIT" in line:
                if "UNIT 1" not in line and len(line) == 7:
                    saved_words = save_wordS(wordS, wordE, wordE)
                    dic[saved_words[0]] = saved_words[1]
                    wordS = ""
                    loading_slovak = False
                was_unit = True
                vocab.append(dic)
                dic = {}
            else:
                for letter in range(len(line)):
                    if line[letter] == "]":
                        ignore_letter = False
                    if line[letter] == "[":
                        ignore_letter = True
                        prev_wordE = wordE
                        if (line[letter-2] == "v" or line[letter-2] == "n") and line[letter-3] == " ":
                            wordE = line[prev_word:letter-3]
                        elif line[letter-4:letter-1] == "adj" or line[letter-4:letter-1] == "adv":
                            wordE = line[prev_word:letter-4]
                        elif "(adj, v)" in line:
                            wordE = line[prev_word:line.find("(adj, v)")]
                        else:
                            wordE = line[prev_word:letter-1]
                        
                        if not was_unit:
                            saved_words = save_wordS(wordS, prev_wordE, wordE)
                            dic[saved_words[0]] = saved_words[1]
                            wordS = ""
                            loading_slovak = False
                            
                    if not ignore_letter and (line[letter] == "." or line[letter] == "!" or line[letter] == "?"):
                        #dot = letter
                        loading_slovak = True

                    if loading_slovak:
                        wordS = wordS + line[letter]
                prev_line = line
                was_unit = False
                
    saved_words = save_wordS(wordS, wordE, wordE)
    dic[saved_words[0]] = saved_words[1]
    vocab.append(dic)
    return vocab

if __name__ == "__main__":
    vocab = create_dic(source)
    n = 0

    def debug(unit):
        for a, s in vocab[unit].items():
            if s == "":
               print(a + ": " + s)
            if "[" in a or "]" in a or "[" in s or "]" in s:
                print(a + ": " + s)
    def print_all(unit):
        for a, s in vocab[unit].items():
            print(a + ": " + s)
       
    #debug(9)
    print_all(9)
