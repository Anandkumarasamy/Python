#Python program to remove Nth occurrence of the given word

def Nth_occurrence(lst, word, N):
    newlis=[]
    count=0
    for one_word in lst:
        if one_word == word:
            count=count+1
            if count != N:
                newlis.append(one_word)
        else:
            newlis.append(one_word)
    if count==0:
        print('the',word,'is not found in given list(',lst,')' )
    else:
        print(newlis)
Nth_occurrence(["he", "is", "ankit", "is", "raj", "is","ankit raj"], "is", 2) 
