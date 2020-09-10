list1=[10,20,30,40,40,40,70,80,99]
lis_element=eval(input('Enter the uniqe value:'))
count=0
for num in list1:
    if lis_element >= num < max(list1):
        count=count+1
print('Element are {}'.format(count))
