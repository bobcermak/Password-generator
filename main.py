import random
import time

#Lists
class Lists:
    letters_list = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]

    numbers_list = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]

    symbols_list = [
        "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
        ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^",
        "_", "`", "{", "|", "}", "~"
    ]
    
#Functions
class Functions:
    def forPassword(countOfSymbols, inList):
        count = 0
        while count < int(countOfSymbols):
            rand = random.randint(0, len(inList) - 1)
            ourMainList.append(inList[rand])
            count += 1
            
    def mainFunction(mainList):
        Functions.forPassword(letter, Lists.letters_list)
        Functions.forPassword(num, Lists.numbers_list)
        Functions.forPassword(symb, Lists.symbols_list)
        
        random.shuffle(mainList)
        randomPassword = ''.join(mainList)
        return randomPassword

#Structure

#Main list
ourMainList = []
run = True

while run:
    try: 
        letter = input("Number of letters: ")
        num = input("Number of numbers: ")
        symb = input("Number of symbols: ")
        time.sleep(1)
        print(f"Your password is: {Functions.mainFunction(ourMainList)}")
        ourMainList.clear()
        ask = input("Do you wanna generate again?(y/n): ").lower()
        if ask == "y":
            print("Okay lets go to another: ")
            continue
        else:
            print("Goodbye :)")
            time.sleep(1)
            run = False
        
    except ValueError:
        print("Try again :(")
        time.sleep(1)

#NEPOUŽÍVAT class na zbytečné věci viz Structure
    