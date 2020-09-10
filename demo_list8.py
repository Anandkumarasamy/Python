#30 Write a Python program to get the frequency of the elements in a list.
list1=[10,10,10,10,20,20,20,20,40,40,50,50,30]
dic={}
for num in list1:
    if num in dic:
        dic[num]=dic[num]+1
    else:
        dic[num]=1
print('the frequency of the elements:',dic)
list2=[]
for key,value in dic.items():
    for iterater in range(value):
        list2.append(key)
print('the normal list:',list2)

