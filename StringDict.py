word=input("Enter the English Words:")
word2=[]
n=0
for i in word:
    n=word.count(i)
    if i not in word2:
        word2.append(i)
    else:
        continue
print(n)

