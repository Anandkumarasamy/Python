#12. Write a Python program to count the occurrences of each word in a given sentence.
dict={}
def no_of_word(string1):
    for words in string1.split(' '):
        if words in dict:
            dict[words]=dict[words]+1
        else:
            dict[words]=1
    return dict
print(no_of_word('i am Anandkumarasamy'))
