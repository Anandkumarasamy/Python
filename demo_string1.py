#8. Write a Python function that takes a list of words and returns the length of the longest one

String1=input('Enter the String:')
dict={}
for word in String1.split(' '):
    word_len=len(word)
    dict[word_len]=word
print(dict[max(dict.keys())])
  
    
    
