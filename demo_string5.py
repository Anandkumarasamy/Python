#14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Go to the editor
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red

sort_order=input("Enter the Colour:")
lis_order=list(sort_order.split(','))
result=sorted(lis_order,reverse=False)
print(result)
