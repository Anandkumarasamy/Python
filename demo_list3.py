#Write a Python program to get the difference between the two lists.
list1=[1,3,5,7,9]
list2=[1,2,4,6,7,8]
list3=list(set(list1+list2))
for num in list1:
    if num in list2:
        list3.remove(num)
print(list3)




