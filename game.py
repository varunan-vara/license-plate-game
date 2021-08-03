# Program to calculate all possible answers to the 'License Plate Game'

# Establish inputs
print("***License Plate Games***")       
print("Note: \n1. Ignore the First Letter of the Plate\n2. Input all letters in Lower Case\n*************************")
print("First Letter")
char1 = str(input())
print("Second Letter")
char2 = str(input())
print("Third Letter")
char3 = str(input())
print("Calculating all possible words")

import re

file_handle = open("words.txt","r")
_wordslist = file_handle.readlines()
wordslist = []
for words in _wordslist:
    pattern = r"\n"
    wordsstr = re.sub(pattern, "", words)
    wordslist.append(wordsstr)

def split(wordy):
    return [char for char in wordy]

answerlist = []
for word in wordslist:
    listy = split(word)
    if (char1 not in listy):
        continue
    else:
        index1 = listy.index(char1, 0)
        shortlisty = listy[(index1 + 1) : len(listy)]
        if (char2 not in shortlisty):
            continue
        else:
            index2 = shortlisty.index(char2, 0)
            shorterlisty = shortlisty[(index2 + 1) : len(shortlisty)]
            if (char3 not in shorterlisty):
                continue
            else:
                answerlist.append(word)

for answer in answerlist:
    print(answer)