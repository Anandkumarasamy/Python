#10.Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def exchange_char(string1):
    result=string1[(len(string1)-1)]+string1[1:(len(string1)-1)]+string1[0]
    return result
print(exchange_char('anandkumarasamy'))
