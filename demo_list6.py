index_input=eval(input('Enter the value:'))
list1=[10, 30, 4, -6]
enum=enumerate(list1,1)
#print(list(enum))
for num in list(enum):
    if index_input in num:
        print(num[0])

'''num =[10, 30, 4, -6]
print(num.index(30))'''