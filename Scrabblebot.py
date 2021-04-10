from collections import Counter

f = open('words.txt','r')
dictionary = f.read() #reads the dictionary .txt file
dictionary = [x.lower() for x in dictionary.split('\n')] #splits each word after \n in the dictionary (\n comes after every line break in the txt file) and creates a list with each word separated 
print((len(dictionary)), 'words on record') #returns the number of words in the dictionary


def solver(letters: str) -> list:
    letters = letters.lower() #takes the function input(in this case n) and makes all the letters lower case
    letters_count = Counter(letters) #uses the counter function to assign a count of each letter in the input ie hello = h:1, e:1, l:2, o:1
    anagrams = set() #creates an empty set named anagrams
    for word in dictionary: # iterates through each word in the dictionary file
        if not set(word) - set(letters): #checks to see whether the tested word and the inputed word have letters in common, if the result of the operation is zero then the all the letters in the tested word are in the inputted word so they return an empty set (false) and the if not command moves the code on
            check_word = set() # creates a new empty set
            for k, v in Counter(word).items(): 
                if v <= letters_count[k]:#compares number of times one letter occurs in the tested word with the inputted word (counter function returns how many times a given letter appears) 
                    check_word.add(k) # if it passes the test, the letter is added to the check word set
            if check_word == set(word): # checks to see if the sets are equal
                anagrams.add(word)# if they are the word is added to the list.
    anagrams.remove('')
    return sorted(list(anagrams), key = lambda x: len(x))


while True:
    n = input('Please enter word: ')
    print(solver(n))
