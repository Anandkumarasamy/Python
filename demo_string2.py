#9. Write a Python program to remove the nth index character from a nonempty string.
 
def nth_index_remove(string1):
     nth_index=int(input("Enter the number:"))
     result=string1[:nth_index]+string1[(nth_index+1):]
     return result
res=nth_index_remove('Anandkumarasamy')
print(res)