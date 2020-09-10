#11. Write a Python program to remove the characters which have odd index values of a given string.
def remove_oddnumber(string1):
    result=''
    for number in list(range((len(string1))+1)):
        if number%2 == 0:
            result=result+string1[number]
    return result
print(remove_oddnumber('anandkumarasamy'))