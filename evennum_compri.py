def even_num(lis):
    eve_lis=[]
    odd_lis=[]
    mode=input("Enter the mode(even or odd):")
    if mode == 'even':
        for num in lis:
            if num%2==0:
                eve_lis.append(num)
    else:
        for num in lis:
            if num%2!=0:
                odd_lis.append(num)
    result=eve_lis or odd_lis
    return result
print(even_num([2, 7, 5, 64, 14]))
    
