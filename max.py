#Python program to find N largest elements from a list
def nth_largest(lis,larger):
    new_lis=[]
    count=0
    arrang=sorted(lis,reverse=True)
    for num in arrang:
        if num == arrang[larger-1]:
            new_lis.append(num)
            break
        else:
            new_lis.append(num)
    return new_lis
print(nth_largest([4, 5, 1, 2, 9],2))

    