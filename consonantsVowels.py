

def alphabet_filter(word):
    # Write your code here
    word_vowels = ""
    word_consonants = ""
   
    i = 0
    while(i < len(word)):
        if(word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u"):
           word_vowels += word_vowels.join(word[i])
           
        else:
            word_consonants += word_consonants.join(word[i])
        i = i + 1

    print(word_vowels)  
    print(word_consonants)
    return word_consonants, word_vowels

alphabet_filter("github")

