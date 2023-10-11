def word_replacement():
    str="this is a word replacement program,hi,hi,hi"
    word_to_replace=input("enter the word to repace:    ")
    new_word=input("enter the new word: ")
    print(str.replace(word_to_replace,new_word))

word_replacement()